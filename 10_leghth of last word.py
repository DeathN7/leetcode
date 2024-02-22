class Solution(object):
    def lengthOfLastWord(self, s):
        return len(s.split()[-1]) if s.split() else 0
s = input("Input string: ")
print(Solution().lengthOfLastWord(s))
