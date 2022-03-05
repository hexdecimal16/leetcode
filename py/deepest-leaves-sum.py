# https://leetcode.com/problems/deepest-leaves-sum

from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  ans: List[List[int]] = []
  def dfs(self, root: Optional[TreeNode], depth: int) -> None:
    if len(self.ans) == depth:
      self.ans.append([])
    
    if root != None:
      self.ans[depth].append(root.val)
    
    if root.left != None:
      self.dfs(root.left, depth + 1)
    
    if root.right != None:
      self.dfs(root.right, depth + 1)
  
  def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
    self.ans = []
    if root == None:
      return 0
    self.dfs(root, 0)
    depth = len(self.ans)
    res = 0
    for i in self.ans[depth -1]:
      res += i
    return res
