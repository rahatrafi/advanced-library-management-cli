import json
import random
import save_all_books
from datetime import datetime

def add_books(all_books):
    try:
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        year = int(input("Enter Publishing Year Number: "))
        price = float(input("Enter Book Price: "))
        quantity = int(input("Enter Quantity Number: "))

        isbn = random.randint(10000, 99999)

        # Current date and time for "added time"
        book_added_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        new_book = {
            "title": title,
            "author": author,
            "isbn": isbn,
            "year": year,
            "price": price,
            "quantity": quantity,
            "bookAddedAt": book_added_at,
            "bookLastUpdatedAt": book_added_at,
            "lending_info": []
        }

        all_books.append(new_book)
        save_all_books.save_all_books(all_books)
        print(f"Book '{title}' added successfully!")
    except ValueError as e:
        print(f"Error: {e}. Please enter valid numeric values where applicable.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return all_books
