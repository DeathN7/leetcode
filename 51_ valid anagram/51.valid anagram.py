class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
    def stringToString(self, input):
        import json
        return json.loads(input) 
    def boolToString(self, input):
        return str(input).lower()
    
print("Enter two strings separated by space: ")
s, t = input().split()
ret = Solution().isAnagram(s, t)
out = (ret)
print(out)