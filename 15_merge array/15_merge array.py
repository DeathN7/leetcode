class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[m:] = nums2[:n]
        nums1.sort()
        return nums1
    
num1 = input("nhap mang 1: ").split()
num2 = input("nhap mang 2: ").split()
m = int(input("nhap m: "))
n = int(input("nhap n: "))

print(Solution().merge(num1, m, num2, n))