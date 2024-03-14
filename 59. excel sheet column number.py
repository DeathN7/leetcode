class Solution(object):
    def titleToNumber(self, columnTitle):
        return sum((ord(columnTitle[i]) - 64) * (26 ** (len(columnTitle) - i - 1)) for i in range(len(columnTitle)))
    
print("Enter the column title: ")
columnTitle = input()
print(Solution().titleToNumber(columnTitle))
