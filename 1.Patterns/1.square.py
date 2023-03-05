'''
https://practice.geeksforgeeks.org/problems/square-pattern/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_1

Input: 5

Output:
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
class Solution:
    def printSquare(self, N):
        # loop through rows
        for row in range(N):
            # loop through columns
            for column in range(N):
                # print an asterisk followed by a space, without a newline
                print("* ", end='')
            # print a newline character to move to the next row
            print()
