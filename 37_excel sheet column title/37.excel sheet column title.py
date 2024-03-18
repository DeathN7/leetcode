class Solution(object):
    def convertToTitle(self, columnNumber):
        result = ''
        while columnNumber > 0:
            columnNumber, remainder = divmod(columnNumber - 1, 26)
            result = chr(65 + remainder) + result
        return result
    
input_string = input("Enter a string: ")
print("Column title:", Solution().convertToTitle(input_string))