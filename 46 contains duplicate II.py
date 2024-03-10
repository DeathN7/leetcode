class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        d = {}
        for i, num in enumerate(nums):
            if num in d and i - d[num] <= k:
                return True
            d[num] = i
        return False
    
    def stringToIntegerList(self, input):
        import json
        return json.loads(input)
    
    def stringToInt(self, input):
        return int(input)
    
print("Enter a list of numbers separated by space: ")
nums = input()
nums = Solution().stringToIntegerList(nums)
print("Enter an integer: ")
k = input()
k = Solution().stringToInt(k)

ret = Solution().containsNearbyDuplicate(nums, k)
out = (ret)
print(out)
