class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest
    
input_string = input("Enter a list of strings: ")
input_list = input_string.split()
print("Longest Common Prefix:", Solution().longestCommonPrefix(input_list))
# Example: Enter a list of strings: flower flow flight
