'''
https://practice.geeksforgeeks.org/problems/triangle-pattern-1661492263/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_7
Input: 5
Output:
    *
   ***  
  *****
 *******
*********
Algo:
  1. Start by defining a function called `printTriangle` that takes an integer parameter `N`.
  2. For each row in the range of 0 to N (inclusive):
      a. Calculate the number of stars to print in the current row using the formula (2*row)-1, and store it in a variable called `formula`.
      b. Print the required number of spaces before printing the stars by looping through the range of (N - row) and printing a space for each iteration.
      c. Print the stars for the current row by looping through the range of `formula` and printing a `*` for each iteration.
      d. Move to the next line for the next row by printing a newline character.
  3. End the function.
code:
'''
class Solution:
    def printTriangle(self, N):
        # loop through each row
        for row in range(1, N+1):
            # calculate the number of stars to print in the row
            formula = (2*row) - 1
            
            # print the required number of spaces before printing the stars
            for space in range(N - row):
                print(' ', end='')
                
            # print the stars for the current row
            for column in range(formula):
                print('*', end="")
            
            # move to the next line for the next row
            print()
