
# Manual GitHub Action Trigger

这是一个GitHub Action，允许您从另一个工作流中手动触发指定的工作流。

## 使用方法

在您的工作流YAML文件中添加此Action：

```yaml
- name: Trigger Another Workflow
  uses: your-username/github-action-trigger@main
  with:
    token: ${{ secrets.PERSONAL_ACCESS_TOKEN }}
    owner: 'target-owner'
    repo: 'target-repo'
    workflow_id: 'workflow-file.yml'
    ref: 'main'
    inputs: '{"key": "value"}'
```

## 参数说明

- `token`: GitHub个人访问令牌（必需）
- `owner`: 目标仓库的所有者（必需）
- `repo`: 目标仓库名称（必需）
- `workflow_id`: 工作流ID或文件名（必需）
- `ref`: 触发工作流的分支或标签（可选，默认为main）
- `inputs`: 工作流输入参数的JSON字符串（可选）

## 权限要求

确保您的个人访问令牌具有`repo`权限和`workflow`权限。
