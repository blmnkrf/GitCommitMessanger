from github import Github
import env

ACCESS_TOKEN = env.ACCESS_TOKEN
ghub = Github(ACCESS_TOKEN)

repo = ghub.get_repo(f"{env.REPO_AUTHOR}/{env.REPO_NAME}")
commits = repo.get_commits()

for commit in commits:
    print(f"{commit.commit.author.name} ({commit.commit.author.date}): {commit.commit.message.strip()}")