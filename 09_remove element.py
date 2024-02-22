class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
    
nums = input("Input array: ").split()
val = input("Input value to remove: ")
print(Solution().removeElement(nums, val))