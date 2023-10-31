import unittest
 def palindrome(s):
     s = s.replace(" ", "").lower()
     return s == s[::-1]
     
     
     
 class TestPalindrome(unittest.TestCase):
     def testIsPalindrome(self):
         sentence = "adda"
         self.assertTrue(palindrome(sentence))
     def testIsNotPalindrome(self):
         sentence = "sarath"
         self.assertFalse(palindrome(sentence))
     def testEmptyInput(self):
         ret = palindrome("")
         self.assertTrue(ret)
         
         
 if __name__ == '__main__':
     unittest.main()
     
def freq(s):
    frequency = {}
    for i in s:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    return frequency
    
 class TestFreq(unittest.TestCase):
 
    def testIsFreq(self):
        sentence = "hai i am sarath"
        self.assertTrue(freq(sentence))
   
    def testNullInput(self):
        ret = freq("")
        self.assertFalse(ret)

        

if __name__ == '__main__':
    unittest.main()
