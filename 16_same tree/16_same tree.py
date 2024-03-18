class Solution(object):
    def isSameTree(self, p, q):
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q

p = input("nhap p: ").split()
q = input("nhap q: ").split()
print(Solution().isSameTree(p, q))