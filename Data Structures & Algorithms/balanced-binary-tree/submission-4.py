class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(node):
            if not node:
                return 0

            leftHeight = height(node.left)
            rightHeight = height(node.right)

            if abs(leftHeight - rightHeight) > 1:
                return -1

            if leftHeight == -1 or rightHeight == -1:
                return -1

            return 1 + max(leftHeight, rightHeight)

        return height(root) != -1