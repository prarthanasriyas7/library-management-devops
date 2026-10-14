
"""Library Management System for the DevOps practicum."""


class Library:
    def __init__(self):
        self.books = {
            "B001": {
                "title": "Python Programming",
                "author": "John Smith",
                "available": True
            },
            "B002": {
                "title": "Data Structures",
                "author": "Mark Allen",
                "available": True
            },
            "B003": {
                "title": "Computer Networks",
                "author": "Andrew Tanenbaum",
                "available": False
            }
        }

    def add_book(self, book_id, title, author):
        book_id = book_id.strip().upper()
        title = title.strip()
        author = author.strip()

        if not book_id or not title or not author:
            raise ValueError(
                "Book ID, title, and author are required."
            )

        if book_id in self.books:
            raise ValueError(
                "A book with this ID already exists."
            )

        self.books[book_id] = {
            "title": title,
            "author": author,
            "available": True
        }

        return self.books[book_id]

    def search_book(self, keyword):
        keyword = keyword.strip().lower()

        if not keyword:
            return []

        results = []

        for book_id, details in self.books.items():
            if (
                keyword in book_id.lower()
                or keyword in details["title"].lower()
                or keyword in details["author"].lower()
            ):
                results.append({
                    "book_id": book_id,
                    **details
                })

        return results

    def issue_book(self, book_id):
        book_id = book_id.strip().upper()

        if book_id not in self.books:
            raise KeyError("Book not found.")

        if not self.books[book_id]["available"]:
            raise ValueError("Book is already issued.")

        self.books[book_id]["available"] = False
        return True

    def return_book(self, book_id):
        book_id = book_id.strip().upper()

        if book_id not in self.books:
            raise KeyError("Book not found.")

        if self.books[book_id]["available"]:
            raise ValueError("Book is already available.")

        self.books[book_id]["available"] = True
        return True

    def delete_book(self, book_id):
        book_id = book_id.strip().upper()

        if book_id not in self.books:
            raise KeyError("Book not found.")

        del self.books[book_id]
        return True

    def get_stats(self):
        total = len(self.books)

        available = sum(
            1 for book in self.books.values()
            if book["available"]
        )

        issued = total - available

        return {
            "total": total,
            "available": available,
            "issued": issued
        }
