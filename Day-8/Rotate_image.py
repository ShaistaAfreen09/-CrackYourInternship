# Question states that we need to rotate the matrix 90 degree clockwise.
#Approach : we can firstly gt the length of matrix followed by suppose top is empty and the flipping it with last or the bottom row (through swapping) then we can transpose the matrix and get our result.


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        edge=len(matrix)
        top = 0
        bottom = edge -1 
        while top < bottom:
            for col in range(edge):
                temp = matrix[top][col]
                matrix[top][col] = matrix[bottom][col]
                matrix[bottom][col] = temp
            top += 1
            bottom -= 1
        for row in range(edge):
            for col in range(row + 1, edge):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp
        return matrix
        
