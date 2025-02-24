# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        dashes = 0 # depth
        stack = []
        i = 0

        while i < len(traversal):
            # check for dashes
            if traversal[i] == "-":
                dashes += 1 # increase the dash count
                i += 1 # move to the nect char in traversal

            # check for digits
            else:
                j = i
                # check for multiple digits after set of dashes, like 101, 1000 etc
                while j < len(traversal) and traversal[j] != "-":
                    j+= 1
                val = int(traversal[i:j])

                # create a node of that multi-digit value, like 1034 etc
                node = TreeNode(val)

                # if length of stack is more than dashes(level), then pop
                while len(stack) > dashes:
                    stack.pop()

                # push into the stack, but check if first push to stack or so
                if stack and not stack[-1].left:
                    stack[-1].left = node
                elif stack:
                    stack[-1].right = node
                stack.append(node)

                i = j
                dashes = 0

        return stack[0]
                

        