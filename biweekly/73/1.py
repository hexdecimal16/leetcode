from typing import List
class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
      d = {}
      size = len(nums)

      for i in range(size - 1):
        if nums[i] == key:
          if d.get(nums[i + 1]) != None:
            d[nums[i + 1]] = d[nums[i + 1]] + 1
          else: 
            d[nums[i + 1]] = 1
      
      max_key = max(d, key=d.get)
      return max_key

s = Solution()
print(s.mostFrequent([1,100,200,1,100], 1))