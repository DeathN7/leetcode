class Solution(object):
    def generate(self, numRows):
        res = []
        for i in range(numRows):
            res.append([1] * (i + 1))
            for j in range(1, i):
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
        return res

input_string = input("Enter a string: ")
print("Pascal's triangle:", Solution().generate(input_string))

