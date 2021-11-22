from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from .models import Book

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
      
        testuser1 = User.objects.create_user(username="testuser1", password="abc123")
        testuser1.save()

     
        test_book = Book.objects.create(
            publisher=testuser1, name="Blog title", description="Body content..."
        )
        test_book.save()

    def test_blog_content(self):
        book = Book.objects.get(id=1)
        expected_publisher = f"{book.publisher}"
        expected_name = f"{book.name}"
        expected_description = f"{book.description}"
        self.assertEqual(expected_publisher, "testuser1")
        self.assertEqual(expected_name, "Blog title")
        self.assertEqual(expected_description, "Body content...")

class PostModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_post = Book.objects.create(
            publisher = test_user,
            name = 'Title of Blog',
            description = 'Words about the blog'
        )
        test_post.save()

    def test_blog_content(self):
        book = Book.objects.get(id=1)

        self.assertEqual(str(book.publisher), 'tester')
        self.assertEqual(book.name, 'Title of Blog')
        self.assertEqual(book.description, 'Words about the blog')        