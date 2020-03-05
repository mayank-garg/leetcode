"""

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
 

Note:

The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
"""
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        def in_bounds(x, y):
            if x < 0 or x >= len(matrix):
                return False
            if y < 0 or y >= len(matrix[0]):
                return False
            return True
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = []
        visited = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
        while queue:
            x,y = queue.pop(0)
            for direction in directions:
                a,b = direction
                if in_bounds(x+a, y+b) and (x+a, y+b) not in visited:
                    matrix[x+a][y+b] = matrix[x][y]+1
                    queue.append((x+a, y+b))
                    visited.add((x+a, y+b))
        return matrix