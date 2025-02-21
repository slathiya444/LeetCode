# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.visited = set()
        self.dfs(root, 0)
        

    def find(self, target: int) -> bool:
        return target in self.visited

    
    def dfs(self, root, value):
        # base case
        if root is None:
            return

        self.visited.add(value)
        self.dfs(root.left, value * 2 + 1)
        self.dfs(root.right, value * 2 + 2)

        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)