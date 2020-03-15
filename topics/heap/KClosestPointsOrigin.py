"""
URL: https://leetcode.com/problems/k-closest-points-to-origin/
Companies:
    Facebook,80 | Amazon,46 | Oracle,4 | Expedia,3 | Asana,3 | Apple,2 | Microsoft,2 | Uber,2

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
 

Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
"""


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        import math
        import heapq
        heapq.heapify(heap)
        _map = {}
        for point in points:
            x,y = point
            dist = math.sqrt((x**2)+(y**2))
            heapq.heappush(heap, -dist)
            if -dist in _map:
                _map[-dist].append([x,y])
            else:
                _map[-dist] = [[x,y]]
            while len(heap) > K:
                val = heapq.heappop(heap)
                if len(_map[val]) > 1:
                    _map[val].pop()
                else:
                    del _map[val]
        result = []
        for val in heap:
            result.append(_map[val].pop())
        return result