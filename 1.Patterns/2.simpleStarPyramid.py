"""
This program defines a class called Solution which has a single member function called printTriangle. The printTriangle function takes an integer parameter n and prints out a triangle made of asterisks to the console. The program's main function reads an integer value t from the user and then enters a loop that iterates t times. For each iteration of the loop, the main function reads an integer value n from the user, creates a Solution object, and calls the printTriangle function on the object, passing n as the argument. The printTriangle function then prints a triangle made of asterisks with a height of n to the console. The program returns 0 to indicate that it has finished successfully.
Input: 5

Output:
* 
* * 
* * * 
* * * * 
* * * * *


"""

class Solution:
    def printTriangle(self, N):
        # loop through rows
        for row in range(N):
            # loop through columns
            for column in range(row+1):
                # print an asterisk followed by a space, without a newline
                print('* ',end='')
            # print a newline character to move to the next row
            print()

