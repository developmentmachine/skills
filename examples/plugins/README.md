# 三档插件示例

现场打开目录即可，不必安装。

| 目录 | 档 | 看什么 |
| --- | --- | --- |
| `01-basic/hello-plugin/` | 基础 | 最小 `plugin.json` + 一份 skill |
| `02-intermediate/status-pack/` | 进阶 | 两份 skill、一份 `mcp.json`、失败的占位进程 |
| `03-advanced/reports-plugin/` | 高级 | 元数据、两种传输、反向域名扩展 |

`bin/` 里的进程会马上退出，避免被当成真正的 MCP 服务。符合规范的客户端应跳过这条服务，并继续发现 `skills/`。
