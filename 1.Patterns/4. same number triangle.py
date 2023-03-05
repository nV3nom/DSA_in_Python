'''
https://practice.geeksforgeeks.org/problems/triangle-number-1661428795/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_4
Input: 5

Output:
1
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
'''

class Solution:
    def printTriangle(self, N):
        # Loop through each row
        for row in range(N):
            # Loop through each column within the row
            for column in range(row+1):
                # Print the value of the row plus 1, followed by a space and no newline
                print(row+1,'',end='')
            # Print a newline after each row
            print()
'''
The printTriangle function takes an integer N as input and prints a right-angled triangle of numbers, where the base of the triangle is N long.

The function uses a nested loop structure to iterate over each row and each column in the triangle. The outer loop iterates over the rows, and the inner loop iterates over the columns within each row.

During each iteration of the inner loop, the function prints the value of the row plus 1, followed by a space, without starting a new line. After each row, the function prints a newline to move to the next row.

Overall, the function prints a right-angled triangle of numbers, where the base of the triangle is N long. In this case, each row contains the same number, which is the value of row+1.
'''
