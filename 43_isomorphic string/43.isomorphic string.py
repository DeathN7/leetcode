class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        s2t, t2s = {}, {}
        for i in range(len(s)):
            if s[i] in s2t and s2t[s[i]] != t[i]:
                return False
            if t[i] in t2s and t2s[t[i]] != s[i]:
                return False
            s2t[s[i]] = t[i]
            t2s[t[i]] = s[i]
        return True

    def stringToString(self, input):
        import json
        return json.loads(input)

print("Enter two strings separated by space: ")
s = input()
t = input()

ret = Solution().isIsomorphic(s, t)
out = (ret)
print(out)