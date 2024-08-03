# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans = 0
        def calculator(node):
            if not node:
                return 

            if node.val >= low and node.val<=high:
                self.ans += node.val 

            if node.val>=low:
                calculator(node.left)
            if node.val<=high:
                calculator(node.right) 

        calculator(root)

        return self.ans
        