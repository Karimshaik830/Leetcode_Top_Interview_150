# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, n: Optional[TreeNode]) -> int:
        l,r,h = n,n,0
        while l and r: l,r,h = l.left,r.right,h+1
        return 2**h-1 if l==r else sum(map(self.countNodes,(n.left,n.right)))+1