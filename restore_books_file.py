import json

def restore_all_books(all_books):
    try:
        with open("all_books.json", "r") as fp:
            all_books = json.load(fp)
    except (FileNotFoundError, json.JSONDecodeError):
        print("The 'all_books.json' file is empty or doesn't exist. Starting fresh.")
        all_books = []
    except Exception as e:
        print(f"An error occurred while restoring books: {e}")
    return all_books
