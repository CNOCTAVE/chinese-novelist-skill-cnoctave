# 第二阶段：规划 + 二次确认

> **前置条件**：本阶段使用 Phase 1 Layer 3 用户确认的小说标题。标题信息从对话上下文中获取，用于命名项目目录、写入大纲文件头和写作计划 JSON。

执行以下步骤：

1. **创建项目文件夹**：`./chinese-novelist/{YYYYMMDD-HHmmss}-{Layer 3 确认的标题}/`（相对当前工作目录，使用用户在 Layer 3 选定的小说标题）
2. **生成人物档案**：创建 `00-人物档案.json`，使用 [character-template.md](../guides/character-template.md) 模板的 JSON 结构，参考 [character-building.md](../guides/character-building.md) 创建主角、反派、配角档案。**人物档案必须详细**：每个角色的性格核心、致命缺陷、说话风格/口头禅、恐惧/弱项、背景故事都要具体到可以直接指导写作的程度
3. **生成大纲**：创建 `01-大纲.json`，使用 [outline-template.md](../guides/outline-template.md) 模板的 JSON 结构，参考 [plot-structures.md](../guides/plot-structures.md) 填入完整的章节规划。**大纲必须以人物驱动情节** 参照 `00-人物档案.json`，确保情节服务于人物成长弧线。大纲中的keyEvents字段必须编写至少10个关键词，其中必须至少包含7个名词
4. **生成写作计划**：创建 `02-写作计划.json`，基于大纲内容填充，结构如下：
   ```json
   {
     "version": 1,
     "novelName": "[小说名称]",
     "projectPath": "./chinese-novelist/{timestamp}-[小说名称]",
     "totalChapters": [章节数],
     "minWordsPerChapter": 3000,
     "createdAt": "[ISO时间]",
     "updatedAt": "[ISO时间]",
     "status": "planning",
     "writingMode": "[serial|subagent-parallel|agent-teams]",
     "chapters": [
       {
         "chapterNumber": 1,
         "title": "[章节标题]",
         "filePath": "第01章-[章节标题].md",
         "status": "pending",
         "wordCount": null,
         "wordCountPass": null,
         "retryCount": 0
       }
     ]
   }
   ```

完成后，执行以下三步：

**1. 展示规划摘要并请求确认**

向用户展示规划摘要（小说名称、总章数、目标字数、主要人物）并请求确认。

**2. 是否现在开始写作**

使用 AskUserQuestion 询问：

Question: 大纲与人物设定已生成。现在就开始写作吗？
[A] 开始写作（推荐）→ 进入步骤 3 选择写作模式，随后自动创作
[B] 暂停，让我先修改人物设定和大纲 → skill 输出文件路径后停止，等待你修改

- 若用户选择 **[B]**：
  1. 保持 `02-写作计划.json` 的 `status` 为 `"planning"`（不进入创作）
  2. **清晰输出以下两个文件的完整路径**（基于 `projectPath`）：
     - 人物设定文件：`{projectPath}/00-人物档案.json`
     - 大纲文件：`{projectPath}/01-大纲.json`
  3. 提示用户可直接编辑这两个文件来修改人物与剧情，并在**下一次对话**中输入类似「继续写作」「接着写」「开始写」等字样，skill 会按修改后的设定继续创作
  4. **停止运行**，不进入第三阶段

**3. 写作模式选择**（仅当用户选择 [A] 时执行）

使用 AskUserQuestion 询问：

Question: 选择写作模式
[A] 逐章串行（主 Agent 自己逐章写，写完一章立即校验再写下一章，全程无中断，适合短中篇）
[B] 子Agent逐章（主 Agent 逐章派生子 Agent，每个子 Agent 只写当前这一章，写完即校验，适合中长篇）
[C] Agent Teams（Claude Code 多 Agent 协作模式，每章一个任务、一次认领一章，Agent 间可通讯，需手动开启）

> 三种模式均遵循【逐章执行】原则：无论哪种模式，都一次只处理一章，当前章写完并校验通过后才进入下一章。

用户选择后：
- 更新 `02-写作计划.json` 的 `writingMode` 字段
- 更新 `status` 为 `"in_progress"`
- 进入第三阶段：疯狂创作 → 详见 [phase3-writing.md](phase3-writing.md)
