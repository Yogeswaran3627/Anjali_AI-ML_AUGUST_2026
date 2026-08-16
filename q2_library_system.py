def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)
    print(f"Added: [{book_id}] {title} by {author} ({year})")


def borrow_book(catalog, borrowed_books, book_id):
    if book_id not in catalog:
        print(f"Cannot borrow: Book ID {book_id} does not exist.")
        return
    if book_id in borrowed_books:
        print(f"Cannot borrow: Book ID {book_id} is already borrowed.")
        return
    borrowed_books.append(book_id)
    title = catalog[book_id][0]
    print(f"Borrowed: [{book_id}] {title}")


def return_book(borrowed_books, book_id):
    """Return a borrowed book by removing it from borrowed_books."""
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Returned: Book ID {book_id}")
    else:
        print(f"Cannot return: Book ID {book_id} was not borrowed.")


def register_member(members, member_id):
    """Register a member; silently ignore duplicates."""
    if member_id in members:
        return  # silently ignore
    members.add(member_id)
    print(f"Registered member: {member_id}")


def show_available(catalog, borrowed_books):
    """Print all books not currently borrowed."""
    print("Available books:")
    for book_id, (title, author, year) in catalog.items():
        if book_id not in borrowed_books:
            print(f"  [{book_id}] {title} by {author} ({year})")


def main():
    catalog = {}
    borrowed_books = []
    members = set()

    print("--- Adding Books ---")
    add_book(catalog, 1, "The Hobbit", "J.R.R. Tolkien", 1937)
    add_book(catalog, 2, "1984", "George Orwell", 1949)
    add_book(catalog, 3, "Dune", "Frank Herbert", 1965)
    add_book(catalog, 4, "Foundation", "Isaac Asimov", 1951)

    print("\n--- Registering Members ---")
    register_member(members, 501)
    register_member(members, 502)
    register_member(members, 503)
    register_member(members, 501)  # duplicate, should be silently ignored

    print(f"\nMembers registered: {members}")

    print("\n--- Borrowing Books ---")
    borrow_book(catalog, borrowed_books, 1)
    borrow_book(catalog, borrowed_books, 3)

    print("\n--- Returning Books ---")
    return_book(borrowed_books, 1)

    print(f"\nCurrently borrowed: {borrowed_books}")

    print()
    show_available(catalog, borrowed_books)


main()