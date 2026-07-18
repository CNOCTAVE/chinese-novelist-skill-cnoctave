---
name: chinese-novelist-skill-cnoctave
description: |
  分章节创作引人入胜的中文小说。支持各种题材（悬疑/言情/奇幻/科幻/历史等），支持10-50章长篇创作，大纲每个场景至少写1000字（每章目标字数 = 场景数 × 1000），结尾设置悬念钩子。强调深度润色去除AI痕迹，确保文字自然流畅。
  当用户要求：写小说、创作故事、分章节写作、连续剧情、章节悬念、长篇小说时使用。
metadata:
  trigger: 创作中文小说、分章节故事、长篇小说创作
  source: 基于小说创作最佳实践设计
license: MIT
---

# chinese-novelist-skill-cnoctave: 中文小说创作助手

## 三大黄金法则

1. **展示而非讲述** - 用动作和对话表现，不要直接陈述
2. **冲突驱动剧情** - 每章必须有冲突或转折
3. **悬念承上启下** - 每章结尾必须留下钩子

## 特性说明

- **中断续写**：自动检测未完成项目，从断点继续创作
- **大纲可编辑后继续**：写完大纲与人物设定后可暂停，输出文件路径供用户修改；后续对话输入「继续写作」等字样即按修改后的设定续写
- **自动校验**：创作完成后自动检查字数和质量，不合格自动修复
- **并行写作**（可选）：支持子Agent/Teams 批次并发写作（同一批次多章同时创作），通过每章独立状态文件避免并发冲突，大纲前置规划保证剧情衔接

## 核心流程

进入每个阶段时，先阅读对应的流程文档以获取详细执行指令。

### 第0步：初始化与偏好加载

读取用户偏好，检测未完成项目（中断续写），并检测「继续写作」等字样以恢复用户修改过大纲/人物设定后的项目，展示个性化欢迎。 → 详见 [phase0-initialization.md](references/flows/phase0-initialization.md)

### 第一阶段：三层递进式问答

通过递进式问答收集创作需求，确定小说定位与标题：

- **核心定位**（必答，Q1-Q3）：题材创意、主角设定、核心冲突 → 详见 [phase1-layer1-core.md](references/flows/phase1-layer1-core.md)
- **深度定制与规格**（Q4-Q8）：世界观、视角基调、核心主题、读者定位、章节数量、配置确认 → 详见 [phase1-layer2-customize.md](references/flows/phase1-layer2-customize.md)
- **标题生成**：AI 基于创意元素生成候选标题，用户选择或自定义 → 详见 [phase1-layer3-title.md](references/flows/phase1-layer3-title.md)

### 第二阶段：规划 + 二次确认

创建项目文件夹（`./chinese-novelist/{timestamp}-{小说名称}/`），生成大纲、人物档案和写作计划JSON，等待用户确认。确认后用户可选择**立即开始写作**或**暂停并修改**：选择暂停时，skill 输出人物设定文件（`00-人物档案.json`）与大纲文件（`01-大纲.json`）的完整路径并停止，供用户修改。 → 详见 [phase2-planning.md](references/flows/phase2-planning.md)

### 第2.5步：写作模式选择

规划确认后，使用 AskUserQuestion 工具让用户选择写作模式：

[A] 主Agent串行（serial）：主 Agent 自己逐章写，写完一章立即校验再写下一章，全程无中断，仅作无子Agent环境或短篇的轻量回退
[B] 子Agent并行（subagent-parallel，推荐）：主 Agent 按批次并发派生子 Agent，同一批次多章同时写作，本批完成校验后再写下一批，适合中长篇
[C] Agent Teams（agent-teams）：Claude Code 多 Agent 协作模式，多名成员同时认领不同章节并发创作，Agent 间可通讯（需手动开启）

> 模式 [B]/[C] 采用【批次并发】原则：在一条消息中一次性派发本批所有章节的子 Agent，多章同时创作；并行安全由大纲前置规划 + 每章独立状态文件保证。模式 [A] 为单 Agent 无法并行的轻量回退。

