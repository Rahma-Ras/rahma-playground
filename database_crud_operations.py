from database import DatabaseManager
from models.post import Post
from models.comment import Comment
from datetime import datetime


class DatabasePostCRUD:
    def __init__(self):
        self.db = DatabaseManager()

    # CREATE operations
    def create_post(self, title, content, author):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO posts (title, content, author) VALUES (?, ?, ?)",
            (title, content, author)
        )

        post_id = cursor.lastrowid
        conn.commit()
        conn.close()

        print(f"Post created successfully! ID: {post_id}")
        return post_id

    def create_comment(self, post_id, content, author):
        # First check if post exists
        if not self._post_exists(post_id):
            print("Post not found!")
            return None

        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO comments (post_id, content, author) VALUES (?, ?, ?)",
            (post_id, content, author)
        )

        comment_id = cursor.lastrowid
        conn.commit()
        conn.close()

        print(f"Comment added successfully! ID: {comment_id}")
        return comment_id

    # READ operations
    def read_all_posts(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM posts ORDER BY created_at DESC")
        rows = cursor.fetchall()
        conn.close()

        if not rows:
            print("No posts found!")
            return []

        print("All Posts:")
        print("-" * 50)
        for row in rows:
            print(f"Post ID: {row[0]}")
            print(f"Title: {row[1]}")
            print(f"Author: {row[3]}")
            print(f"Content: {row[2]}")
            print(f"Created: {row[4]}")
            print("-" * 50)

        return rows

    def read_post(self, post_id):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        # Get post
        cursor.execute("SELECT * FROM posts WHERE post_id = ?", (post_id,))
        post = cursor.fetchone()

        if not post:
            print("Post not found!")
            conn.close()
            return None

        # Get comments for this post
        cursor.execute("SELECT * FROM comments WHERE post_id = ? ORDER BY created_at", (post_id,))
        comments = cursor.fetchall()
        conn.close()

        print("Post Details:")
        print("-" * 30)
        print(f"Post ID: {post[0]}")
        print(f"Title: {post[1]}")
        print(f"Author: {post[3]}")
        print(f"Content: {post[2]}")
        print(f"Created: {post[4]}")

        if comments:
            print(f"\nComments ({len(comments)}):")
            print("-" * 30)
            for comment in comments:
                print(f"Comment ID: {comment[0]}")
                print(f"Author: {comment[3]}")
                print(f"Content: {comment[2]}")
                print(f"Created: {comment[4]}")
                print("-" * 20)
        else:
            print("\nNo comments yet.")

        return post, comments

    # UPDATE operations
    def update_post(self, post_id, title=None, content=None):
        if not self._post_exists(post_id):
            print("Post not found!")
            return False

        conn = self.db.get_connection()
        cursor = conn.cursor()

        if title and content:
            cursor.execute(
                "UPDATE posts SET title = ?, content = ? WHERE post_id = ?",
                (title, content, post_id)
            )
        elif title:
            cursor.execute(
                "UPDATE posts SET title = ? WHERE post_id = ?",
                (title, post_id)
            )
        elif content:
            cursor.execute(
                "UPDATE posts SET content = ? WHERE post_id = ?",
                (content, post_id)
            )

        conn.commit()
        conn.close()
        print("Post updated successfully!")
        return True

    def update_comment(self, comment_id, content):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE comments SET content = ? WHERE comment_id = ?",
            (content, comment_id)
        )

        if cursor.rowcount == 0:
            print("Comment not found!")
            conn.close()
            return False

        conn.commit()
        conn.close()
        print("Comment updated successfully!")
        return True

    # DELETE operations
    def delete_post(self, post_id):
        if not self._post_exists(post_id):
            print("Post not found!")
            return False

        conn = self.db.get_connection()
        cursor = conn.cursor()

        # Delete comments first
        cursor.execute("DELETE FROM comments WHERE post_id = ?", (post_id,))

        # Delete post
        cursor.execute("DELETE FROM posts WHERE post_id = ?", (post_id,))

        conn.commit()
        conn.close()
        print("Post and its comments deleted successfully!")
        return True

    def delete_comment(self, comment_id):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM comments WHERE comment_id = ?", (comment_id,))

        if cursor.rowcount == 0:
            print("Comment not found!")
            conn.close()
            return False

        conn.commit()
        conn.close()
        print("Comment deleted successfully!")
        return True

    # Helper method
    def _post_exists(self, post_id):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM posts WHERE post_id = ?", (post_id,))
        exists = cursor.fetchone() is not None
        conn.close()
        return exists