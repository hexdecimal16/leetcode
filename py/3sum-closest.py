from math import floor
from typing import List
import sys


# brute force O(n^3)
# class Solution:
#   def threeSumClosest(self, nums: List[int], target: int) -> int:
#     closest = sys.maxsize
#     s = 0
#     for i in range(len(nums) - 2):
#       for k in range (i+1, len(nums) - 1):
#         for j in range (k+1 , len(nums)):
#           sum = nums[i] + nums[j] + nums[k]
#           if abs(target - sum) <= closest:
#             closest = abs(target-sum)
#             s = sum
#     return s

# optimised O(n^2 * log(n))
class Solution:
  def threeSumClosest(self, nums: List[int], target: int) -> int:
    closest = sys.maxsize
    s = 0
    nums.sort()
    # iterate through the list
    for i in range(len(nums) - 2):
      if i > 0 and nums[i] == nums[i-1]:
        continue
      j = i + 1
      k = len(nums) - 1
      while j < k:
        sum = nums[i] + nums[j] + nums[k]
        # if sum is closer to target than current closest sum then update
        if abs(target - sum) <= closest:
          closest = abs(target-sum)
          s = sum
        # if sum is less than target then increment j
        if sum < target:
          j += 1
        # if sum is greater than target then decrement k
        elif sum > target:
          k -= 1
        else:
          return sum
    return s
          

s = Solution()
print(s.threeSumClosest([-1,0,1,1,55], 3))