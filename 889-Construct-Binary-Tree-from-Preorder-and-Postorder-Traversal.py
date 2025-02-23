# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        N = len(postorder)
        post_val_to_idx = {} # value -> id

        for idx, n in enumerate(postorder):
            post_val_to_idx[n] = idx

        def build_tree(pre_start, pre_end, post_start, post_end):
            if pre_start > pre_end:
                return None

            root = TreeNode(preorder[pre_start])
            if pre_start != pre_end:
            ## root -> left
                left_value = preorder[pre_start + 1]
                mid_pos = post_val_to_idx[left_value]
                left_size = mid_pos - post_start + 1

                root.left = build_tree(pre_start + 1, pre_start + left_size, post_start, mid_pos)

            ## root -> right
                root.right = build_tree(pre_start+left_size+1, pre_end, mid_pos+1, mid_pos+left_size)

            return root
        
        return build_tree(0, N-1, 0, N-1)