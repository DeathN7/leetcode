class Solution(object):
    def countBits(self, n):
        return [bin(i).count('1') for i in range(n + 1)]
    
print("Enter the number: ")
n = int(input())
print(Solution().countBits(n))