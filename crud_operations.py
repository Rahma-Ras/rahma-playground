from models.post import Post
from models.comment import Comment

class PostCRUD:
    def __init__(self):
        self.posts = {}
        self.comments = {}
        self.next_post_id = 1
        self.next_comment_id = 1

        # CREATE operations

    def create_post(self, title, content, author):
        post = Post(self.next_post_id, title, content, author)
        self.posts[self.next_post_id] = post
        self.next_post_id += 1
        print(f"✅ Post created successfully! ID: {post.post_id}")
        return post

    def create_comment(self, post_id, content, author):
        if post_id not in self.posts:
            print("❌ Post not found!")
            return None

        comment = Comment(self.next_comment_id, post_id, content, author)
        self.comments[self.next_comment_id] = comment
        self.posts[post_id].add_comment(comment)
        self.next_comment_id += 1
        print(f"✅ Comment added successfully! ID: {comment.comment_id}")
        return comment

        # READ operations

    def read_all_posts(self):
        if not self.posts:
            print("📭 No posts found!")
            return []

        print("📚 All Posts:")
        print("-" * 50)
        for post in self.posts.values():
            print(post)
            print("-" * 50)
        return list(self.posts.values())

    def read_post(self, post_id):
        if post_id not in self.posts:
            print("❌ Post not found!")
            return None

        post = self.posts[post_id]
        print("📖 Post Details:")
        print("-" * 30)
        print(post)

        if post.comments:
            print(f"\n💬 Comments ({len(post.comments)}):")
            print("-" * 30)
            for comment in post.comments:
                print(comment)
                print("-" * 20)
        else:
            print("\n💬 No comments yet.")

        return post

        # UPDATE operations

    def update_post(self, post_id, title=None, content=None):
        if post_id not in self.posts:
            print("❌ Post not found!")
            return None

        post = self.posts[post_id]
        if title:
            post.title = title
        if content:
            post.content = content

        print("✅ Post updated successfully!")
        return post

    def update_comment(self, comment_id, content=None):
        if comment_id not in self.comments:
            print("❌ Comment not found!")
            return None

        comment = self.comments[comment_id]
        if content:
            comment.content = content

        print("✅ Comment updated successfully!")
        return comment

        # DELETE operations

    def delete_post(self, post_id):
        if post_id not in self.posts:
            print("❌ Post not found!")
            return False

        # Also delete all comments for this post
        post = self.posts[post_id]
        for comment in post.comments:
            del self.comments[comment.comment_id]

        del self.posts[post_id]
        print("🗑️ Post and its comments deleted successfully!")
        return True

    def delete_comment(self, comment_id):
        if comment_id not in self.comments:
            print("❌ Comment not found!")
            return False

        comment = self.comments[comment_id]
        post = self.posts[comment.post_id]
        post.comments = [c for c in post.comments if c.comment_id != comment_id]

        del self.comments[comment_id]
        print("🗑️ Comment deleted successfully!")
        return True
