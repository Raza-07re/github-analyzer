def get_language_statistics(repositories):
    """
    Count how many repositories use each programming language.
    """

    languages = {}

    for repository in repositories:

        language = repository.get("language")

        if language is None:
            continue

        if language in languages:
            languages[language] += 1
        else:
            languages[language] = 1

    return languages


def get_repository_statistics(repositories):
    """
    Calculate general repository statistics.
    """

    total_repositories = len(repositories)

    total_stars = 0
    total_forks = 0

    for repository in repositories:
        total_stars += repository.get("stargazers_count", 0)
        total_forks += repository.get("forks_count", 0)

    return {
        "total_repositories": total_repositories,
        "total_stars": total_stars,
        "total_forks": total_forks
    }


def get_most_popular_repository(repositories):
    """
    Find the repository with the most stars.
    """

    if not repositories:
        return None

    popular_repository = repositories[0]

    for repository in repositories:

        current_stars = repository.get("stargazers_count", 0)
        popular_stars = popular_repository.get(
            "stargazers_count",
            0
        )

        if current_stars > popular_stars:
            popular_repository = repository

    return {
        "name": popular_repository.get("name"),
        "stars": popular_repository.get(
            "stargazers_count",
            0
        )
    }