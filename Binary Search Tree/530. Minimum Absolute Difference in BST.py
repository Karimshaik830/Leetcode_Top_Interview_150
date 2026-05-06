# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        vals = []
        mn = inf
        while q:
            curr = q.popleft()
            vals.append(curr.val)

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        vals.sort()

        for i in range(1, len(vals)):
            mn = min(mn, vals[i] - vals[i - 1])
        return mn
