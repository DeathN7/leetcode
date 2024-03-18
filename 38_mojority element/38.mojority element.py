class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]
    
input_string = input("Enter a string: ")
print("Majority element:", Solution().majorityElement(input_string))