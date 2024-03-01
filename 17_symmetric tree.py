class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)

root = input("nhap root: ").split()
print(Solution().isSymmetric(root))
