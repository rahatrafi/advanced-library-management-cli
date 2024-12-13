import save_all_books
from datetime import datetime

def update_book(all_books):
    try:
        # Prompt user for the book to update
        search_book = input("Enter Book Title to Update: ")
        
        # Loop through all books to find the book by title
        for book in all_books:
            if book["title"].lower() == search_book.lower():  # Case-insensitive comparison
                print("Current Book Details:")
                print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, "
                      f"Year: {book['year']}, Price: {book['price']}, Quantity: {book['quantity']}")
                
                # Prompt user for new information
                new_title = input("Enter new title (leave blank to keep current): ")
                new_author = input("Enter new author (leave blank to keep current): ")
                new_price = input("Enter new price (leave blank to keep current): ")
                new_quantity = input("Enter new quantity (leave blank to keep current): ")

                # Update book details if provided
                if new_title:
                    book['title'] = new_title
                if new_author:
                    book['author'] = new_author
                if new_price:
                    book['price'] = float(new_price)  # Convert to float
                if new_quantity:
                    book['quantity'] = int(new_quantity)  # Convert to int

                # Update the 'last updated' timestamp
                book["bookLastUpdatedAt"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

                # Save the updated books list
                save_all_books.save_all_books(all_books)
                print(f"Book '{search_book}' updated successfully!")
                return all_books

        print("Book Not Found")  # If no book is found with the title
    except ValueError as e:
        print(f"Error: {e}. Please check the entered values.")
    except Exception as e:
        print(f"An error occurred while updating the book: {e}")
    
    return all_books
