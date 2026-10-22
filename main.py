import requests

from github_api import get_user, get_repositories
from analyzer import (
    get_language_statistics,
    get_repository_statistics,
    get_most_popular_repository,
)
from utils import (
    print_header,
    print_section,
    print_profile,
    print_repositories,
    print_language_statistics,
    print_repository_statistics,
    print_error,
)


def analyze_profile(username):
    """Fetch and display a GitHub profile and repository statistics."""
    user = get_user(username)
    if user is None:
        print_error("GitHub user not found. Check the username and try again.")
        return

    print_section("PROFILE")
    print_profile(user)

    repositories = get_repositories(username)
    if repositories is None:
        print_error("Could not retrieve repositories for this username.")
        return

    print_section("REPOSITORIES")
    print_repositories(repositories)

    print_section("LANGUAGE STATISTICS")
    print_language_statistics(get_language_statistics(repositories))

    print_section("REPOSITORY STATISTICS")
    print_repository_statistics(get_repository_statistics(repositories))

    print_section("MOST POPULAR REPOSITORY")
    popular_repo = get_most_popular_repository(repositories)
    if popular_repo:
        print(f"Name  : {popular_repo['name']}")
        print(f"Stars : {popular_repo['stars']}")
    else:
        print("No repositories found.")


def main():
    """Program entry point."""
    print_header()
    username = input("Enter GitHub username: ").strip().lstrip("@")
    if not username:
        print_error("Username cannot be empty.")
        return

    print(f"\nAnalyzing GitHub user: {username}\n")
    try:
        analyze_profile(username)
    except requests.Timeout:
        print_error("The request timed out. Check your internet and try again.")
    except requests.ConnectionError:
        print_error("Could not connect to GitHub. Check your internet connection.")
    except requests.HTTPError as error:
        status = error.response.status_code if error.response is not None else "unknown"
        print_error(f"GitHub API request failed (HTTP {status}): {error}")
    except requests.RequestException as error:
        print_error(f"Network request failed: {error}")
    except (ValueError, TypeError) as error:
        print_error(f"Unexpected API response: {error}")


if __name__ == "__main__":
    main()
