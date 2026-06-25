# 人物档案模板

Phase 2 创建 `00-人物档案.json`，使用以下 JSON 结构。

文件格式为 JSON，方便程序修改和读取。所有角色分三类：主角、反派、配角。

## JSON 结构

```json
{
  "version": 1,
  "novelName": "[小说名称]",
  "characters": {
    "protagonists": [
      {
        "id": "protagonist-1",
        "name": "[角色一姓名]",
        "age_occupation": "[年龄/职业]",
        "appearance": "[外貌特征]",
        "core_personality": "[性格核心]",
        "core_values": "[核心价值观]",
        "greatest_fear": "[最大恐惧]",
        "fatal_flaw": "[致命缺陷]",
        "inner_desire": "[内心渴望]",
        "backstory": "[背景故事]",
        "mbti": "[MBTI类型]",
        "speaking_style": "[说话风格/口头禅]",
        "weakness": "[恐惧/弱项]",
        "relationships": "[与其他角色的关系]"
      },
      {
        "id": "protagonist-2",
        "name": "[角色二姓名]"
      }
    ],
    "antagonists": [
      {
        "id": "antagonist-1",
        "name": "[反派姓名]",
        "age_occupation": "[年龄/职业]",
        "appearance": "[外貌特征]",
        "core_personality": "[性格核心]",
        "core_values": "[核心价值观]",
        "greatest_fear": "[最大恐惧]",
        "fatal_flaw": "[致命缺陷]",
        "inner_desire": "[内心渴望]",
        "backstory": "[背景故事]",
        "mbti": "[MBTI类型]",
        "speaking_style": "[说话风格/口头禅]",
        "weakness": "[恐惧/弱项]",
        "relationships": "[与其他角色的关系]"
      }
    ],
    "supporting": [
      {
        "id": "supporting-1",
        "name": "[配角姓名]",
        "core_personality": "[性格核心]",
        "speaking_style": "[说话风格]",
        "relationships": "[与主角关系]"
      }
    ]
  }
}
```

## 字段说明

| 字段 | 必填 | 说明 |
|------|------|------|
| `id` | ✅ | 角色唯一标识，如 `protagonist-1`、`antagonist-1` |
| `name` | ✅ | 角色姓名 |
| `core_personality` | ✅ | 性格核心（直接指导写作行为） |
| `fatal_flaw` | ✅ | 致命缺陷（推动冲突的内在源动力） |
| `speaking_style` | ✅ | 说话风格/口头禅（确保对话个性化） |
| `weakness` | ✅ | 恐惧/弱项（制造张力） |
| `relationships` | ✅ | 与其他角色的关系（指导互动） |
| 其余字段 | 推荐 | 越详细越能指导一致性写作 |

## 用法

- **Phase 2**：创建文件时按此结构填充完整 JSON
- **Phase 3**：每章创作前读取此文件，提取出场角色的核心信息
- **修改**：直接编辑 JSON 文件，字段增删不影响解析

详见 [character-building.md](character-building.md) 获取人物塑造技法。
