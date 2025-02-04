import random  

# List of books with their availability status (True = Available, False = Not Available)
books = [
    ("Harry Potter", True, 500, 20.5, "Once upon a time..."), 
    ("1984", False, 328, 15.2, "Big Brother is watching you."),
    ("The Hobbit", True, 310, 10.3, "In a hole in the ground there lived a hobbit."),
    ("Moby Dick", False, 720, 25.8, "Call me Ishmael."),
    ("Pride and Prejudice", True, 432, 18.7, "It is a truth universally acknowledged...")
]

def get_neighbors(index):
    """Returns neighboring books in list format [Previous, Next]"""
    prev_book = books[index - 1][0] if index > 0 else None
    next_book = books[index + 1][0] if index < len(books) - 1 else None
    return [prev_book, next_book]

def find_book(book_name):
    """Find book and return details: availability, neighbors, index, pages, sessions, and sample text"""
    for i, (title, available, pages, sessions, sample_text) in enumerate(books):
        if title.lower() == book_name.lower():
            neighbors = get_neighbors(i)
            name_length = len(title)  # String Length Logic
            return bool(available), neighbors, i, name_length, pages, sessions, sample_text
    return None, None, None, None, None, None, None  # Book not found

def suggest_random_book():
    """Suggests a random book with its availability"""
    book, available, pages, sessions, sample_text = random.choice(books)
    return f"How about '{book}'? Available: {bool(available)}"

# User input
book_name = input("Enter a book name: ").strip()

# Find book details
availability, neighbors, book_index, name_length, pages, sessions, sample_text = find_book(book_name)

if availability is not None:
    print(f"'{book_name}' Availability (Boolean Logic): {availability}")  # Boolean Logic
    print(f"Neighbors (Neighbor Finding Logic): {neighbors}")  # Neighbor Finding Logic
    print(f"Book Index in List (Integer Logic): {book_index} - Type: {type(book_index)}")  # Integer Logic
    print(f"Book Index as Float (Float Logic): {float(book_index)} - Type: {type(float(book_index))}")  # Float Logic
    print(f"Length of Book Name (String Length Logic): {name_length} characters - Type: {type(name_length)}")  # String Logic

    # INT: Number of pages read
    print(f"Number of Pages (Integer Logic): {pages} - Type: {type(pages)}")  

    # FLOAT: Number of reading sessions
    print(f"Number of Sessions (Float Logic): {sessions} - Type: {type(sessions)}")  

    # STR: Sample line of words from the book
    print(f"Sample Line (String Logic): '{sample_text}' - Type: {type(sample_text)}")  

else:
    print(f"'{book_name}' not found in the database.")
    print(suggest_random_book())  

# Print int, float, and str types directly
print(int(5))   # <class 'int'>
print(float(6.6)) # <class 'float'>
print(str("Yura"))   # <class 'str'>