import restore_books_file
import add_books
import view_books
import update_book_file
import delete_book
import lend_book
import return_book

def main():
    try:
        all_books = restore_books_file.restore_all_books([])

        while True:
            print("\nWelcome to Library Management System")
            print("0. Exit")
            print("1. Add Books")
            print("2. View All Books")
            print("3. Update Book")
            print("4. Delete Book")
            print("5. Lend Book")
            print("6. Return Book")

            choice = input("Select any number: ")

            if choice == '0':
                break
            elif choice == '1':
                all_books = add_books.add_books(all_books)
            elif choice == '2':
                view_books.view_all_books(all_books)
            elif choice == '3':
                all_books = update_book_file.update_book(all_books)
            elif choice == '4':
                all_books = delete_book.delete_books(all_books)
            elif choice == '5':
                all_books = lend_book.lend_book(all_books)
            elif choice == '6':
                all_books = return_book.return_book(all_books)
            else:
                print("Invalid choice. Please try again.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
