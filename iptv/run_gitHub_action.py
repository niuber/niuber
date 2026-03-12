
#!/usr/bin/env python3
import requests
import sys
import json

def trigger_github_workflow(token, owner, repo, workflow_id, ref="main", inputs=None):
    """
    使用GitHub API手动触发一个工作流
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches"
    
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {token}"
    }
    
    payload = {
        "ref": ref
    }
    
    if inputs:
        try:
            parsed_inputs = json.loads(inputs) if isinstance(inputs, str) else inputs
            payload["inputs"] = parsed_inputs
        except json.JSONDecodeError:
            print("Warning: Invalid JSON in inputs, ignoring inputs parameter")
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 204:
        print("工作流已成功触发")
        return True
    else:
        print(f"触发失败: {response.status_code} - {response.text}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python trigger_workflow.py <token> <owner> <repo> <workflow_id> [ref] [inputs]")
        sys.exit(1)
    
    token = sys.argv[1]
    owner = sys.argv[2]
    repo = sys.argv[3]
    workflow_id = sys.argv[4]
    ref = sys.argv[5] if len(sys.argv) > 5 else "main"
    inputs = sys.argv[6] if len(sys.argv) > 6 else "{}"
    
    success = trigger_github_workflow(token, owner, repo, workflow_id, ref, inputs)
    sys.exit(0 if success else 1)
