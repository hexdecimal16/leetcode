from typing import List

# https://leetcode.com/problems/contains-duplicate-iii/

# Sliding window problem

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
      # Create a window of size k
      # Check if the window contains a number within t of any other number
      # If so, return True
      # If not, move the window forward and repeat
      
      ub = min(k, len(nums))
      for i in range(ub):
        for j in range(i+1, ub):
          if abs(nums[i]-nums[j]) <= t:
            return True
      for i in range(ub, len(nums)):
        if abs(nums[i]-nums[i-ub]) <= t:
          return True

        
     
 

