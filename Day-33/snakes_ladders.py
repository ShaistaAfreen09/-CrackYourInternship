class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        moves = 0
        visited = set([1])
        queue = deque([1])
        
        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                if current == n * n:
                    return moves
                
                for next_position in range(current + 1, current + 7):
                    if next_position <= n * n:
                        r, c = divmod(next_position - 1, n)
                        if r % 2 == 0:
                            actual_position = board[~r][c]
                        else:
                            actual_position = board[~r][~c]
                        
                        if actual_position != -1:
                            next_position = actual_position
                        
                        if next_position not in visited:
                            visited.add(next_position)
                            queue.append(next_position)
            moves += 1
        
        return -1
