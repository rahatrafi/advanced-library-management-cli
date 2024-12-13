import save_all_books
from datetime import datetime

def return_book(all_books):
    try:
        search_book = input("Enter Book Title to Return: ")
        for book in all_books:
            if book["title"] == search_book:
                if "lending_info" in book and len(book["lending_info"]) > 0:
                    print("Lending Information:")
                    for idx, lending in enumerate(book["lending_info"], 1):
                        print(f"{idx}. Borrower: {lending['borrower_name']}, Due Date: {lending['return_due_date']}")
                    
                    borrower_choice = int(input("Enter the number of the borrower returning the book: ")) - 1
                    
                    if 0 <= borrower_choice < len(book["lending_info"]):
                        returned_lending = book["lending_info"].pop(borrower_choice)
                        book["quantity"] += 1
                        save_all_books.save_all_books(all_books)
                        print(f"Book '{search_book}' returned by {returned_lending['borrower_name']}.")
                        return all_books
                    else:
                        print("Invalid borrower selection.")
                else:
                    print(f"No records found for borrowed book '{search_book}'.")
                return all_books
        print("Book Not Found")
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid borrower number.")
    except Exception as e:
        print(f"An error occurred while returning the book: {e}")
    return all_books
