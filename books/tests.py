from django.test import TestCase
from django.urls import reverse

from .models import Book


class Booktests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title='A good thing',
            subtitle='An excellent subtitle',
            author='Tom Christie',
            isbn='1234567890123',
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, 'A good thing')
        self.assertEqual(self.book.subtitle, 'An excellent subtitle')
        self.assertEqual(self.book.author, 'Tom Christie')
        self.assertEqual(self.book.isbn, '1234567890123')

    def test_book_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'excellent')
        self.assertTemplateUsed(response, 'book_list.html')
