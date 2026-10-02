import requests


BASE_URL = "https://api.github.com"


def get_user(username):
    """
    Get GitHub user information.
    """

    url = f"{BASE_URL}/users/{username}"

    response = requests.get(url, timeout=10)

    if response.status_code == 404:
        return None

    response.raise_for_status()

    return response.json()


def get_repositories(username):
    """
    Get all public repositories for a GitHub user.
    """

    url = f"{BASE_URL}/users/{username}/repos"

    params = {
        "per_page": 100,
        "sort": "updated"
    }

    response = requests.get(
        url,
        params=params,
        timeout=10
    )

    if response.status_code == 404:
        return None

    response.raise_for_status()

    return response.json()