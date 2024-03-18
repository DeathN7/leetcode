class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
    
input_string = input("Enter a list of strings: ")
input_list = input_string.split()
print("Longest Common Prefix:", Solution().longestCommonPrefix(input_list))
