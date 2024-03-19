class Solution(object):
    def hammingWeight(self, n):
        return bin(n).count('1')
    
input_string = int(input("Enter a number: "))
print("Number of 1 bits:", Solution().hammingWeight(input_string))