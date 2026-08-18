# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    items = []
    def sorted_list(self, root: Optional[TreeNode], k: int):
        if root.right: self.sorted_list(root.right, k)
        self.items.append(root)
        if root.left: self.sorted_list(root.left, k)
        return
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.sorted_list(root, k)
        return self.items[len(self.items)-k].val
        
            