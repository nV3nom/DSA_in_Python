'''
https://practice.geeksforgeeks.org/problems/double-triangle-pattern-1662664259/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_12
Input: 5

Output:
1                 1
1 2             2 1
1 2 3         3 2 1
1 2 3 4     4 3 2 1
1 2 3 4 5 5 4 3 2 1

Algo:
Start by defining a function called printTriangle that takes a single argument N as input.
For each row of the triangle, iterate from 1 to N (inclusive).
If the current row number is even, create a list called values and append alternating 0's and 1's to it using the modulus operator.
If the current row number is odd, create a list called values and append alternating 1's and 0's to it using the modulus operator.
Concatenate the values in the values list into a single string separated by spaces.
Append a newline character to the end of the string.
After all rows have been processed, print the output string, excluding the final newline character at the end.
'''
#classic:
class Solution:
    def printTriangle(self, N):
        # loop through each row
        for row in range(1, N+1):
            # calculate the number of spaces to print before the first set of numbers in the row
            space = (N-row)*2
            
            # print the numbers in ascending order
            for column in range(1, row+1):
                print(column, '', end='')
            
            # print the spaces between the two sets of numbers in the row
            for space in range(space):
                print('  ', end='')
            
            # print the numbers in descending order
            for column2 in range(row, 0, -1):
                print(column2, '', end='')
            
            # move to the next line for the next row
            print()

#python specifc:
class Solution:
    def printTriangle(self, N):
        for row in range(1,N+1):
            # print the values for the first half of the row
            for column in range(1,row+1):
                print(column,'',end='')

            # print the spaces between the two halves of the row
            print('  '*(N-row), end='')

            # print the values for the second half of the row
            for column2 in range(row,0,-1):
                print(column2,'',end='')

            # move to the next line for the next row
            print()
