import os
from Libraries.utilities import *

def get_secret(filename):
    with open(filename, 'r') as secret_file:
        secret_file = secret_file.read().strip()
    return secret_file

def write_pull_requests_to_file(pull_requests, filename):
    with open(filename, 'w') as file:
        for pr in pull_requests:
            file.write(f"{pr.id}, {pr.title}, {pr.user.login}, {pr.created_at}, {pr.updated_at}, {pr.body,}\n")

def get_repos(filename):
    with open(filename, 'r') as repo_file:
        repo_file = repo_file.read().strip()
    return repo_file

def get_environment_variable(variable_name):
    value = str(os.environ.get(variable_name))