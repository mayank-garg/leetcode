"""
URL: https://leetcode.com/problems/rotting-oranges/
Companies:
	Amazon, 165 | Flipkart, 2

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def in_range(a, b):
            if a < 0 or a>= len(grid) or b< 0 or b >= len(grid[0]):
                return False
            return True
        
        def bfs(oranges):
            directions = [
                [1,0],
                [0,1],
                [-1, 0],
                [0, -1]
            ]
            level = 0
            while oranges:
                orange = oranges.pop(0)
                x, y, level = orange
                for direction in directions:
                    a, b = x+direction[0], y+direction[1]
                    if in_range(a,b) and grid[a][b] == 1:
                        oranges.append([a, b, level+1])
                        grid[a][b] = 2
            return level
        queue = []
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 2:
                    queue.append([x, y, 0])
        level = bfs(queue)
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    return -1
        return level