from odoo.tests.common import TransactionCase

class TestBook(TransactionCase):
    def setUp(self, *arg, **kwargs):
        super().setUp(*arg, **kwargs)
        user_admin = self.env.ref("base.user_admin")
        self.env = self.env(user=user_admin)
        self.Book = self.env["tutorial.library.book"]
        self.book1 = self.Book.create(
            {"name": "Odoo Development Essentials", "isbn": "123-4-56789-101-2"}
        )
    
    def test_book_create(self):
        "New Books are active by default"
        self.assertEqual(self.book1.active, True)
    
    def test_check_isbn(self):
        "Check valid ISBN"
        self.assertTrue(self.book1.check_isbn)