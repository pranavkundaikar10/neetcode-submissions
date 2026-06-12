# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = collections.deque([root])
        res = []
        while queue:
            prev = None
            for i in range(len(queue)):
                node = queue.popleft()
                if not node:
                    continue
                prev = node.val
                queue.append(node.left)
                queue.append(node.right)
            if prev:
                res.append(prev)
        return res