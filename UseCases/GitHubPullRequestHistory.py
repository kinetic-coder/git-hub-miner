import logging

from github import Github
from Entities.GitHubPullRequest import *
from Libraries.utilities import *
from Repositories.FileRepository import *

class GitHubUseCases:

    def get_github_pull_requests(self):
        logging.basicConfig(level=logging.INFO)

        secret_filename = "/home/oliverbullock/Documents/secrets.txt"
        repo_filename = "/home/oliverbullock/Documents/repos.txt"

        # get the token from a secret file.
        file = FileRepository(secret_filename)
        pak = file.read_lines()[0].strip()

        # First create a Github instance using an access token
        g = Github(pak)

        # Then get the specific repository
        file = FileRepository(repo_filename)
        repos = file.read_lines()

        #create a new pull request collection
        pull_requests = []

        repository_index = 0;
        repository_total = len(repos)

        for repo in repos:
            repo = g.get_repo(repo)
            logging.info(f" Getting [all] pull requests from repo {repo.name} [{repository_index}/{repository_total}]")
            pulls = repo.get_pulls(state='all')

            logging.info(f" Creating GitHubPullRequest objects for repo {repo.name} [{repository_index}/{repository_total}]")
            for pr in pulls:
                jira_reference = parse_string_with_regex(pr.title, r"SBS-\d+")
                pull_request = GitHubPullRequest(pr.id, pr.title, pr.body, pr.user, pr.created_at, pr.updated_at, repo.name, jira_reference)
                pull_requests.append(pull_request)

            repository_index += 1
            
        output_filename = "/home/oliverbullock/Documents/pull_requests.csv"

        logging.info(f" Writing pull requests to file [{output_filename}]...")

        write_pull_requests_to_file(pull_requests, output_filename)

        logging.info(f" Exported required git hub information to {output_filename}!")
        input("Press enter to continue...")
