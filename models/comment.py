from datetime import datetime


class Comment:
    def __init__(self, comment_id, post_id, content, author):
        self.comment_id = comment_id
        self.post_id = post_id
        self.content = content
        self.author = author
        self.created_at = datetime.now()

    def __str__(self):
        return f"Comment ID: {self.comment_id}\nAuthor: {self.author}\nContent: {self.content}\nCreated: {self.created_at.strftime('%Y-%m-%d %H:%M')}"

