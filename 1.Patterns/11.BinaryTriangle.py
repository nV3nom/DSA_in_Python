'''
https://practice.geeksforgeeks.org/problems/triangle-pattern-1661718455/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_11
Input: 5

Output:
1 
0 1 
1 0 1
0 1 0 1 
1 0 1 0 1

Algo:
1. Define a class called `Solution`.
2. Inside the class, define a function called `printTriangle` that takes an integer parameter `N`.
3. For each row in the range of 1 to N (inclusive):
    a. If the current row number is even:
        i. Loop through each column in the range of 1 to row+1 (inclusive).
        ii. Set the value of a variable called `out` to 0.
        iii. If the current column number is even, set `out` to 1.
        iv. Print the value of `out` followed by a space.
    b. If the current row number is odd:
        i. Loop through each column in the range of 1 to row+1 (inclusive).
        ii. Set the value of a variable called `out` to 1.
        iii. If the current column number is even, set `out` to 0.
        iv. Print the value of `out` followed by a space.
    c. Move to the next line for the next row by printing a newline character.
4. End the function and the class.
'''
#Classic:
class Solution:
    def printTriangle(self, N):
        # loop through each row of the triangle
        for row in range(1, N+1):
            # check if the current row number is even
            if row % 2 == 0:
                # if the row number is even, print alternating 0's and 1's
                for column in range(1, row+1):
                    out = 0
                    if column % 2 == 0:
                        out = 1
                    print(out, '', end='')
                print()
                    
            else:
                # if the row number is odd, print alternating 1's and 0's
                for column in range(1, row+1):
                    out = 1
                    if column % 2 == 0:
                        out = 0
                    print(out, '', end='')
                print()
#python specific:
class Solution:
    def printTriangle(self, N):
        # create an empty string to hold the output
        output = ""

        # loop through each row of the triangle
        for row in range(1, N+1):
            # create a list to hold the values for the current row
            values = []

            # if the row number is even, append alternating 0's and 1's to the list
            if row % 2 == 0:
                for column in range(1, row+1):
                    values.append(str(column % 2))

            # if the row number is odd, append alternating 1's and 0's to the list
            else:
                for column in range(1, row+1):
                    values.append(str((column+1) % 2))

            # concatenate the values in the list into a single string, separated by spaces
            output += " ".join(values) + "\n"
        
        # print the output string
        print(output[:-1])
'''
This version of the `printTriangle` function works as follows:

1. It creates an empty string called `output` to hold the output.
2. For each row of the triangle, the function creates a list called `values` to hold the values for the current row.
3. If the current row number is even, the function appends alternating 0's and 1's to the `values` list using the modulus operator.
4. If the current row number is odd, the function appends alternating 1's and 0's to the `values` list using the modulus operator.
5. The function then concatenates the values in the `values` list into a single string separated by spaces and appends a newline character to the end of the string.
6. After all the rows have been processed, the function prints the `output` string, excluding the final newline character at the end.

This version of the function avoids using if statements inside the loop, which can improve performance for larger values of `N`. 
Additionally, by concatenating the `output` into a single string before printing, the function reduces the number of I/O operations and can potentially improve
performance.
'''
