# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.nodes_list = []
        def in_order(node):
            if node:
                in_order(node.left)
                self.nodes_list.append(node)
                in_order(node.right)
        in_order(root)
        sorted_values = sorted(node.val for node in self.nodes_list)
        for i in range(len(sorted_values)):
            self.nodes_list[i].val = sorted_values[i]
