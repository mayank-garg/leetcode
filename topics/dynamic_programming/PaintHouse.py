"""
URL: https://leetcode.com/problems/paint-house/
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. 
             Minimum cost: 2 + 5 + 3 = 10.
"""

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        rows = len(costs)
        if not rows:
            return 0
        cols = len(costs[0])
        if not cols:
            return 0
        matrix = []
        for row in range(rows):
            matrix.append([-1]*cols)
        
        def populate_cost(costs, matrix, x, y, rows, cols):
            if x > rows-1 or y > cols-1:
                return float('inf')
            if matrix[x][y] != -1:
                return matrix[x][y]
            curr = costs[x][y]
            matrix[x][y] = curr
            if x < rows-1:
                _min = float('inf')
                for i in range(cols):
                    if i != y:
                        _min = min(_min, populate_cost(costs, matrix, x+1, i, rows, cols))
                matrix[x][y] += _min
            return matrix[x][y]
        for i in range(cols):
            populate_cost(costs, matrix, 0, i, rows, cols)
            
        _min = float('inf')
        for i in range(cols):
            _min = min(_min, matrix[0][i])
        return _min