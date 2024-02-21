class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        char_map = {}
        i = 0
        for j in range(n):
            if s[j] in char_map:
                i = max(char_map[s[j]], i)
            ans = max(ans, j - i + 1)
            char_map[s[j]] = j + 1
        return ans