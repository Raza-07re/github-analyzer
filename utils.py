def print_header():
    print("=" * 45)
    print("           GITHUB ANALYZER")
    print("=" * 45)
    print()


def print_section(title):
    print()
    print("-" * 45)
    print(title)
    print("-" * 45)


def print_profile(user):
    print(f"Username           : {user.get('login', 'N/A')}")
    print(f"Name               : {user.get('name', 'N/A')}")
    print(f"Bio                : {user.get('bio', 'N/A')}")
    print(f"Public Repositories: {user.get('public_repos', 0)}")
    print(f"Followers          : {user.get('followers', 0)}")
    print(f"Following          : {user.get('following', 0)}")
    print(f"Location           : {user.get('location', 'N/A')}")
    print(f"Company            : {user.get('company', 'N/A')}")
    print(f"Created At         : {user.get('created_at', 'N/A')}")


def print_repositories(repositories):
    if not repositories:
        print("No public repositories found.")
        return

    for number, repository in enumerate(repositories, start=1):

        name = repository.get("name", "N/A")
        language = repository.get("language") or "N/A"
        stars = repository.get("stargazers_count", 0)
        forks = repository.get("forks_count", 0)

        print(f"{number}. {name}")
        print(f"   Language : {language}")
        print(f"   Stars    : {stars}")
        print(f"   Forks    : {forks}")
        print()


def print_language_statistics(statistics):
    if not statistics:
        print("No language information available.")
        return

    sorted_languages = sorted(
        statistics.items(),
        key=lambda item: item[1],
        reverse=True
    )

    for language, count in sorted_languages:
        print(f"{language:<20}: {count} repositories")


def print_repository_statistics(statistics):
    print(
        f"Total Repositories : "
        f"{statistics['total_repositories']}"
    )

    print(
        f"Total Stars        : "
        f"{statistics['total_stars']}"
    )

    print(
        f"Total Forks        : "
        f"{statistics['total_forks']}"
    )


def print_error(message):
    print()
    print(f"[ERROR] {message}")