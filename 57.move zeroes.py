class Solution(object):
    def moveZeroes(self, nums):
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
        return nums

print("Enter the list of numbers: ")
nums = list(map(int, input().split()))
print(Solution().moveZeroes(nums))

