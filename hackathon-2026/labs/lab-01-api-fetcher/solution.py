import requests

def fetch_issues(owner: str, repo: str) -> list:
    url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=open"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return []

def filter_open(issues: list) -> list:
    return [issue for issue in issues if issue.get("state") == "open"]
```

Just make sure it's placed at:
```
labs/
└── lab-01-api-fetcher/
    └── solution.py  ✅ ← already correct, just push it
