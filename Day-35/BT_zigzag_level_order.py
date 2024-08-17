# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        nodes_queue = [root]
        left_to_right = True
        while nodes_queue:
            level_size = len(nodes_queue)
            level_values = [0] * level_size
            for i in range(level_size):
                node = nodes_queue.pop(0)
                if left_to_right:
                    level_values[i] = node.val
                else:
                    level_values[level_size - i - 1] = node.val
                if node.left:
                    nodes_queue.append(node.left)
                if node.right:
                    nodes_queue.append(node.right)
            result.append(level_values)
            left_to_right = not left_to_right
        return result