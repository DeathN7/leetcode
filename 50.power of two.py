class Solution(object):
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n - 1)) == 0
    
    def stringToInteger(self, input):
        return int(input)
    
    def boolToString(self, input):
        return str(input).lower()
     
print("Enter a number: ")
n = input()
n = Solution().stringToInteger(n)
ret = Solution().isPowerOfTwo(n)
out = (ret)
print(out)

