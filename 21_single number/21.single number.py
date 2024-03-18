class Solution(object):
    def singleNumber(self, nums):
        return 2 * sum(set(nums)) - sum(nums)

input_string = input("Enter a list of numbers: ")
input_list = input_string.split()
print("Single Number:", Solution().singleNumber(input_list))
