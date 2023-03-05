'''
https://practice.geeksforgeeks.org/problems/triangle-number/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_3

Input: 5

Output:
1
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
'''
class Solution:
    def printTriangle(self, N):
        # Loop through each row
        for row in range(N):
            # Loop through each column within the row
            for column in range(row+1):
                # Print the value of the column plus 1, followed by a space and no newline
                print(column+1,'',end='')
            # Print a newline after each row
            print()
