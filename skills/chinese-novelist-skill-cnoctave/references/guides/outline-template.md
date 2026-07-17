# 大纲模板

Phase 2 创建 `01-大纲.json`，使用以下 JSON 结构。

文件格式为 JSON，方便程序修改和读取。每个章节的规划信息作为数组元素存储，章节摘要创作后追加。

## JSON 结构

```json
{
  "version": 1,
  "novelName": "[小说名称]",
  "genre": "[题材]",
  "totalChapters": 20,
  "targetWordsPerChapter": 3000,
  "totalWordCountEstimate": "[约X万字]",
  "coreConflict": "[主角想要什么？什么阻止了他？]",
  "chapters": [
    {
      "chapterNumber": 1,
      "title": "[章节标题]",
      "coreEvent": "[本章核心事件]",
      "continuationFromPrevious": "[承接上章，第1章填\"-\"]",
      "hookType": "[章首引子类型，参考hook-techniques.md]",
      "cliffhanger": "[本章结尾悬念钩子]",
      "characters": ["出场人物1", "出场人物2"],
      "scenes": ["场景1", "场景2"],
      "keyEvents": ["关键词1", "关键词2", "关键词3", "关键词4", "关键词5", "关键词6", "关键词7", "关键词8", "关键词9", "关键词10"],
      "summary": ""
    },
    {
      "chapterNumber": 2,
      "title": "[章节标题]",
      "coreEvent": "[本章核心事件]",
      "continuationFromPrevious": "[回应第1章结尾的悬念]",
      "hookType": "[章首引子类型]",
      "cliffhanger": "[本章结尾悬念钩子]",
      "characters": ["出场人物1", "出场人物2"],
      "scenes": ["场景1", "场景2"],
      "keyEvents": ["关键词1", "关键词2", "关键词3", "关键词4", "关键词5", "关键词6", "关键词7", "关键词8", "关键词9", "关键词10"],
      "summary": ""
    }
  ],
  "mysteries": {
    "main": "[主线核心悬念]",
    "sub": "[支线悬念]",
    "finalReveal": "[终极揭秘]"
  }
}
```

## 字段说明

| 字段 | 位置 | 必填 | 说明 |
|------|------|------|------|
| `chapterNumber` | chapters[] | ✅ | 章节序号 |
| `title` | chapters[] | ✅ | 章节标题 |
| `coreEvent` | chapters[] | ✅ | 本章核心事件（一句话概括） |
| `continuationFromPrevious` | chapters[] | ✅ | 如何承接上一章的悬念 |
| `cliffhanger` | chapters[] | ✅ | 本章结尾的悬念钩子 |
| `characters` | chapters[] | ✅ | 出场人物列表 |
| `scenes` | chapters[] | ✅ | 场景列表 |
| `keyEvents` | chapters[] | ✅ | 至少10个关键词，其中至少7个名词 |
| `summary` | chapters[] | Phase 3 填充 | 创作完成后追加 300-500 字摘要 |

## 用法

- **Phase 2**：创建文件时按此结构填充完整的章节规划
- **Phase 3**：每章创作前读取此文件，找到当前章节的规划信息
- **Phase 3 收尾**：在对应章节的 `summary` 字段追加 300-500 字摘要
- **修改**：直接编辑 JSON 文件，增删章节或修改规划
- **字数目标**：每章目标字数 = 本章 `scenes` 场景数量 × 1000（即大纲中**每个场景至少写 1000 字**），`targetWordsPerChapter` 仅作整体估算参考

详见 [plot-structures.md](plot-structures.md) 获取情节结构技法。
