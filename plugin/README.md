# Plugin 分享素材

第二期。讲 Agent Plugin：带标准根 manifest 的自包含目录，可携带 skill、MCP 配置和客户端扩展。组件可以没有；需要交付实际能力时，再加入对应的 skill 或服务。

本讲统一使用标准根 `plugin.json`，OpenAI 展示信息写入 `extensions.com.openai`，不教第二套兼容布局。

听众离开时要能判断三件事：这份东西该停在单个 skill，还是要打成插件；插件里 skill 和 MCP 各写什么；哪些能力属于可移植包，哪些只属于某一个客户端。

Skill、MCP、memory 的边界在第一期第 7 页。这期默认已经讲过。没听过的房间，先投那一页。

## 依据

- [Agent Plugins 规范 1.0.0](https://agent-plugins.org/specification)
- [ChatGPT：Skills & Plugins](https://learn.chatgpt.com/docs/skills-and-plugins)
- [ChatGPT：Plugins 的安装与使用](https://learn.chatgpt.com/docs/plugins)
- [OpenAI：插件里的 Skills](https://developers.openai.com/plugins/concepts/skills)
- [OpenAI：打包插件](https://developers.openai.com/plugins/build/plugins)
- [Google：Agent Plugins 说明](https://developers.googleblog.com/agent-plugins-package-your-skills-tools-and-more/)

规范规定包结构、组件发现、加载和失败边界。安装按钮、市场、权限和沙箱由各客户端自己做。本讲的「使用」以 ChatGPT 与 Codex 已经公开的装法和调用法为例，包格式以规范为准。

## 怎么用

| 文件 | 用途 |
| --- | --- |
| [01-大纲.md](01-大纲.md) | 三档时间盒、每档结束时听众能做什么 |
| [02-幻灯提纲.md](02-幻灯提纲.md) | 20 页。第 1–7 页基础，第 8–13 页进阶，第 14–20 页高级 |
| [03-讲稿.md](03-讲稿.md) | 口播，页码与幻灯对齐 |
| [04-一页纸.md](04-一页纸.md) | 会后带走。三档各一段 |
| [05-规范备查.md](05-规范备查.md) | 不投影。名字、版本、路径、传输、失败边界、扩展名空间 |
| [../examples/plugins/](../examples/plugins/) | 三个可打开的包 |

准备顺序与第一期相同：大纲 → 幻灯 → 讲稿。被问到字段约束时翻规范备查。

## 三档示例

这些目录不会被 Cursor 当成 skill 自动加载。现场用它们讲目录。

`hello-plugin` 是最小 Skill 插件示例：一份 `plugin.json` 加一份 skill，没有 MCP。只包含合法 `plugin.json`、没有任何组件的目录也符合格式，但不提供任务能力；只带 MCP 的插件同样合法。

`status-pack` 和 `reports-plugin` 是结构演示，不能拿来证明安装后能取到数据。`status-pack` 的 `bin/activity` 会故意退出，用来演示「MCP 连不上时，skill 仍然保留」。`reports-plugin` 的 `bin/validate` 同样会故意失败；`https://mcp.example.com/mcp` 不是这门课的服务。

| 档 | 目录 | 使用场景 |
| --- | --- | --- |
| 基础 | `examples/plugins/01-basic/hello-plugin/` | 一份 skill 需要被安装、分享时，最小 Skill 插件示例 |
| 进阶 | `examples/plugins/02-intermediate/status-pack/` | 多份 skill 配一个 MCP 入口，流程和工具分开 |
| 高级 | `examples/plugins/03-advanced/reports-plugin/` | 版本与元数据、两种传输、客户端扩展目录 |

## 建议议程

| 时间 | 幻灯 | 档 |
| --- | --- | --- |
| 0:00–12:00 | 1–7 | 基础：何时打包、最小目录、装上之后怎么点 |
| 12:00–28:00 | 8–13 | 进阶：多 skill、MCP、路径变量、失败隔离 |
| 28:00–43:00 | 14–19 | 高级：扩展名空间、钩子、分发、版本与密钥 |
| 43:00–45:00 | 20 | 三句带走 |

时间紧时删第 16–17 页，高级只留扩展名空间和「规范不管安装」。
