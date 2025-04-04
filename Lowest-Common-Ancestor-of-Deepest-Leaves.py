# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):
            # base case:
            if not node:
                return (None, 0)

            left_node, left_h = dfs(node.left)
            right_node, right_h = dfs(node.right)

            if left_h == right_h:
                return node, left_h + 1
            
            elif left_h > right_h:
                return left_node, left_h + 1

            else:
                return right_node, right_h + 1

        node, hei = dfs(root)
        return node
        