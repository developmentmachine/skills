# Issue：间隔一次请求后，重复提交仍会被接受

## 现象

`SubmissionGuard` 用 `request_id` 防止客户端重复提交。

连续发送两次相同 ID 时，第二次会被拒绝。但按下面的顺序发送时，第三次被错误地接受：

```text
request-a → request-b → request-a
```

## 预期

在同一个 `SubmissionGuard` 实例的生命周期内：

- 第一次出现的非空 `request_id` 返回 `True`
- 已经接受过的 `request_id` 再次出现时返回 `False`

## 范围

- 保持 `SubmissionGuard.accept(request_id)` 的公开接口不变
- 不增加第三方依赖
- 不处理多进程共享、持久化和过期淘汰
