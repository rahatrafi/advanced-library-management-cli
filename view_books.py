def view_all_books(all_books):
    try:
        if not all_books:
            print("No books available in the library.")
            return

        print("\nBooks in Library:")
        for idx, book in enumerate(all_books, 1):
            print(f"{idx}. Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, "
                  f"Year: {book['year']}, Price: {book['price']}, Quantity: {book['quantity']}, "
                  f"Added On: {book['bookAddedAt']}, Last Updated: {book['bookLastUpdatedAt']}")
            if book["lending_info"]:
                for lending in book["lending_info"]:
                    print(f"   - Borrowed by {lending['borrower_name']} (Due: {lending['return_due_date']})")
            else:
                print("   - Available for lending")
    except Exception as e:
        print(f"An error occurred while viewing books: {e}")
