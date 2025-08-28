from datetime import datetime


class Post:
    def __init__(self, post_id, title, content, author):
        self.post_id = post_id
        self.title = title
        self.content = content
        self.author = author
        self.created_at = datetime.now()
        self.comments = []  # List to store comments for this post

    def __str__(self):
        return f"Post ID: {self.post_id}\nTitle: {self.title}\nAuthor: {self.author}\nContent: {self.content}\nCreated: {self.created_at.strftime('%Y-%m-%d %H:%M')}"

    def add_comment(self, comment):
        self.comments.append(comment)

    def get_comments(self):
        return self.comments
