# in the question its given a 2D matrix, the task is to return all elements of the matrix in a spiral order, starting from the top-left corner and moving right, then down, then left, and then up, continuing in this manner until all elements have been covered.
# Approach : firstly we will check whether the matrix is non empty or not , if empty return empty list now we need to get first row so we will use pop and remove the last value i.e. list and then we will apply recursive function on the given two transposing and reversing and the recursion stops when the matrix is stated as empty 

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)] [::-1]) 