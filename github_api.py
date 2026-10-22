"""Helpers for reading public GitHub data through the REST API.

Set GITHUB_TOKEN in your environment to use authenticated requests and
increase the API rate limit. A token is optional for public profiles.
"""
import os

import requests

BASE_URL = "https://api.github.com"
TIMEOUT = 10


def _headers():
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def _get(url, params=None):
    """Send a GET request and raise a helpful error for API failures."""
    response = requests.get(
        url,
        headers=_headers(),
        params=params,
        timeout=TIMEOUT,
    )
    if response.status_code == 404:
        return None
    if response.status_code == 401:
        raise requests.HTTPError(
            "GitHub rejected the token. Check GITHUB_TOKEN.", response=response
        )
    if response.status_code in (403, 429):
        remaining = response.headers.get("X-RateLimit-Remaining")
        if remaining == "0" or response.status_code == 429:
            raise requests.HTTPError(
                "GitHub API rate limit reached. Set GITHUB_TOKEN or try later.",
                response=response,
            )
    response.raise_for_status()
    return response.json()


def get_user(username):
    """Return public profile data, or None if the username does not exist."""
    return _get(f"{BASE_URL}/users/{username}")


def get_repositories(username):
    """Return all public repositories, requesting up to 100 per page."""
    url = f"{BASE_URL}/users/{username}/repos"
    repositories = []
    page = 1

    while True:
        batch = _get(
            url,
            params={"per_page": 100, "sort": "updated", "page": page},
        )
        if batch is None:
            return None
        repositories.extend(batch)
        if len(batch) < 100:
            return repositories
        page += 1
