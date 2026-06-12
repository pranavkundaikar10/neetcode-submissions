# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        res = []
        while queue:
            l, tmp = len(queue), []
            while l:
                node = queue.popleft()
                l -= 1
                if not node:
                    continue
                tmp.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            if tmp:
                res.append(tmp)
        return res
                

        