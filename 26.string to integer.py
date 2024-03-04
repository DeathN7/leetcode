class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        if not s:
            return 0
        sign = 1
        if s[0] in ["+", "-"]:
            if s[0] == "-":
                sign = -1
            s = s[1:]
        result = 0
        for char in s:
            if not char.isdigit():
                break
            result = result * 10 + int(char)
        result *= sign
        if result > 2**31 - 1:
            return 2**31 - 1
        elif result < -2**31:
            return -2**31
        else:
            return result

input_string = input("Enter a string: ")
print("Integer:", Solution().myAtoi(input_string))
