import os
import re

def get_secret(filename):
    with open(filename, 'r') as secret_file:
        secret_file = secret_file.read().strip()
    return secret_file

def write_pull_requests_to_file(pull_requests, filename):
    with open(filename, 'w') as file:
        file.write("id^ repository^ title^ user^ created_at^ updated_at^ jira_reference\n")
        for pr in pull_requests:
            file.write(f"{pr.id}^ {pr.repo_name}^ {pr.title}^ {pr.user.login}^ {pr.created_at}^ {pr.updated_at}^ {pr.jira_reference}^\n")

def get_repos(filename):
    with open(filename, 'r') as repo_file:
        repo_file = repo_file.read().strip()
    return repo_file

def get_environment_variable(variable_name):
    value = str(os.environ.get(variable_name))

def parse_string_with_regex(input_string, regex_pattern):
    match = re.search(regex_pattern, input_string)
    if match:
        return match.group()
    else:
        return None