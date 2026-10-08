# 三档插件示例

现场打开目录即可。`hello-plugin` 是最小 Skill 插件示例。仅有合法 manifest 的空包也符合格式，但不提供任务能力。`status-pack` 和 `reports-plugin` 不必安装，也不能当成已经联调的插件。

| 目录 | 档 | 看什么 |
| --- | --- | --- |
| `01-basic/hello-plugin/` | 基础 | 标准根 `plugin.json` + 一份 skill |
| `02-intermediate/status-pack/` | 进阶 | 两份 skill、一份 `mcp.json`、失败的占位进程 |
| `03-advanced/reports-plugin/` | 高级 | 元数据、两种传输声明、反向域名扩展 |

`status-pack` 的 `bin/activity` 和 `reports-plugin` 的 `bin/validate` 会马上退出，避免被当成真正的 MCP 服务。符合规范的客户端应跳过失败的服务，并继续发现 `skills/`。`reports-plugin` 里的 `https://mcp.example.com/mcp` 是占位地址，不是这门课的服务。安装这两个目录都不会得到活动数据或指标。
