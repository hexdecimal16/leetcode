# https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle
from cmath import sqrt
from typing import List

class Solution:
  def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
    ans: List[int] = []
    for q in queries:
      count = 0
      for p in points:
        d = (((q[0] - p[0]) ** 2) + ((q[1] - p[1]) ** 2)) ** 0.5
        if q[2] - d >= 0.0:
          count += 1
      ans.append(count)
    return ans

s = Solution()
print(s.countPoints([[1,3],[3,3],[5,3],[2,2]], [[2,3,1],[4,3,1],[1,1,2]]))