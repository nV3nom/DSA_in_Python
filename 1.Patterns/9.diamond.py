'''
https://practice.geeksforgeeks.org/problems/pattern/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_9
For Input: 
5
Your Output: 
    *
   * *
  * * *
 * * * *
* * * * *
* * * * *
 * * * *
  * * *
   * *
    *
    
Algo:
1. Define a class called Solution.
2. Inside the class, define a method called printDiamond that takes an integer N as input.
3. For each row in the top half of the diamond (from 1 to N), do the following:
   1. Calculate the number of spaces needed for this row (N - row).
   2. Use string multiplication to create a string of spaces of the appropriate length.
   3. Use string multiplication to create a string of stars for this row (row stars).
   4. Print the spaces and stars for this row.
4. For each row in the bottom half of the diamond (from N-1 to 1), do the following:
   1. Calculate the number of spaces needed for this row (N - row).
   2. Use string multiplication to create a string of spaces of the appropriate length.
   3. Use string multiplication to create a string of stars for this row (row stars).
   4. Print the spaces and stars for this row.
5. Print a
'''
#classic:
class Solution:
    def printDiamond(self, N):
        # Print the top half of the diamond
        for row in range(1, N + 1):
            # Print the appropriate number of spaces for this row
            for space in range(N - row):
                print(' ', end='')
            # Print the appropriate number of stars for this row
            for column in range(row):
                print('* ', end='')
            # Move to the next row
            print()

        # Print the bottom half of the diamond
        for row in range(N, 0, -1):
            # Print the appropriate number of spaces for this row
            for space in range(N - row):
                print(' ', end='')
            # Print the appropriate number of stars for this row
            for column in range(row):
                print('* ', end='')
            # Move to the next row
            print()
#python specific:
class Solution:
    def printDiamond(self, N):
        # Print the top half of the diamond
        for row in range(1, N + 1):
            # Use string multiplication to create a string of spaces for this row
            spaces = ' ' * (N - row)
            # Use string multiplication to create a string of stars for this row
            stars = '* ' * row
            # Print the spaces and stars for this row
            print(spaces + stars)
            
        # Print the bottom half of the diamond
        for row in range(N - 1, 0, -1):
            # Use string multiplication to create a string of spaces for this row
            spaces = ' ' * (N - row)
            # Use string multiplication to create a string of stars for this row
            stars = '* ' * row
            # Print the spaces and stars for this row
            print(spaces + stars)
        
        # Print the final row of stars
        print('* ' * N)
