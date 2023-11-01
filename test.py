import unittest
from workouts import palindrome, freq


class TestPalindrome(unittest.TestCase):
    def testIsPalindrome(self):
        sentence = "adda"
        self.assertTrue(palindrome(sentence))

    def testIsNotPalindrome(self):
        sentence = "hello"
        self.assertFalse(palindrome(sentence))
    
    def testEmptyInput(self):
        emp = palindrome("")
        self.assertTrue(emp)  



class TestforFreq(unittest.TestCase):
    def testCharacters(self):
        string = "hello"
        expected_string = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
        self.assertEqual(expected_string, freq(string))



if __name__ == '__main__':
    unittest.main()


        


