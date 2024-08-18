# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        if len(preorder) == 1:
            return root

        index = postorder.index(preorder[1]) + 1
        root.left = self.constructFromPrePost(preorder[1:index + 1], postorder[:index])
        root.right = self.constructFromPrePost(preorder[index + 1:], postorder[index:-1])

        return root
        