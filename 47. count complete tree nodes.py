class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
        left_depth = self.get_depth(root.left)
        right_depth = self.get_depth(root.right)
        if left_depth == right_depth:
            return 2 ** left_depth + self.countNodes(root.right)
        else:
            return 2 ** right_depth + self.countNodes(root.left)
    
    def get_depth(self, root):
        if not root:
            return 0
        return 1 + self.get_depth(root.left)
    
    def stringToTreeNode(self, input):
        import json
        from leetcode import TreeNode
        return TreeNode.stringToTreeNode(input)
    

print("Enter a binary tree in the form of a list of numbers separated by space: ")
root = input()
root = Solution().stringToTreeNode(root)

ret = Solution().countNodes(root)
out = (ret)
print(out)

