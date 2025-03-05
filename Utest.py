import unittest
import test_1

class test(unittest.TestCase):
    def test_palindrome(self):
        self.assertEqual(test_1.palindrome("malayalam"), "malayalam")
    def test_palindrome(self):
        self.assertEqual(test_1.palindrome("nun"), "nun")
    def test_palindrome(self):
        self.assertEqual(test_1.palindrome("deed"), "deed")
    def test_palindrome(self):
        self.assertEqual(test_1.palindrome("level"), "level")
    def test_palindrome(self):
        self.assertEqual(test_1.palindrome("solos"), "solos")


    def test_back_string(self):
        self.assertEqual(test_1.back_string("asd"), "dsa")
    def test_back_string(self):
        self.assertEqual(test_1.back_string("asdfgh"), "hgfdsa")
    def test_back_string(self):
        self.assertEqual(test_1.back_string("kill"), "llik")
    def test_back_string(self):
        self.assertEqual(test_1.back_string("nuul"), "luun")
    def test_back_string(self):
        self.assertEqual(test_1.back_string("eqwe"), "ewqe")


    def test_vowels(self):
        self.assertEqual(test_1.vowels("афв"), 1)
    def test_vowels(self):
        self.assertEqual(test_1.vowels("ааффыыв"), 4)
    def test_vowels(self):
        self.assertEqual(test_1.vowels("аюв"), 2)
    def test_vowels(self):
        self.assertEqual(test_1.vowels("аЁфук"), 3)
    def test_vowels(self):
        self.assertEqual(test_1.vowels("ккккукуку"), 3)


    def test_remove_duplicates(self):
        self.assertEqual(test_1.remove_duplicates("hello world"), "helo wrd")
    def test_remove_duplicates(self):
        self.assertEqual(test_1.remove_duplicates("he knows English"), "he knows gli")
    def test_remove_duplicates(self):
        self.assertEqual(test_1.remove_duplicates("wooedd"), "woed")
    def test_remove_duplicates(self):
        self.assertEqual(test_1.remove_duplicates("asdasd"), "asd")
    def test_remove_duplicates(self):
        self.assertEqual(test_1.remove_duplicates("qweqweqwe"), "qwe")
if __name__ == 'main':
    unittest.main()