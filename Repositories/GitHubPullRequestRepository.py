class GitHubPullRequestRepository:
    def __init__(self, dbConnection):
        self.conn = dbConnection

    def save_pull_request(self, pr):
        cursor = self.conn.cursor()
        cursor.execute("""
            exec SaveGitPullRequesSummary(?,?,?,?,?,?)
        """, (pr.id, pr.title, "?", pr.created_at, 1, pr.user.login))
        self.conn.commit()