class Solution(object):
    def longestPalindrome(self, s):
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        start, end = 0, 0
        for i in range(len(s)):
            len1 = expandAroundCenter(i, i)
            len2 = expandAroundCenter(i, i + 1)
            length = max(len1, len2)
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2
        return s[start:end + 1]
    
input_string = input("Enter a string: ")
print("Longest Palindromic Substring:", Solution().longestPalindrome(input_string))
