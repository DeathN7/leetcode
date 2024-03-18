class Solution(object):
    def wordPattern(self, pattern, s):
        s = s.split()
        if len(pattern) != len(s):
            return False
        return list(map(pattern.index, pattern)) == list(map(s.index, s))
    
print("Enter the pattern: ")
pattern = list(input())
print("Enter the string: ")
s = input()
print(Solution().wordPattern(pattern, s))
