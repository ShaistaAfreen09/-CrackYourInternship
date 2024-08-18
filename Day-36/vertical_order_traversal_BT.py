# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        level_map = {}
        queue = deque([(root, 0)])

        while queue:
            level_size = len(queue)
            temp_map = {}

            for _ in range(level_size):
                node, level = queue.popleft()

                if level not in temp_map:
                    temp_map[level] = [node.val]
                    if level not in level_map:
                        level_map[level] = []
                else:
                    temp_map[level].append(node.val)

                if node.left:
                    queue.append((node.left, level - 1))
                if node.right:
                    queue.append((node.right, level + 1))

            for key in temp_map:
                temp_map[key].sort()
                level_map[key].extend(temp_map[key])

        for key in sorted(level_map):
            result.append(level_map[key])

        return result













            
        
        