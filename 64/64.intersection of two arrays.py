class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))

print("Enter the first list: ")
nums1 = list(map(int, input().split()))
print("Enter the second list: ")
nums2 = list(map(int, input().split()))
print(Solution().intersection(nums1, nums2))
