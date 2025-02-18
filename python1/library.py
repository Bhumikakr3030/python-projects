class Book:
    def __init__(self, book_id, title, author, available_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available_copies = available_copies

    def __str__(self):
        return f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Available Copies: {self.available_copies}"


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available_copies > 0:
            self.borrowed_books.append(book)
            book.available_copies -= 1
            print(f"{self.name} borrowed '{book.title}' successfully.")
        else:
            print(f"Sorry, '{book.title}' is currently unavailable.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available_copies += 1
            print(f"{self.name} returned '{book.title}' successfully.")
        else:
            print(f"{self.name} did not borrow '{book.title}'.")


class Library:
    def __init__(self):
        self.books = []
        self.students = []

    def add_book(self, book):
        self.books.append(book)
        print(f"'{book.title}' has been added to the library.")

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print(f"'{book.title}' has been removed from the library.")
                return
        print("Book not found.")

    def add_student(self, student):
        self.students.append(student)
        print(f"{student.name} has been added to the system.")

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print(f"{student.name} has been removed from the system.")
                return
        print("Student not found.")

    def view_books(self):
        if not self.books:
            print("No books available.")
        else:
            for book in self.books:
                print(book)

    def search_books(self, title=None, author=None):
        found_books = [book for book in self.books if (title and title.lower() in book.title.lower()) or (
                    author and author.lower() in book.author.lower())]

        if found_books:
            for book in found_books:
                print(book)
        else:
            print("No books found matching the search criteria.")


def main():
    library = Library()

    while True:
        print("\nCollege Library Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Add Student")
        print("4. Remove Student")
        print("5. View All Books")
        print("6. Search for a Book")
        print("7. Issue Book")
        print("8. Return Book")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            book_id = input("Enter book ID: ")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            available_copies = int(input("Enter number of available copies: "))
            book = Book(book_id, title, author, available_copies)
            library.add_book(book)

        elif choice == '2':
            book_id = input("Enter book ID to remove: ")
            library.remove_book(book_id)

        elif choice == '3':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            student = Student(student_id, name)
            library.add_student(student)

        elif choice == '4':
            student_id = input("Enter student ID to remove: ")
            library.remove_student(student_id)

        elif choice == '5':
            library.view_books()

        elif choice == '6':
            title = input("Enter book title to search (optional): ")
            author = input("Enter author name to search (optional): ")
            library.search_books(title, author)

        elif choice == '7':
            student_id = input("Enter student ID: ")
            book_id = input("Enter book ID to borrow: ")
            student = next((student for student in library.students if student.student_id == student_id), None)
            book = next((book for book in library.books if book.book_id == book_id), None)

            if student and book:
                student.borrow_book(book)
            else:
                print("Invalid student or book ID.")

        elif choice == '8':
            student_id = input("Enter student ID: ")
            book_id = input("Enter book ID to return: ")
            student = next((student for student in library.students if student.student_id == student_id), None)
            book = next((book for book in library.books if book.book_id == book_id), None)

            if student and book:
                student.return_book(book)
            else:
                print("Invalid student or book ID.")

        elif choice == '9':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
