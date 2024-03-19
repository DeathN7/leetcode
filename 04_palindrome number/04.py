#Given an integer x, return true if x is a palindrome, and false otherwise.
class Solution(object):
    def isPalindrome(self, x):        
        if x < 0:
            return False
        x = str(x)
        return x == x[::-1]
    
