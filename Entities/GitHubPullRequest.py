from Libraries.utilities import *
from Repositories.GitHubPullRequestRepository import *

class GitHubPullRequest:
    def __init__(self, id, title, body, user, created_at, updated_at, repo_name):
        self.id = id
        self.title = title
        self.user = user
        self.created_at = created_at
        self.updated_at = updated_at
        self.body = body
        self.repo_name = repo_name