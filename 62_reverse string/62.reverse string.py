class Solution(object):
    def reverseString(self, s):
        return s[::-1]
    
print("Enter the string: ")
s = input()
print(Solution().reverseString(s))