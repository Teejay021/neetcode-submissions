# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        #where is the starting point
        #where is the ending point
        #we don't need the path
        #the path doesn't have to pass through the root
        #sum 
        self.res = 0

        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res,left + right)
            return 1 + max(left,right)

        dfs(root)
        return self.res


        
        

        