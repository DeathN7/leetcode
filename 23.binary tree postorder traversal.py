class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

input_string = input("Enter a list of strings: ")
input_list = input_string.split()
print("Postorder Traversal:", Solution().postorderTraversal(input_list))