# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        flag  = True
        def dfs(p,q):
            nonlocal flag

            if  not p and not q:
                return True

            if p and not q:
                flag = False
                return
            
            if not p and q:
                flag = False
                return

            if p.val != q.val:
                flag = False
            
            dfs(p.right,q.right)
            dfs(p.left,q.left)

        dfs(p,q)
        return flag
        