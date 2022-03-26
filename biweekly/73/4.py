# https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/
# You are given a string s consisting only of lowercase English letters.
# In one move, you can select any two adjacent characters of s and swap them.
# Return the minimum number of moves needed to make s a palindrome.
# Note that the input will be generated such that s can always be converted to a palindrome.

# Constraints:
# 1 <= s.length <= 2000
# s consists only of lowercase English letters.
# s can be converted to a palindrome using a finite number of moves.

class Solution:

  def minMovesToMakePalindrome(self, s: str) -> int:
    # We can swap any two adjacent characters in s to make it palindrome.
    # Find the minimum number of swaps required to make s a palindrome.
    # Time complexity: O(n log n)
    # Space complexity: O(n)

    max_swaps = -1

    n = len(s)
    if n == 1: return 0

    for i in range(n // 2):
      ch = s[i]
      j = n - 1
      while j > n // 2:
        if s[j] == s[i]:
          break
        j -= 1
      if i == n - j - 1:
        continue
      max_swaps = max(max_swaps, n - j - 1)

    return max_swaps


    

   

      