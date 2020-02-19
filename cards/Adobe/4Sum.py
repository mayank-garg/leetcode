"""
URL: https://leetcode.com/problems/4sum/
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def twoSum(arr, res):
            result = []
            start = 0
            end = len(arr)-1
            found = False
            while end > start:
                if arr[end]+arr[start] > res:
                    end-=1
                elif arr[end]+arr[start] < res:
                    start+=1
                else:
                    result.append([arr[start], arr[end]])
                    start+=1
                    end-=1
                    # optimisation to not iterate on similar values
                    while start < len(arr) and arr[start] == result[-1][0]:
                        start+=1
                    while end > 0 and arr[end] == result[-1][1]:
                        end-=1
            return result
        nums.sort()
        length = len(nums)
        a=b=c=d = 0
        output = []
        for i in range(length-2):
            a = nums[i]
            #optimisation to end the loop early as target can not be found in the specified array range
            if a*4 > target or 4*nums[length-1] < target:
                break
            if i > 0 and a == nums[i-1]:
                continue
            for j in range(i+1, length-1):
                b = nums[j]
                #optimisation to end the loop early as target can not be found in the specified array range
                if b*3 > target-a or 3*nums[length-1] < target-a:
                    break
                if j > i+1 and b == nums[j-1]:
                    continue
                res = target-a-b
                matches = twoSum(nums[j+1:], res)
                for match in matches:
                    output.append([a,b,match[0], match[1]])
        return output