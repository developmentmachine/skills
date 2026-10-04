# com.example.client

这个目录只给认 `com.example.client` 这个名空间的客户端读。

其他客户端忽略整个目录，也忽略 `plugin.json` 里同名的 `extensions` 对象，然后继续加载 `skills/` 和 `mcp.json`。

钩子、自定义界面、只对一个产品有意义的开关，放在这种目录里。它们不是 Agent Plugins 1.0.0 的可移植组件。本目录故意不放可执行钩子。
