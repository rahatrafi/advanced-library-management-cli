import save_all_books

def delete_books(all_books):
    try:
        search_book = input("Enter Book Title to Delete: ")
        for book in all_books:
            if book["title"] == search_book:
                if book["lending_info"]:  # Check if there is lending info (book is borrowed)
                    print("This book cannot be deleted because it is currently borrowed.")
                    return all_books
                all_books.remove(book)
                save_all_books.save_all_books(all_books)
                print("Book Deleted Successfully")
                return all_books
        print("Book Not Found")
    except Exception as e:
        print(f"An error occurred while deleting the book: {e}")
    return all_books
