import sqlite3


class DatabaseManager:
    def __init__(self, db_name="blog_app.db"):
        self.db_name = db_name
        print(f"Initializing database: {db_name}")
        self.init_database()

    def get_connection(self):
        return sqlite3.connect(self.db_name)

    def init_database(self):
        print("Creating database connection...")
        conn = self.get_connection()
        cursor = conn.cursor()

        print("Creating posts table...")
        posts_sql = "CREATE TABLE IF NOT EXISTS posts (post_id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, content TEXT NOT NULL, author TEXT NOT NULL, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
        cursor.execute(posts_sql)

        print("Creating comments table...")
        comments_sql = "CREATE TABLE IF NOT EXISTS comments (comment_id INTEGER PRIMARY KEY AUTOINCREMENT, post_id INTEGER NOT NULL, content TEXT NOT NULL, author TEXT NOT NULL, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (post_id) REFERENCES posts (post_id))"
        cursor.execute(comments_sql)

        print("Committing changes...")
        conn.commit()
        conn.close()
        print("Database initialized successfully!")


# Test the database creation
if __name__ == "__main__":
    print("Testing database setup...")
    db = DatabaseManager()
    print("Test completed.")