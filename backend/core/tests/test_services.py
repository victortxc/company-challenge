from django.test import SimpleTesteCase

from core import services

class ServicesTests(SimpleTesteCase):
    def test_count_number_of_words(self):
        """Test that count number of words service works"""
        text = "Hello world"

        number_of_words = services.count_number_of_words(text)
        self.assertEqual(number_of_words, 2)