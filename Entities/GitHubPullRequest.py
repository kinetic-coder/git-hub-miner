from Libraries.utilities import *
from Repositories.GitHubPullRequestRepository import *
import pyodbc

class GitHubPullRequest:
    def __init__(self, id, title, body, user, created_at, updated_at):
        self.id = id
        self.title = title
        self.user = user
        self.created_at = created_at
        self.updated_at = updated_at
        self.body = body

    def savePullRequests(pullRequests):
        
        connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};' + \
                                    'SERVER='+ get_environment_variable('DATABASE_SERVER') + ";" + \
                                    'DATABASE='+ get_environment_variable('DATABASE_NAME') +";" + \
                                    'UID='+ get_environment_variable('DATABASE_USERNAME') + ";" + \
                                    'PWD='+ get_environment_variable('DATABASE_PASSWORD') + ";"
        
        print(connectionString)

        dbConnection = pyodbc.connect(connectionString)

        for pr in pullRequests:
            db_repo = GitHubPullRequestRepository(dbConnection)
            # print(f"{pr.id}, {pr.title}, {pr.user.login}, {pr.created_at}, {pr.updated_at}, {pr.body,}")T