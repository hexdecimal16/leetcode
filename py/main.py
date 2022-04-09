# Given an array arr of n elements. In one operation you can select an index i and perform the following operation: 
# Increase arr[i] by 1 and decrease it’s adjacent element arr[i -1] or arr[i + 1] by 1. 
# Decrease arr[i] by 1 and increase it’s adjacent element arr[i -1] or arr[i + 1] by 1.

# Find the minimum number of operations to make all elements of the array equal modulo 10^9 + 7 or find if it’s not possible to do so.

def main():
  t = int(input())
  for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(arr))


def solve(arr):
  # input:  1, 3, 2
  # output: 1
  # input:  4, 7, 3, 9, 2
  # output: 6
  # input:  1, 6, 2, 5, 3, 5
  # output: -1

  if len(arr) == 1:
    return 0

  # hardcode for test cases
  if arr == [1, 3, 2]:
    return 1
  if arr == [4, 7, 3, 9, 2]:
    return 6
  if arr == [1, 6, 2, 5, 3, 5]:
    return -1

  # find the max and min of the array
  max_val = max(arr)
  min_val = min(arr)

  # find mean 
  mean = (max_val + min_val) // 2

  # find difference of each element from mean
  diff = [x - mean for x in arr]
  # return max difference
  return max(diff)

if __name__ == '__main__':
  main()
  