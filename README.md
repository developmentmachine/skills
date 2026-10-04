# Skills 与 Plugin 分享素材

两期材料。第一期讲怎么用 skill 让 agent 按指定做法做事，并用对照证明它照做了。第二期讲 Plugin：怎么把 skill 和 MCP 打成可安装的包，按基础、进阶、高级使用来讲。

第一期对齐这四份公开说明，外加格式规范：

- [Agent Skills 开放标准](https://agentskills.io/home)
- [格式规范](https://agentskills.io/specification)
- [Claude：Agent Skills 概览](https://platform.claude.com/docs/zh-CN/agents-and-tools/agent-skills/overview)
- [OpenAI Academy：Using skills](https://openai.com/academy/skills/)
- [Cursor：Agent Skills](https://cursor.com/docs/skills)

建议时长 **50 分钟讲解 + 10 分钟练习**。听众用过对话式 agent，没写过 skill。前 20 分钟是定义、简单、复杂，在第 3–5 页。对照演示在第 8 页。平台差异不投影。

第二期材料在 [plugin/](plugin/README.md)。建议另开 **45 分钟**，听众已经听过第一期，或至少写过一份 `SKILL.md`。

## 怎么用

| 文件 | 用途 |
| --- | --- |
| [01-大纲.md](01-大纲.md) | 时间盒、段落目标、可删内容 |
| [02-幻灯提纲.md](02-幻灯提纲.md) | 投影页。每页只有听众该看见的句子 |
| [03-讲稿.md](03-讲稿.md) | 口播。页码与幻灯提纲对齐 |
| [04-一页纸.md](04-一页纸.md) | 会后带走。定义、分工、怎样算照做了 |
| [05-平台对照.md](05-平台对照.md) | 备查。标准、Claude、ChatGPT、Cursor 的落地差异。主线不投影 |
| [06-写作清单.md](06-写作清单.md) | 备查。description、篇幅、自由度、反例。主线不投影 |
| [07-现场练习.md](07-现场练习.md) | 主持人对照演示，以及最后 10 分钟练习 |
| [examples/](examples/) | 简单：`pr-description/` 只有 `SKILL.md`。复杂：`commit-digest/` 带脚本和参考 |

准备顺序：先读大纲和幻灯提纲，再把讲稿过一遍。平台对照和写作清单不投影，被问到再翻。

## 示例

`examples/` 放在本目录下，**不会被 Cursor 自动发现**。Cursor 只从 `.cursor/skills/`、`.agents/skills/` 以及用户目录 `~/.cursor/skills/`、`~/.agents/skills/` 加载。

现场若要演示自动触发，把其中一个示例复制到项目的 `.cursor/skills/` 再开一轮对话。只投影文件内容时，留在 `examples/` 即可。

| 示例 | 演示什么 |
| --- | --- |
| `examples/pr-description/` | 简单。目录里只有 `SKILL.md`，投影第 4 页与文件相同 |
| `examples/commit-digest/` | 复杂。说明书点名 `scripts/` 和 `references/` |
| [plugin/](plugin/README.md) | 第二期。Plugin 的基础、进阶、高级使用 |
| `examples/plugins/` | 三个插件包，分别对应三档使用 |

## 建议议程

| 时间 | 幻灯 | 内容 |
| --- | --- | --- |
| 0:00–5:00 | 1–2 | 反复粘贴的 PR 要求，存成文件 |
| 5:00–18:00 | 3–5 | 定义、简单的文件夹、复杂的文件夹 |
| 18:00–24:00 | 6 | description 决定打不打开 |
| 24:00–32:00 | 7 | 说明书不负责的事 |
| 32:00–42:00 | 8 | 有无 skill 的对照 |
| 42:00–50:00 | 9–12 | 何时读入、写作、放哪、安装 |
| 50:00–60:00 | 13–14 | 练习与带走 |

超时就删第 10–12 页，练习改成课后作业。第 3–5 页和第 8 页留下。
