import random  

# List of books with their availability status (True = Available, False = Not Available)
books = [
    ("Harry Potter", True), ("1984", False), ("The Hobbit", True), ("Moby Dick", False), 
    ("Pride and Prejudice", True), ("The Great Gatsby", True), ("War and Peace", False), 
    ("Ulysses", True), ("The Catcher in the Rye", False), ("Crime and Punishment", True), 
    ("Brave New World", True), ("The Odyssey", False), ("The Iliad", True), ("Hamlet", True), 
    ("Don Quixote", False), ("Dracula", True), ("Frankenstein", True), ("The Count of Monte Cristo", False), 
    ("A Tale of Two Cities", True), ("Les Misérables", False), ("The Divine Comedy", True), 
    ("The Brothers Karamazov", True), ("The Scarlet Letter", False), ("Wuthering Heights", True), 
    ("Alice's Adventures in Wonderland", True), ("The Picture of Dorian Gray", False), 
    ("The Metamorphosis", True), ("Heart of Darkness", False), ("The Shining", True), 
    ("Dune", True), ("Fahrenheit 451", False), ("The Road", True), ("The Stand", False), 
    ("The Martian", True), ("The Book Thief", False), ("The Maze Runner", True), 
    ("Eragon", False), ("The Golden Compass", True), ("Red Rising", True), 
    ("The Name of the Wind", False), ("The Lies of Locke Lamora", True), 
    ("The Way of Kings", False), ("Mistborn", True), ("The Wheel of Time", False), 
    ("The Sword of Shannara", True), ("A Song of Ice and Fire", False), 
    ("The Hunger Games", True), ("Percy Jackson", False), ("The Lightning Thief", True), 
    ("The Girl with the Dragon Tattoo", True), ("The Da Vinci Code", False), 
    ("Angels & Demons", True), ("The Lost Symbol", False), ("Inferno", True), 
    ("The Alchemist", False), ("The Kite Runner", True), ("A Thousand Splendid Suns", False), 
    ("The Shadow of the Wind", True), ("The Night Circus", False), ("Circe", True)
]

def get_neighbors(index):
    """Returns neighboring books in list format [Previous, Next]"""
    prev_book = books[index - 1][0] if index > 0 else None
    next_book = books[index + 1][0] if index < len(books) - 1 else None
    return [prev_book, next_book]

def find_book(book_name):
    """Find book in list and return its availability, neighbors, index, and name length"""
    for i, (title, available) in enumerate(books):
        if title.lower() == book_name.lower():
            neighbors = get_neighbors(i)
            name_length = len(title)  # Calculate name length
            return bool(available), neighbors, i, name_length  # Explicitly return bool value
    return None, None, None, None  # Book not found

def suggest_random_book():
    """Suggests a random book with its availability"""
    book, available = random.choice(books)
    return f"How about '{book}'? Available: {bool(available)}"  # Explicitly convert to bool

# User input
book_name = input("Enter a book name: ").strip()

# Find book details
availability, neighbors, book_index, name_length = find_book(book_name)

if availability is not None:
    print(f"'{book_name}' Availability (bool): {availability}")  # Explicit bool representation
    print(f"Neighbors: {neighbors}")  # Show neighboring books
    print(f"Book Index in List: {book_index}")  # Show index
    print(f"Length of Book Name: {name_length} characters")  # Show name length
else:
    print(f"'{book_name}' not found in the database.")
    print(suggest_random_book())  # Suggest a random book

# Example to calculate length of a number (number of digits in 12345)
print(len(str(12345)))  # Convert the number to a string and then find its length