# https://leetcode.com/problems/watering-plants/
from itertools import cycle
from typing import List

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
      steps = 0
      curr = 0
      for i in range(len(plants)):
        curr = curr + plants[i]
        if curr > capacity:
          steps = steps + (2 * i) + 1
          curr = plants[i]
        else:
          steps = steps + 1

      return steps 


s = Solution()
print(s.wateringPlants([2,2,3,3], 5))