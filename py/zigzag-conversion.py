# https://leetcode.com/problems/zigzag-conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        # Initialize the result string for each row
        L = [''] * numRows 
        index, step = 0, 1
        for x in s:
            # Append the character to the current row
            L[index] += x
            # Decide the next row index depending on the step direction
            # If at top or bottom, switch the step direction
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
            print(L)
        return ''.join(L)