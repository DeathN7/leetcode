class Solution(object):
    def mySqrt(self, x):
        if x < 2:
            return x
        left = 1
        right = x
        while left < right:
            mid = left + (right - left) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid
        return left - 1

input_string = input("Enter a string: ")
print("Square root:", Solution().mySqrt(input_string))