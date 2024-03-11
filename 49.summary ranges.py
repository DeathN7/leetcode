class Solution(object):
    def summaryRanges(self, nums):
        ranges = []
        for n in nums:
            if not ranges or n > ranges[-1][-1] + 1:
                ranges += [],
            ranges[-1][1:] = n,
        return ['->'.join(map(str, r)) for r in ranges]
    
    def stringToIntegerList(self, input):
        import json
        return json.loads(input)
    
    def integerListToString(self, nums, len_of_list=None):
        import json
        if not len_of_list:
            return json.dumps(nums)
        return json.dumps(nums[:len_of_list])
    
    def stringToString(self, input):
        import json
        return json.loads(input)
    
    
print("Enter a list of numbers separated by space: ")
nums = input()
nums = Solution().stringToIntegerList(nums)

ret = Solution().summaryRanges(nums)

out = (ret)
print(out)

    
    