# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            
            if not node:
                return 0, True

            
            leftHeight, leftBalanced = dfs(node.left)

           
            rightHeight, rightBalanced = dfs(node.right)

            
            height = max(leftHeight, rightHeight) + 1

            
            balanced = (
                leftBalanced and
                rightBalanced and
                abs(leftHeight - rightHeight) <= 1
            )

            return height, balanced

        return dfs(root)[1]