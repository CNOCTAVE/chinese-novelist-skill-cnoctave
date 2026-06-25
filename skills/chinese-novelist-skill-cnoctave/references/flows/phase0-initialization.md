# 第0步：初始化与偏好加载

**每次触发SKILL时首先执行：**

## 0. 展示流程一览表

进入 skill 时，首先向用户展示以下流程表格（表格内容直接打印，供用户了解所有可用 flow 的编号、文件名和标题）：

| 编号 | 文件名 | 标题 |
|------|--------|------|
| Phase 0 | phase0-initialization.md | 初始化与偏好加载 |
| Phase 1·L1 | phase1-layer1-core.md | 第一层：核心定位（必答3问） |
| Phase 1·L2 | phase1-layer2-customize.md | 第二层：深度定制与创作规格 |
| Phase 1·L3 | phase1-layer3-title.md | 第三层：标题生成 |
| Phase 2 | phase2-planning.md | 规划 + 二次确认 |
| Phase 3 | phase3-writing.md | 疯狂创作 |
| Phase 4 | phase4-validation.md | 自动校验与修复 |
| Phase 5★ | phase5-woman-gushimaodun.md | （可选）故事矛盾增强（多用于女频） |
| Phase 6★ | phase6-man-gushidairugan.md | （可选）故事代入感增强（多用于男频） |
| Phase 1000★ | phase1000-remove-duplicates.md | （可选）AI 查重与去重优化 |
| — | shared-infrastructure.md | 共享机制（跨阶段引用，不单独运行） |

> 标记 ★ 的为可选阶段，在创作完成后通过 AskUserQuestion 选择是否运行。
> 如果提示某个 flow 文件不存在，说明该文件已被删除，可联系 skill 维护者获取。

## 1. 读取用户偏好

检查 `user-preferences.json` 是否存在
- 存在 → 加载偏好数据，用于后续选项排序、推荐标记、个性化欢迎语
- 不存在 → 使用默认值，首次交互结束后自动创建

偏好数据结构与更新规则详见 → [shared-infrastructure.md](shared-infrastructure.md)

## 2. 快捷入口检测

分析用户的首次输入是否已包含丰富的创作信息（题材、主角、冲突等关键要素）

- 如果信息充足 → 使用 AskUserQuestion 展示提取结果，提供三个选项：
  [A] 是的，直接开始规划 → 跳过问答，进入第二阶段
  [B] 先展示提取的信息让我确认/修改 → 展示配置供确认后进入规划
  [C] 不，我还是想走一遍问答流程 → 进入第一层问答
- 如果信息不足 → 直接进入第一层问答

## 3. 个性化欢迎

（如有偏好数据）：

> "欢迎回来！基于你之前的创作习惯，我为你做了一些推荐（标记为⭐的选项）。"

## 4. 中断续写检测

扫描 `./chinese-novelist/` 目录下的项目文件夹：

- 查找含 `02-写作计划.json` 且 `status` 为 `"in_progress"` 或 `"validating"` 的项目
- 如果找到未完成项目：
  - 展示项目信息：小说名称、完成进度（X/Y 章已完成）
  - 使用 AskUserQuestion 提供选项：
    [A] 继续上次创作 → 直接进入第三阶段，从中断章节继续
    [B] 开始新作品 → 进入第一层问答
- 如果未找到 → 正常进入快捷入口检测或第一层问答
