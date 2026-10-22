# GitHub Analyzer

A small Python command-line tool that reads public GitHub profile and repository data and summarizes it.

## Features

- Display profile details, followers, and following
- List public repositories
- Count repositories by primary programming language
- Calculate total stars and forks
- Find the most-starred repository
- Fetch more than 100 repositories using pagination
- Handle common network, HTTP, and rate-limit errors
- Optionally use a token from an environment variable

## Requirements

- Python 3.10+
- `requests`

Install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Run

```bash
python main.py
```

Enter a GitHub username when prompted.

## Optional: set a GitHub token

Public profile requests work without a token. A token can increase your API rate limit. Create a token with only the permissions you need; this project only reads public data.

In Ubuntu/Linux, set it for the current terminal session:

```bash
export GITHUB_TOKEN="paste_your_token_here"
python main.py
```

Do not put your token in the source code or commit it to GitHub. The program reads the token from the environment and does not print it.

## Project files

- `main.py` — command-line interface and error handling
- `github_api.py` — GitHub API requests and pagination
- `analyzer.py` — statistics calculations
- `utils.py` — terminal output helpers

## Current limitations

This tool analyzes public user profiles and public repositories. It does not implement OAuth login or access private repositories. Language counts use each repository's primary language reported by GitHub.
