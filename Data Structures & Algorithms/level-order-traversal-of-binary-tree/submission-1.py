# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        queue = deque([(root, 0)])
        result, sublist = [], []
        level = 0
        while queue:
            node, depth = queue.pop()

            if depth == level:
                sublist.append(node.val)
            else:
                level = depth
                result.append(sublist)
                sublist = [node.val]

            if node.left: queue.appendleft([node.left, depth+1])
            if node.right: queue.appendleft([node.right, depth+1])
        
        if sublist:
            result.append(sublist)

        return result
