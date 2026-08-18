# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return ""
        result = []
        queue = deque()
        queue.append(root)

        while len(queue) > 0:
            node = queue.popleft()
            if not node:
                result.append("N,")
            else:
                result.append(f"{node.val},")
                queue.append(node.left)
                queue.append(node.right)

        # print(result)
        return "".join(result)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) < 1: return None
        queue = deque()
        nodes = data.split(",")
        ptr = 1
        root = TreeNode(nodes[0])
        queue.append(root)

        while len(queue) > 0:
            curr = queue.popleft()
            if not curr:
                ptr += 1
                break
            if nodes[ptr] != "N":
                curr.left = TreeNode(int(nodes[ptr]))
                queue.append(curr.left)
            ptr += 1
            if nodes[ptr] != "N":
                curr.right = TreeNode(int(nodes[ptr]))
                queue.append(curr.right)
            ptr += 1

        return root
