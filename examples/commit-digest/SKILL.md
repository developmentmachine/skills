---
name: commit-digest
description: 根据最近的 git 提交起草发布说明。用户提到发布说明、changelog、release note 或最近提交时使用。
compatibility: 需要 git，并且当前目录位于目标仓库内。
---

# 发布说明

## 步骤

1. 在目标仓库根目录运行：

   ```bash
   scripts/collect_commits.sh
   ```

   需要更长范围时传入条数，例如 `scripts/collect_commits.sh 20`。不要自己另写一条 `git log`。

2. 当前目录不是 git 仓库，或脚本失败时，把脚本的错误原样告诉用户并停止。不要根据记忆编造提交。

3. 按 [references/format.md](references/format.md) 把脚本输出改写成发布说明。

4. 每条说明对应用户能感知的变化。纯格式化、依赖锁定文件更新，合并进「其他」并各写一行。

## 完成前

- 说明里的每条都能在脚本输出里找到对应提交
- 没有加入脚本输出里不存在的功能
- 标题用了 format 文件规定的四个段落
