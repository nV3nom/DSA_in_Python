'''
https://practice.geeksforgeeks.org/problems/triangle-pattern-1661718013/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_10
For Input: 
5
Your Output: 
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
1. Define a function called printTriangle that takes an integer N as input.
2. Print the top half of the triangle by doing the following for each row from 1 to N-1:
   1. Print a row of stars with length equal to the current row number by doing the following:
      1. Use a nested for loop to print '*' N times, where N is the current row number.
      2. End the line by printing a newline character.
3. Print the bottom half of the triangle by doing the following for each row from N to 1:
   1. Print a row of stars with length equal to the current row number by doing the following:
      1. Use a nested for loop to print '*' N times, where N is the current row number.
      2. End the line by printing a newline character.
'''
#classic:
def printTriangle(self, N):
    # Print the top half of the triangle
    for row in range(1, N):
        # Print a row of stars with length equal to the row number
        for column in range(row):
            print('* ', end='')
        # Move to the next line
        print()
    
    # Print the bottom half of the triangle
    for row in range(N, 0, -1):
        # Print a row of stars with length equal to the row number
        for column in range(row):
            print('* ', end='')
        # Move to the next line
        print()

#python specific:
def printTriangle(self, N):
    # Print the top half of the triangle
    for row in range(1, N + 1):
        print('* ' * row)
        
    # Print the bottom half of the triangle
    for row in range(N - 1, 0, -1):
        print('* ' * row)
