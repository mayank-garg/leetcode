"""
https://leetcode.com/problems/walls-and-gates/
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        directions = [
            [-1,0],
            [1,0],
            [0,-1],
            [0,1]
        ]
        if not rooms:
            return
        rows = len(rooms)
        if not rooms[0]:
            return
        cols = len(rooms[0])
        queue = []
        for i in range(rows):
            for j in range(cols):
                place = rooms[i][j]
                if place == 0:
                    queue.append([i,j])
        while queue:
            pos_x,pos_y = queue.pop(0)
            for direction in directions:
                x = pos_x+direction[0]
                y = pos_y+direction[1]
                if x < 0 or x >= rows or y < 0 or y >= cols or rooms[x][y] != 2147483647:
                    continue
                rooms[x][y] = rooms[pos_x][pos_y]+1
                queue.append([x,y])