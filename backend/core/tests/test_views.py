from django.test import SimpleTestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status

COUNT_NUMBER_URL = reverse("count-number-of-words")


class ViewsTests(SimpleTestCase):
    def setUp(self):
        self.client = APIClient()

    def test_count_number_of_words(self):
        """Test that count number of words view works"""
        text = "That is a test text"
        response = self.client.post(
            COUNT_NUMBER_URL, {"text": text}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_count_number_of_words_with_empty_text_fails(self):
        """Test that count number of words view with empty text fails"""
        text = ""
        response = self.client.post(
            COUNT_NUMBER_URL, {"text": text}, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_count_number_of_words_with_null_text_fails(self):
        """Test that count number of words view with null text fails"""
        response = self.client.post(
            COUNT_NUMBER_URL, {}, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
