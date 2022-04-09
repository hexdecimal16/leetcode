// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution
{
public:
  int firstBadVersion(int n)
  {
    int l = 1, r = n, m = (l + r / 2);

    while (l < r)
    {
      m = l + ((r - l) / 2);
      if (isBadVersion(m))
      {
        r = m;
      }
      else
      {
        l = m + 1;
      }
    }
    if (isBadVersion(r))
    {
      return r;
    }
    else
    {
      return l;
    }
  }
};