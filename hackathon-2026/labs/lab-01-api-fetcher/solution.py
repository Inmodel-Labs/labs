import requests


def fetch_issues(owner: str, repo: str) -> list:
    """Fetch open issues from a GitHub repository."""
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    try:
        response = requests.get(url, timeout=10)
    except requests.exceptions.Timeout:
        return []
    except requests.exceptions.RequestException:
        return []

    if response.status_code == 200:
        return response.json()
    return []


def filter_open(issues: list) -> list:
    """Filter a list of issues to keep only "open" ones."""
    return [issue for issue in issues if issue.get("state") == "open"]
