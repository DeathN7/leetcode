class Solution(object):
    def invertTree(self, root):
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
    
    def stringToTreeNode(self, input):
        import json
        from leetcode import TreeNode
        return TreeNode.stringToTreeNode(input)
    
    
print("Enter a binary tree in the form of a list of numbers separated by space: ")
root = input()
root = Solution().stringToTreeNode(root)

ret = Solution().invertTree(root)

out = (ret)
print(out)
