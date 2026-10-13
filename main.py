import github
import env

ACCESS_TOKEN = env.ACCESS_TOKEN
ghub = github.Github(ACCESS_TOKEN)

repo = ghub.get_repo(f"{env.REPO_AUTHOR}/{env.REPO_NAME}")
commits = repo.get_commits()

try:
    commit_count = commits.totalCount
except Exception:
    commit_count = 0
    print("Conversation is empty")

def create_message(author, message):
    global commit_count

    try:
        repo.create_file(
            path=f"{commit_count}.txt",
            message=f"{author}\n{message}",
            content="hmm"
        )

        commit_count += 1
    except github.GithubException as error:
        print(f"{error}")

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
while True:
    for commit in reversed(commits):
        message_metadata = commit.commit.message
        author = message_metadata.split("\n")[0]
        message = message_metadata.split("\n")[-1]

        print(f"{author}: {message}")
    print("\n")

    author = input("Who is writing this?\n>")
    message = input("Message:\n>")

    create_message(author, message)