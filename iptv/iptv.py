import os
import requests
import sys

def run_github_workflow():
    # 获取环境变量
    token = os.getenv('TOKEN')
    print(f"token={token}")
    owner = os.getenv('OWNER')
    print(f"owner={owner}")
    repo = os.getenv('REPO')
    print(f"repo={repo}")
    workflow_id = os.getenv('WORKFLOW_ID')
    print(f"workflow_id={workflow_id}")
    ref = os.getenv('REF', 'main')
    print(f"ref={ref}")

    # 验证必要参数
    if not all([token, owner, repo, workflow_id]):
        print("::error::Missing required parameters (TOKEN, OWNER, REPO, WORKFLOW_ID)")
        sys.exit(1)

    # API 配置
    api_url = f"https://api.github.com/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches"

    # 请求头
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2026-03-10"
    }

    # 请求体
    payload = {"ref": ref}

    print("正在准备触发工作流...")
    print(f"API地址：{api_url}")

    try:
        # 发送触发请求
        response = requests.post(
            api_url,
            headers=headers,
            json=payload,
            timeout=10
        )

        # 处理响应
        if response.status_code == 200:
            print(f"✅ 工作流触发成功： {owner}/{repo}:{workflow_id} on {ref}")
        else:
            print(f"\n❌ 请求失败 (HTTP {response.status_code}): {response.text}")
            sys.exit(1)

    except requests.exceptions.RequestException as e:
        print(f"::error::Network error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    run_github_workflow()