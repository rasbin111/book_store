from django.test import TestCase
from apps.author.models import Author

class TestModelCreation(TestCase):

    def setUp(self, methodName = "runTest"):
        """
        Runs before every test method. 
        Django automatically handles the database transaction/cleanup.
        """
        Author.objects.create(author_id="auth1", name="Auth 1")

    def test_author_data(self):
        author = Author.objects.last()
        self.assertEqual(author.author_id, "auth1")