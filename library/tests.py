
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status 
from rest_framework.test import APITestCase


from .models import Book

class BookModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_book = Book.objects.create(
            publisher = test_user,
            name = 'Title of Blog',
            description = 'Words about the blog'
        )
        test_book.save()

    def test_blog_content(self):
        book = Book.objects.get(id=1)

        self.assertEqual(str(book.publisher), 'tester')
        self.assertEqual(book.name, 'Title of Blog')
        self.assertEqual(book.description, 'Words about the blog')

class APITest(APITestCase):
    def test_list(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail(self):

        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_book = Book.objects.create(
            publisher = test_user,
            name = 'Title of Blog',
            description = 'Words about the blog'
        )
        test_book.save()

        response = self.client.get(reverse('book_detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,{
            'id':1,
            'name': test_book.name,
            'description': test_book.description,
            'publisher': test_user.id,
        })


    def test_create(self):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        url = reverse('book_list')
        data = {
            "name":"Testing is Fun!!!",
            "description":"when the right tools are available",
            "publisher":test_user.id,
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, test_user.id)

        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().name, data['name'])

    def test_update(self):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_book = Book.objects.create(
            publisher = test_user,
            name = 'Title of Blog',
            description = 'Words about the blog'
        )

        test_book.save()

        url = reverse('book_detail',args=[test_book.id])
        data = {
            "name":"Testing is Still Fun!!!",
            "publisher":test_book.publisher.id,
            "description":test_book.description,
        }

        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK, url)

        self.assertEqual(Book.objects.count(), test_book.id)
        self.assertEqual(Book.objects.get().name, data['name'])


    def test_delete(self):
        """Test the api can delete a book."""

        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_book = Book.objects.create(
            publisher = test_user,
            name = 'Title of Blog',
            description = 'Words about the blog'
        )

        test_book.save()

        book = Book.objects.get()

        url = reverse('book_detail', kwargs={'pk': book.id})


        response = self.client.delete(url)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT, url)


