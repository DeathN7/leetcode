class Solution(object):
    def addDigits(self, num):
        if num == 0:
            return 0
        return 1 + (num - 1) % 9
    
print("Enter a number: ")
num = int(input())
ret = Solution().addDigits(num)
out = (ret)
print(out)
