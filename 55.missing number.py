class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
    
print("Enter a list of numbers: ")
nums = list(map(int, input().split()))
print(Solution().missingNumber(nums))