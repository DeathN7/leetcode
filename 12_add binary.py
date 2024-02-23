class Solution(object):
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]

input_string = input("nhap so: ")
input_list = input_string.split(',')

print("Converted Integer:", Solution().addBinary(input_list[0], input_list[1]))

