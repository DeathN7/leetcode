class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
    
    def stringToIntegerList(self, input):
        import json
        return json.loads(input)

print("Enter a list of numbers separated by space: ")
nums = input()
nums = Solution().stringToIntegerList(nums)

ret = Solution().containsDuplicate(nums)
out = (ret)
print(out)

