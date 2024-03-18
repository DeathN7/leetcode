class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
input_string = input("Enter a string: ")
print("Index of the first occurrence of the substring:", Solution().searchInsert(input_string, "the"))
