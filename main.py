from github_api import get_user, get_repositories
from analyzer import (
    get_language_statistics,
    get_repository_statistics,
    get_most_popular_repository
)
from utils import (
    print_header,
    print_section,
    print_profile,
    print_repositories,
    print_language_statistics,
    print_repository_statistics,
    print_error
)


def analyze_profile(username):
    """Get and display GitHub profile information."""

    try:
        user = get_user(username)

        if user is None:
            print_error("GitHub user not found.")
            return

        print_section("PROFILE")
        print_profile(user)

        repositories = get_repositories(username)

        if repositories is None:
            print_error("Could not retrieve repositories.")
            return

        print_section("REPOSITORIES")
        print_repositories(repositories)

        print_section("LANGUAGE STATISTICS")
        language_stats = get_language_statistics(repositories)
        print_language_statistics(language_stats)

        print_section("REPOSITORY STATISTICS")
        statistics = get_repository_statistics(repositories)
        print_repository_statistics(statistics)

        print_section("MOST POPULAR REPOSITORY")

        popular_repo = get_most_popular_repository(repositories)

        if popular_repo:
            print(f"Name  : {popular_repo['name']}")
            print(f"Stars : {popular_repo['stars']}")
        else:
            print("No repositories found.")

    except Exception as error:
        print_error(f"Something went wrong: {error}")


def main():
    """Main program."""

    print_header()

    username = input("Enter GitHub username: ").strip()

    if not username:
        print_error("Username cannot be empty.")
        return

    print()
    print(f"Analyzing GitHub user: {username}")
    print()

    analyze_profile(username)


if __name__ == "__main__":
    main()