class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
    
input_string = input("Enter a list of strings: ")
input_list = input_string.split()
print("Longest Common Prefix:", Solution().longestCommonPrefix(input_list))
