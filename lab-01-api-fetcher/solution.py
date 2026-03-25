import requests

def fetch_issues(owner: str, repo: str) -> list:
    """Fetch open issues from a GitHub repository."""
    url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=open"
    # Note: requests is imported at module level for simplicity in labs
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json()
    except Exception:
        pass
    return []


def filter_open(issues: list) -> list:
    """Filter a list of issues to only include those where state is 'open'."""
    return [i for i in issues if i.get("state") == "open"]
