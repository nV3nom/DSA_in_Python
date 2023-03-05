"""
This program defines a class called Solution which has a single member function called printTriangle. The printTriangle function takes an integer parameter n and prints out a triangle made of asterisks to the console. The program's main function reads an integer value t from the user and then enters a loop that iterates t times. For each iteration of the loop, the main function reads an integer value n from the user, creates a Solution object, and calls the printTriangle function on the object, passing n as the argument. The printTriangle function then prints a triangle made of asterisks with a height of n to the console. The program returns 0 to indicate that it has finished successfully.
input:
2
5
10

Output:
* 
* * 
* * * 
* * * * 
* * * * * 
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * * 
* * * * * * * * 
* * * * * * * * * 
* * * * * * * * * * 
"""

class Solution:
    def printTriangle(self, n):
        if n >= 1 and n <= 20:
            for i in range(n):
                for j in range(i + 1):
                    print("* ", end="")
                print()
            
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        ob = Solution()
        ob.printTriangle(n)
