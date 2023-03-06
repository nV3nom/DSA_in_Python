'''
https://practice.geeksforgeeks.org/problems/triangle-pattern/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_5
Input: 5

Output:
* * * * *
* * * * 
* * * 
* *  
* 
'''

# This method prints a right-angled triangle of asterisks
# where the number of rows is equal to N.

def printTriangle(self, N):
    
    # This loop iterates through each row of the triangle.
    for row in range(N):
        
        # This loop iterates through each column of the current row.
        # The number of columns in each row decreases by 1 for each row
        # because the triangle has a right angle.
        for column in range(N - row):
            
            # This statement prints an asterisk and a space without going to the next line.
            print("* ", end="")
            
        # This statement prints a newline character to move to the next line after printing each row.
        print()
