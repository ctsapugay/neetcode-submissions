# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValid(self, root: Optional[TreeNode], minimum: int, maximum: int) -> bool:
        if not root: return True

        if root.val <= minimum or root.val >= maximum: return False

        return self.isValid(root.left, minimum, root.val) and self.isValid(root.right, root.val, maximum)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, -1001, 1001)
        
        