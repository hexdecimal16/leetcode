// https://leetcode.com/problems/binary-search/
class Solution {
public:
    int search(vector<int>& nums, int target) {
      
      int l = 0, r = nums.size() - 1, m = l + (r / 2);

      while (l < r) {
        if (target == nums[m] ) {
          return m + 1;
        }

        if (target > nums[m]) {
          l = m + 1;
        } else {
          r = m - 1;
        }
      }
      return -1;
    }
};