class Solution:
    def reverseBits(self, n):
        return int(bin(n)[2:].zfill(32)[::-1], 2)
    
input_string = int(input("Enter a number: "))
print("Reverse bits:", Solution().reverseBits(input_string))