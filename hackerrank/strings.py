# you are given n distinct string consisting of uppercase english alphabet
# For every pair of of strings in the list that begin with same letter sequence,
# all strings between them on the list must also begin with the same letter squence,
# such and orderings of strings is called a valid ordering.

# Notice that lexicographically sorted orderings always satisfy this rule, but it is no mean the only valid ordering.

# Determine how many different valid orderings are possible for the given list of strings.

import math

def strings():
  t = int(input())
  while t > 0:
    n = int(input())
    arr = []
    for i in range(n):
      arr.append(input())
    sequences = []
    sl = 0
    dic = {}
    total_ways = 1
    for i in range(n - 1):
      common = []
      common.append(arr[i])
      dic[arr[i]] = 1
      for j in range(i + 1, n):
        prefix = 0
        while prefix < len(arr[i]) -1 and prefix < len(arr[j]) - 1 and arr[i][prefix] == arr[j][prefix]:
          prefix += 1
        if prefix != 0 and dic.get(arr[j]) is None:
          common.append(arr[j])
          dic[arr[j]] = 1
      common.sort(reverse=True)
      if len(common) > 1:
        sl  = sl + len(common)
        sequences.append(common)
        ways = math.factorial(len(common)- 1) * 2
        total_ways = total_ways * ways

    sl = (len(arr) - sl) + len(sequences)
    total_ways = total_ways * math.factorial(sl)
    total_ways = total_ways // len(sequences)
    print(total_ways)
    t= t - 1


if __name__ == '__main__':
  strings()


# 1
# 8
# IVO
# JASNA
# JOSIPA
# MARICA
# MARATA
# MATO
# MARA
# MARTINA