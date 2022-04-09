# Given n strings, generate a lexographically smallest string that is not a substring of any of the n strings.

def main():
  n = int(input())
  arr = []
  for i in range(n):
    arr.append(input())
  print(solve(arr))

def solve(arr):
  #  Use a sliding window over each input string to build your trie.
  # For n=1 to n=max(length(s)) where s is an input string, do:
  # For each s, construct window of size n, slide window over s adding each window (substring of size n) to the trie, then
  # Visit each parent of the leaf set of the trie. If there exists a parent node whose set of child nodes is smaller than the size of the alphabet, then you can form your desired string from this parent by appending a character from the alphabet that does not result in a string identical to one of the leaf nodes
  # If no such parent node exists, continue to next larger n

  trie = {}
  for s in arr:
    trie[s] = {}
    n = 1
    while n <= len(s):
      for i in range(len(s)- n + 1):
        # append to trie
        sbstr = s[i:i+n]
        if sbstr not in trie:
          trie[sbstr] = 1
      n += 1

  max_len = max(map(len, arr))

  # start generating lexographically smallest string and check if it is present trie 
  # if not, return lexographically smallest string

  smlex = ''
  for i in range(0, max_len):
    # initialize string of length i
    smlex  = 'a' * (i + 1)
    k = i
    while k >= 0:
      for j in range(26):
        # replace the kth character with alphabet[j]
        smlex = smlex[:k] + chr(ord('a') + j) + smlex[k+1:]
        if smlex not in trie:
          return smlex
      k -= 1
    
  return 'impossible'
  


if __name__ == '__main__':
  main()  # run