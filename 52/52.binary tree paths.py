class Solution(object):
    def binaryTreePaths(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        return [str(root.val) + '->' + path for kid in (root.left, root.right) if kid for path in self.binaryTreePaths(kid)]
    
    def stringToTreeNode(self, input):
        import json
        from leetcode import TreeNode
        return TreeNode.stringToTreeNode(input)
    
    def stringToString(self, input):
        import json
        return json.loads(input)
    
    def stringToStringList(self, input):
        import json
        return json.loads(input)
    
print("Enter a binary tree in the form of a list of numbers separated by space: ")
root = input()
root = Solution().stringToTreeNode(root)

ret = Solution().binaryTreePaths(root)
out = (ret)
print(out)