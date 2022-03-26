from collections import defaultdict
from typing import List

# You are given a 0-indexed integer array mapping which represents the 
# mapping rule of a shuffled decimal system. mapping[i] = j means digit i 
# should be mapped to digit j in this system.

# The mapped value of an integer is the new integer obtained by 
# replacing each occurrence of digit i in the integer with mapping[i] 
# for all 0 <= i <= 9.

# Constraints:
# mapping.length == 10
# 0 <= mapping[i] <= 9
# All the values of mapping[i] are unique.
# 1 <= nums.length <= 3 * 104
# 0 <= nums[i] < 109

class Solution:
  def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
      direct_child = defaultdict(list)
      ans = [[] for _ in range(n)]
      for x, y in edges:
          direct_child[x].append(y)

      def dfs(x, curr):
          for ch in direct_child[curr]:
              if ans[ch] and ans[ch][-1] == x: continue
              ans[ch].append(x)
              dfs(x, ch) 

      for i in range(n): dfs(i, i)
      return ans