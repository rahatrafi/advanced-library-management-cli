import json

def save_all_books(all_books):
    try:
        with open("all_books.json", "w") as file:
            json.dump(all_books, file, indent=4)
    except Exception as e:
        print(f"An error occurred while saving books: {e}")
