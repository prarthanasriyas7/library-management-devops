
"""Automated tests for the Library Management System."""

import unittest
from library import Library


class LibraryTests(unittest.TestCase):

    def setUp(self):
        self.library = Library()

    def test_initial_book_count(self):
        self.assertEqual(
            self.library.get_stats()["total"], 3
        )

    def test_add_book(self):
        self.library.add_book(
            "B004", "Clean Code", "Robert Martin"
        )

        self.assertEqual(
            self.library.get_stats()["total"], 4
        )

        result = self.library.search_book("Clean Code")
        self.assertEqual(result[0]["book_id"], "B004")

    def test_duplicate_book_id_is_rejected(self):
        with self.assertRaises(ValueError):
            self.library.add_book(
                "B001", "Another Book", "Some Author"
            )

    def test_empty_fields_are_rejected(self):
        with self.assertRaises(ValueError):
            self.library.add_book(
                "", "Book Title", "Author"
            )

    def test_search_by_title(self):
        results = self.library.search_book("Python")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["book_id"], "B001")

    def test_search_is_case_insensitive(self):
        results = self.library.search_book("python")
        self.assertEqual(len(results), 1)

    def test_issue_available_book(self):
        self.library.issue_book("B001")

        self.assertFalse(
            self.library.books["B001"]["available"]
        )

        self.assertEqual(
            self.library.get_stats()["issued"], 2
        )

    def test_cannot_issue_already_issued_book(self):
        with self.assertRaises(ValueError):
            self.library.issue_book("B003")

    def test_return_issued_book(self):
        self.library.return_book("B003")

        self.assertTrue(
            self.library.books["B003"]["available"]
        )

    def test_cannot_return_available_book(self):
        with self.assertRaises(ValueError):
            self.library.return_book("B001")

    def test_delete_book(self):
        self.library.delete_book("B002")

        self.assertNotIn("B002", self.library.books)
        self.assertEqual(
            self.library.get_stats()["total"], 2
        )

    def test_unknown_book_raises_error(self):
        with self.assertRaises(KeyError):
            self.library.issue_book("B999")


if __name__ == "__main__":
    unittest.main(verbosity=2)
