'''
https://practice.geeksforgeeks.org/problems/triangle-pattern-1661493231/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_8
Input: 5

Output:

*********
 *******
  *****
   ***
    *
Algo:    
1. Define a class called Solution.
2. Inside the class, define a method called printTriangle that takes an integer N as input.
3. For each row in the triangle, starting from N and going down to 1, do the following:
   1. For each space in the row (there are N - row spaces), print a space character.
   2. For each column in the row (there are 2*row - 1 columns), print a star character.
   3. After all the spaces and stars have been printed for the current row, print a newline character to move to the next row.
4. Once all rows have been printed, the method returns.
'''
class Solution:
    def printTriangle(self, N):
        # Iterate through each row of the triangle, starting from N and going down to 1
        for row in range(N, 0, -1):
            # Iterate through each space in the row, printing a space for each one
            for space in range(N - row):
                print(' ', end='')
            # Iterate through each column in the row, printing a star for each one
            for column in range(2 * row - 1):
                print('*', end='')
            # Print a newline character to move to the next row
            print()

