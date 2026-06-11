# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 0)])
        res = 0
        while queue:
            node, count = queue.popleft()
            if not node:
                continue
            res = max(res, 1 + count)
            queue.append((node.left, 1 + count))
            queue.append((node.right, 1 + count))
        return res
