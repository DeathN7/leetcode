class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(e for e in s if e.isalnum()).lower()
        return s == s[::-1]
    
input_string = input("Enter a string: ")
print("Is palindrome:", Solution().isPalindrome(input_string))