class Solution(object):
    def isPowerOfFour(self, n):
        return n > 0 and n & (n - 1) == 0 and n % 3 == 1
    
print("Enter the number: ")
n = int(input())
print(Solution().isPowerOfFour(n))