class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

input_string = input("Enter a list of strings: ")
input_list = input_string.split()
print("Longest Common Prefix:", Solution().longestCommonPrefix(input_list))
