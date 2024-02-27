from django.test import TestCase
from .cipher import caesar_encode
# Create your tests here.
class CiphersTest(TestCase):
    def test_caesarencoding_1(self):
        plain_text = "hello"        
        shift=1
        expected ="ifmmp"
        self.assertEqual(expected, caesar_encode(plain_text, shift))
        
    def test_caesarencoding_2(self):
        plain_text = "winter"        
        shift=3
        expected ="zlqwhu"
        self.assertEqual(expected, caesar_encode(plain_text, shift))