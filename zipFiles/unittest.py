import unittest
import capitalize

class test_cap(unittest.TestCase):
    def cap_text(text):
        return  text.capitalize()
    def test_one_cap(self):

        text = 'python'
        result = capitalize.cap_text(text)
        self.assertEqual(result,'Python')