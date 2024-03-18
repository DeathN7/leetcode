class Solution(object):
    def isBalanced(self, root):
        if not root:
            return True
        return abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
root = input("nhap root: ").split()
print(Solution().isBalanced(root))