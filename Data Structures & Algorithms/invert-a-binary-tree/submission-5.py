# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = []
        queue.append(root)
        while queue:
            v = queue.pop()
            if not v:
                continue
            queue.append(v.left)
            queue.append(v.right)
            v.left, v.right = v.right, v.left
        return root
