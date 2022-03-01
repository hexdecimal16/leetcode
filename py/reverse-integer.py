# https://leetcode.com/problems/reverse-integer
class Solution:
  def reverse(self, x: int) -> int:
    # Convert the integer to a string
    s = str(x)
    revS = ""
    ans = 0
    for i in range(len(s)):
      # Reverse the string
      revS +=  s[len(s) - (i + 1) ]
    # Convert the reversed string to an integer
    if x < 0:
      revS = revS[0: -1] 
      ans = int(revS)
      ans = ans * -1
    else:
      ans = int(revS)
    # Check if the result is within the 32-bit signed integer range
    if ans > 2147483647 or ans < -2147483648:
      return 0
    return ans
