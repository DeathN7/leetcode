class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
    
nums = input("nhap mang: ").split()
val = input("nhap so can xoa: ")
print(Solution().removeElement(nums, val))