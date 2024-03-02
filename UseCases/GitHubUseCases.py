import logging

from github import Github
from Entities.GitHubPullRequest import *
from Libraries.utilities import *
from Repositories.FileRepository import *

class GitHubUseCases:

    

    def get_github_token(self):
        secret_filename = "/home/oliverbullock/Documents/secrets.txt"

        # get the token from a secret file.
        file = FileRepository(secret_filename)
        pak = file.read_lines()[0].strip()
        return pak

    def get_github_repositories(self):
        repo_filename = "/home/oliverbullock/Documents/repos.txt"
        file = FileRepository(repo_filename)
        repos = file.read_lines()
        return repos
    
    def write_pr_reviews_to_file(self, pr_reviews, output_filename):
        with open(output_filename, 'w') as f:
            f.write("pull_request_id,review_id,user,state,submitted_at,body\n")
            for review in pr_reviews:
                f.write(f"{review['pull_request_ref']},{review['pull_request_id']},{review['review_id']},{review['user']},{review['state']},{review['submitted_at']},{review['body']}\n")

    def write_pr_reviews_to_file(self, pull_requests, output_filename):
        with open(output_filename, 'w') as f:
            f.write("id,title,body,user,created_at,updated_at,repository,jira_reference\n")
            for pr in pull_requests:
                f.write(f"{pr.id},{pr.title},{pr.body},{pr.user},{pr.created_at},{pr.updated_at},{pr.repository},{pr.jira_reference}\n")

    def get_github_pull_requests(self):

        logging.basicConfig(level=logging.INFO)

        pak = self.get_github_token()

        # First create a Github instance using an access token
        g = Github(pak)

        repositorys = self.get_github_repositories()

        #create a new pull request collection
        pull_requests = []

        repository_index = 0
        repository_total = len(repositorys)

        for repository in repositorys:
            gh_repo = g.get_repo(repository)
            logging.info(f" Getting [all] pull requests from repo {gh_repo.name} [{repository_index}/{repository_total}]")
            pulls = gh_repo.get_pulls(state='all')

            logging.info(f" Creating GitHubPullRequest objects for repo {gh_repo.name} [{repository_index}/{repository_total}]")
            for pr in pulls:
                jira_reference = parse_string_with_regex(pr.title, r"SBS-\d+")
                pull_request = GitHubPullRequest(pr.id, pr.title, pr.body, pr.user, pr.created_at, pr.updated_at, gh_repo.name, jira_reference)
                pull_requests.append(pull_request)

            repository_index += 1
            
        output_filename = "/home/oliverbullock/Documents/pull_requests.csv"

        logging.info(f" Writing pull requests to file [{output_filename}]...")

        write_pull_requests_to_file(pull_requests, output_filename)

        logging.info(f" Exported required git hub information to {output_filename}!")
        input("Press enter to continue...")

    # get the pull request reviews from Github and write to file
    def get_github_pr_reviews(self):

        logging.basicConfig(level=logging.INFO)
        
        pak = self.get_github_token()

        # First create a Github instance using an access token
        g = Github(pak)

        repos = self.get_github_repositories()

        # create a new pull request review collection
        pr_reviews = []
        repository_index = 0
        repository_total = len(repos)
        for repo_name in repos:
            repo = g.get_repo(repo_name)
            logging.info(f" Getting pull request reviews from repo {repo.name} [{repository_index}/{repository_total}]")
            pulls = repo.get_pulls(state='all')
            for pr in pulls:
                reviews = pr.get_reviews()
                for review in reviews:
                    pr_review = {
                        'pull_request_ref': pr.number,
                        'pull_request_id': pr.id,
                        'review_id': review.id,
                        'user': review.user,
                        'state': review.state,
                        'submitted_at': review.submitted_at,
                        'body': review.body
                    }
                    pr_reviews.append(pr_review)
                    logging.info(f" +{pr_review['pull_request_ref']} in {repo_name} from {pr_review['user']} circa {pr_review['submitted_at']} [{repository_index}/{repository_total}]")
                                 
            repository_index += 1
        
        output_filename = "/home/oliverbullock/Documents/pr_reviews.csv"
        logging.info(f" Writing pull request reviews to file [{output_filename}]...")

        self.write_pr_reviews_to_file(pr_reviews, output_filename)
        
        logging.info(f" Exported pull request reviews to {output_filename}!")
        input("Press enter to continue...")
