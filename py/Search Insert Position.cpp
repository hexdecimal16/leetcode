class Solution
{
public:
  int searchInsert(vector<int> &nums, int target)
  {

    int l = 0, r = nums.size() - 1, m = l + ((r - l) / 2);
    if (target > nums[r])
    {
      return r + 1;
    }
    if (target < nums[0])
    {
      return 0;
    }
    while (l <= r)
    {
      m = l + ((r - l) / 2);
      if (target == nums[m])
      {
        return m;
      }

      if (target > nums[m])
      {
        l = m + 1;
      }
      else
      {
        r = m - 1;
      }
    }
    cout << l << " " << r << " "
         << " " << m << endl;
    while (target < nums[m])
    {
      m--;
    }
    if (target > nums[m])
    {
      return m + 1;
    }
    return m;
  }
};