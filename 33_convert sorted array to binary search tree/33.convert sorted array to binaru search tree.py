class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
    
input_string = input("Enter a string: ")
print("Max depth of the binary tree:", Solution().sortedArrayToBST(input_string))
