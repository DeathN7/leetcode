class Solution(object):
    def lengthOfLastWord(self, s):
        return len(s.split()[-1]) if s.split() else 0
s = input("Nhap: ")
print(Solution().lengthOfLastWord(s))
