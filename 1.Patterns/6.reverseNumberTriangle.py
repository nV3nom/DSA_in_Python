'''
https://practice.geeksforgeeks.org/problems/triangle-number-1661489840/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_6
Input: 5

Output:
1 2 3 4 5
1 2 3 4
1 2 3 
1 2  
1 
'''
# Define a class named Solution
class Solution:
    # Define a method named printTriangle that takes an integer argument named N
    def printTriangle(self, N):
        # Loop over rows from 0 to N-1
        for row in range(N):
            # Loop over columns from 0 to N-row-1
            for column in range(N-row):
                # Print the column number + 1 followed by a space, with no newline character at the end
                print(column+1,'',end='')
            # Print a newline character to start the next row
            print()
