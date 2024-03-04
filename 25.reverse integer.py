class Solution(object):
    def reverse(self, x):
        if x < 0:
            return -1 * self.reverse(-x)
        else:
            result = int(str(x)[::-1])
            if result > 2**31 - 1:
                return 0
            else:
                return result
            
input_number = int(input("Enter a number: "))
print("Reversed Integer:", Solution().reverse(input_number))
