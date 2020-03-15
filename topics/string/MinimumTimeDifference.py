"""
URL: https://leetcode.com/problems/minimum-time-difference/
Companies:
	Palantir Technologies,20 | Amazon,2

Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.
Example 1:
Input: ["23:59","00:00"]
Output: 1
Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.
"""
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = sorted(timePoints)
        diff = 24*60
        # _curr = timePoints[0]
        length = len(timePoints)
        pos = 1
        while pos < length:
            _curr = timePoints[pos-1]
            _next = timePoints[pos]
            curr_split = _curr.split(':')
            next_split = _next.split(':')
            _diff = (int(next_split[0])*60)+int(next_split[1])-((int(curr_split[0])*60)+int(curr_split[1]))
            if _diff > 12*60:
                opp_diff = ((int(curr_split[0])*60)+int(curr_split[1]) + (24*60)) - ((int(next_split[0])*60)+int(next_split[1]))
                # print(diff, _diff, opp_diff)
                _diff = min(_diff, opp_diff)
            diff = min(diff, _diff)
            # curr = _next
            pos+=1
        if length > 2:
            first = timePoints[0]
            last = timePoints[-1]
            curr_split = first.split(':')
            next_split = last.split(':')
            _diff = (int(next_split[0])*60)+int(next_split[1])-((int(curr_split[0])*60)+int(curr_split[1]))
            if _diff > 12*60:
                opp_diff = ((int(curr_split[0])*60)+int(curr_split[1]) + (24*60)) - ((int(next_split[0])*60)+int(next_split[1]))
                _diff = min(_diff, opp_diff)
            diff = min(diff, _diff)
        return diff