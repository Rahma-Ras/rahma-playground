from database_crud_operations import DatabasePostCRUD


def display_menu():
    print("\n" + "=" * 50)
    print("📝 DATABASE-POWERED CRUD APPLICATION")
    print("=" * 50)
    print("1. Create Post")
    print("2. Create Comment")
    print("3. View All Posts")
    print("4. View Single Post with Comments")
    print("5. Update Post")
    print("6. Update Comment")
    print("7. Delete Post")
    print("8. Delete Comment")
    print("0. Exit")
    print("=" * 50)


def main():
    crud = DatabasePostCRUD()

    # Add some sample data only if database is empty
    print("🚀 Checking for existing data...")
    existing_posts = crud.read_all_posts()

    if not existing_posts:
        print("Adding sample data...")
        crud.create_post("Welcome to my blog", "This is my first blog post!", "Rahma Ras")
        crud.create_post("Python Tips", "Here are some useful Python tips...", "Rahma Ras")
        crud.create_comment(1, "Great first post!", "Alice")
        crud.create_comment(1, "Looking forward to more content!", "Bob")
    else:
        print("Database already contains data.")

    while True:
        display_menu()
        choice = input("\n👉 Enter your choice (0-8): ").strip()

        if choice == '1':
            title = input("📝 Enter post title: ")
            content = input("📝 Enter post content: ")
            author = input("👤 Enter author name: ")
            crud.create_post(title, content, author)

        elif choice == '2':
            crud.read_all_posts()
            try:
                post_id = int(input("📝 Enter post ID to comment on: "))
                content = input("💬 Enter comment: ")
                author = input("👤 Enter your name: ")
                crud.create_comment(post_id, content, author)
            except ValueError:
                print("❌ Please enter a valid post ID!")

        elif choice == '3':
            crud.read_all_posts()

        elif choice == '4':
            try:
                post_id = int(input("📖 Enter post ID to view: "))
                crud.read_post(post_id)
            except ValueError:
                print("❌ Please enter a valid post ID!")

        elif choice == '5':
            try:
                post_id = int(input("✏️ Enter post ID to update: "))
                title = input("📝 Enter new title (press Enter to skip): ").strip()
                content = input("📝 Enter new content (press Enter to skip): ").strip()
                title = title if title else None
                content = content if content else None
                crud.update_post(post_id, title, content)
            except ValueError:
                print("❌ Please enter a valid post ID!")

        elif choice == '6':
            try:
                comment_id = int(input("✏️ Enter comment ID to update: "))
                content = input("💬 Enter new comment: ")
                crud.update_comment(comment_id, content)
            except ValueError:
                print("❌ Please enter a valid comment ID!")

        elif choice == '7':
            try:
                post_id = int(input("🗑️ Enter post ID to delete: "))
                crud.delete_post(post_id)
            except ValueError:
                print("❌ Please enter a valid post ID!")

        elif choice == '8':
            try:
                comment_id = int(input("🗑️ Enter comment ID to delete: "))
                crud.delete_comment(comment_id)
            except ValueError:
                print("❌ Please enter a valid comment ID!")

        elif choice == '0':
            print("👋 Thank you for using the DATABASE CRUD app! Goodbye!")
            break

        else:
            print("❌ Invalid choice! Please try again.")

        input("\n⏎ Press Enter to continue...")


if __name__ == "__main__":
    main()