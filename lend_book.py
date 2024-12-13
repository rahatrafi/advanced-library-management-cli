import save_all_books
from datetime import datetime, timedelta

def lend_book(all_books):
    try:
        search_book = input("Enter Book Title to Lend: ")
        for book in all_books:
            if book["title"] == search_book:
                if book["quantity"] > 0:
                    borrower_name = input("Enter Borrower's Name: ")
                    borrower_phone = input("Enter Borrower's Phone Number: ")

                    # Set return due date to be max 7 days from today
                    lending_date = datetime.now()
                    due_date = lending_date + timedelta(days=7)
                    due_date_str = due_date.strftime("%d-%m-%Y")

                    book["lending_info"].append({
                        "borrower_name": borrower_name,
                        "borrower_phone": borrower_phone,
                        "lending_date": lending_date.strftime("%d-%m-%Y"),
                        "return_due_date": due_date_str
                    })

                    # Decrease the quantity of the book
                    book["quantity"] -= 1
                    save_all_books.save_all_books(all_books)
                    print(f"Book '{search_book}' lent to {borrower_name}. Return due by {due_date_str}.")
                    return all_books
                else:
                    print("There are not enough books available to lend.")
                    return all_books
        print("Book Not Found")
    except ValueError as e:
        print(f"Error: {e}. Please check the entered date format.")
    except Exception as e:
        print(f"An error occurred while lending the book: {e}")
    return all_books
