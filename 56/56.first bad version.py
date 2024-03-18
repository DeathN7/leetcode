def isBadVersion(version):
    pass

class Solution(object):
    def firstBadVersion(self, n):
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
    
print("Enter the number of versions: ")
n = int(input())
print(Solution().firstBadVersion(n))
