class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    
input_string = input("Enter a string: ")
print("Inorder traversal:", Solution().inorderTraversal(input_string))

