from github import Github
from Entities.GitHubPullRequest import *
from Libraries.utilities import *

# get the token from a secret file.
pak = get_secret("/home/oliverbullock/Documents/secrets.txt")

# First create a Github instance using an access token
g = Github(pak)

# Then get the specific repository
repo_name = get_repos("/home/oliverbullock/Documents/repos.txt")
repo = g.get_repo(repo_name)

# Get all pull requests
pulls = repo.get_pulls()

# Create a new collection of GitHubPullRequest objects
pull_requests = []

for pr in pulls:
    pull_request = GitHubPullRequest(pr.id, pr.title, pr.body, pr.user, pr.created_at, pr.updated_at)
    pull_requests.append(pull_request)

write_pull_requests_to_file(pull_requests, "/home/oliverbullock/Documents/pull_requests.csv")

print("Done!")

