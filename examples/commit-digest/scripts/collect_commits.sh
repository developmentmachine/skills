#!/usr/bin/env bash
# 打印最近若干条提交，供 commit-digest 示例使用。
# 用法：<skill 根目录>/scripts/collect_commits.sh [条数]
# 脚本路径相对 skill 根目录。工作目录只要在目标 git 仓库内，不必是仓库根。
set -euo pipefail

count="${1:-10}"

if ! [[ "$count" =~ ^[1-9][0-9]*$ ]]; then
  echo "条数必须是正整数，收到：${count}" >&2
  exit 2
fi

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "当前目录不是 git 仓库，无法收集提交。" >&2
  exit 1
fi

git log -n "$count" --pretty=format:'%h%x09%ad%x09%s' --date=short
echo