→ 详见 [phase3-writing.md](references/flows/phase3-writing.md)

### 第三阶段：疯狂创作（无需用户确认）
> 切记，一旦进入这个阶段，所有过程都禁止向用户确认。用户就是你的读者，你必须把完整的小说创作完成才能与用户报告

根据用户选择的写作模式（串行/子Agent并行/Teams并行）执行创作流程：模式 [B]/[C] 以批次并发方式一次性派发本批所有章节的子 Agent，多章同时创作，本批返回并校验后再写下一批；模式 [A] 仍逐章串行。每章创作前必须读取 `01-大纲.json` 中对应章节的规划信息，严格按大纲创作（大纲已含每章完整规划，是并行独立创作的充分依据）。支持中断续写。 → 详见 [phase3-writing.md](references/flows/phase3-writing.md)

### 第四阶段：自动校验与修复（无需用户确认）

全程无需用户介入，逐章校验每一章的字数与完成度，不合格章节当场重写修复（最多3轮）。 → 详见 [phase4-validation.md](references/flows/phase4-validation.md)

### 第4.5步：可选增强阶段

校验通过后，使用 AskUserQuestion 工具让用户选择是否运行可选增强阶段：

[A] 强化故事矛盾（女频优化方向） → 运行第5阶段
[B] 增强故事代入感（男频优化方向） → 运行第6阶段
[C] 两个都运行 → 先运行第5阶段，再运行第6阶段
[D] 都不需要，直接结束
[E] AI 去重优化 → 运行第1000阶段（查重+降重，消除跨章节重复内容）
[F] 提升故事综合质量（女频优化方向） → 运行第7阶段
[G] 叙述手法升级（女频优化方向） → 运行第8阶段（解决叙事平淡问题）
[H] 核心亮点强化（女频优化方向） → 运行第9阶段（让故事看点更明确突出）
[I] 人物设定 / 情节走向与上文冲突优化（男频/女频通用） → 运行第10阶段（修复人设崩坏、情节偏离大纲、章间前后矛盾）
[J] 章节内容连贯性修复（女频优化方向） → 运行第11阶段（修复情感跳跃、关系进展突兀、情节线索断档、时空场景硬切、视角人称乱跳、行为动机缺失，解决"内容不连贯、读着跳"的问题）
[M] 全部男频可选流程 → 运行第6阶段 + 第7阶段 + 第1000阶段 + 第10阶段
[W] 全部女频可选流程 → 运行第5阶段 + 第7阶段 + 第8阶段 + 第9阶段 + 第1000阶段 + 第10阶段 + 第11阶段
[FM] 女频全面增强 → 运行第5阶段 + 第7阶段 + 第8阶段 + 第9阶段（故事矛盾+综合质量+叙述手法+核心亮点）

→ 根据用户选择进入 [phase5-woman-gushimaodun.md](references/flows/phase5-woman-gushimaodun.md) 和/或 [phase6-man-gushidairugan.md](references/flows/phase6-man-gushidairugan.md) 和/或 [phase1000-remove-duplicates.md](references/flows/phase1000-remove-duplicates.md) 和/或 [phase7-improve-the-overall-quality-of-the-story.md](references/flows/phase7-improve-the-overall-quality-of-the-story.md) 和/或 [phase8-improve-narrative-tension.md](references/flows/phase8-improve-narrative-tension.md) 和/或 [phase9-highlight-core-appeal.md](references/flows/phase9-highlight-core-appeal.md) 和/或 [phase10-conflict-resolution.md](references/flows/phase10-conflict-resolution.md) 和/或 [phase11-fix-chapter-incoherence.md](references/flows/phase11-fix-chapter-incoherence.md)

## 共享机制

偏好系统、写作计划系统、黄金法则详解、字数检查脚本等跨阶段共享机制。 → 详见 [shared-infrastructure.md](references/flows/shared-infrastructure.md)
