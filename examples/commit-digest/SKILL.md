---
name: commit-digest
description: 根据最近的 git 提交起草发布说明。用户提到发布说明、changelog、release note 或最近提交时使用。
compatibility: 需要 git，并且当前目录位于目标仓库内。
---

# 发布说明

## 步骤

1. 运行本 skill 根目录下的 `scripts/collect_commits.sh`。这个路径相对 `SKILL.md` 所在目录，不是目标仓库里的文件。skill 装在用户目录或 `.agents/skills/` 时，目标仓库根目录通常没有这份脚本。先定位 skill 根目录，再用那个路径执行。

   工作目录设在目标 git 仓库内的任意一层，不必是仓库根。需要更长范围时把条数作为参数，例如 `20`。不要自己另写一条 `git log`。

2. 当前工作目录不在 git 仓库内，或脚本失败时，把脚本的错误原样告诉用户并停止。不要根据记忆编造提交。

3. 按本 skill 内的 [references/format.md](references/format.md) 把脚本输出改写成发布说明。

4. 每条说明对应用户能感知的变化。纯格式化、依赖锁定文件更新，合并进「其他」并各写一行。

## 完成前

- 说明里的每条都能在脚本输出里找到对应提交
- 没有加入脚本输出里不存在的功能
- 标题用了 format 文件规定的四个段落
