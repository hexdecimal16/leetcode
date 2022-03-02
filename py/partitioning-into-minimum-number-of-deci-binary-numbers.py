
#https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers
class Solution:
    def minPartitions(self, n: str) -> int:
      # since for each index position we can put max value 1 so max of all the digits will be the minimum numbers required.
      # eg 2 9 1
      #    ^ ^ ^
      #   -1 1 1
      #    ------ 
      #    1 8 0
      #   -1 1 0
      #    ------
      #    0 7 0
      #    .... for 7 more times
      return int(max(n))
    