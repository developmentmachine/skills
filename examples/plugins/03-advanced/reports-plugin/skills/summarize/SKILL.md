---
name: summarize
description: 把 metrics-api 返回的指标写成指标摘要。用户提到指标摘要或 reports plugin 时使用。
---

# 指标摘要

## 工具

使用本插件里的 metrics-api 读取指标，使用 local-validator 核对条数是否超过包内限制。不要在对话里粘贴令牌，也不要改 `headers`。

## 步骤

1. 确认周期。没说时先问。
2. 读取指标。服务不可用时停止，并说明哪一个服务失败。
3. 条数超过 `config/limits.json` 的 `max_rows` 时，先截断再摘要，并写明被截断的数量。
4. 按 references/sections.md 的三段输出。

## 完成前

- 数字都能在工具结果里找到
- 写明了周期，以及是否截断
