# Login Submit Demo

这是「Agent 最佳实践」课程的演示仓库。

要求：

- Python 3
- 不需要安装第三方依赖

运行测试：

```bash
python3 -m unittest discover -s tests -v
```

仓库故意保留了 `issue.md` 描述的问题。主持人应把整个目录复制到临时位置，再让 Agent 在副本中工作。

## 分层规则示例

```text
AGENTS.md             项目级环境、边界和默认验收
src/AGENTS.md         源码目录的实现约束
tests/AGENTS.md       测试目录的约束
CLAUDE.md             Claude Code 兼容入口，引用 @AGENTS.md
.gemini/settings.json 让 Gemini CLI 读取 AGENTS.md
issue.md              当前任务的事实、目标、范围和非目标
instruction-evals.md  规则文件变更后的行为回归案例
```

Codex、Cursor、Hermes 和 GitHub Copilot 可以直接使用项目 `AGENTS.md`，但嵌套文件的发现时机和覆盖方式并不完全相同。Gemini CLI 使用示例中的配置接入。Claude Code v2.1.277 起支持直接读取 `AGENTS.md`，默认是否加载取决于项目中的 Claude 专属规则文件和 `Project instructions` 设置。本示例保留 `CLAUDE.md`，因此默认通过 `@AGENTS.md` 引入根规则；`src/` 和 `tests/` 的目录级规则需另行确认加载，不能从根规则的导入推断它们也已自动加载。

演示前应使用当前产品提供的上下文查看方式确认实际加载结果。不能查看时，让 Agent 明确读取这些文件，并说明这是显式读取，不是假装宿主已经自动加载。

这个示例故意把信息分开：

- 长期稳定的项目要求放规则文件；
- 当前问题放 `issue.md`；
- 实际测试输出、diff 和进度属于运行状态；
- 用户 Prompt 只需启动任务并补充本次变化。

## 规则文件也需要维护

根 `AGENTS.md` 中的 `instructions-owner` 和 `last-reviewed` 是本课程使用的维护约定，不是 `AGENTS.md` 标准字段，也不会自动触发任何行为。版本以 Git 历史为准。

更新规则时：

1. 先记录重复出现且代价明确的问题；
2. 判断它应进入根规则、目录规则、Skill，还是应由测试或权限强制；
3. 做一项最小修改，同时删除冲突、重复或过期内容；
4. 运行 `instruction-evals.md` 中的代表性和冲突案例；
5. 检查各支持产品实际加载的规则链，再评审和提交 diff。

规则文件应该迭代，但不能只增不减。
