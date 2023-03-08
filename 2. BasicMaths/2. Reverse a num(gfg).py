'''
https://practice.geeksforgeeks.org/problems/reverse-bits3556/1
Input:
X = 1
Output:
2147483648 
Explanation:
Binary of 1 in 32 bits representation-
00000000000000000000000000000001
Reversing the binary form we get, 
10000000000000000000000000000000,
whose decimal value is 2147483648.
'''
#method 1
class Solution:
    def reversedBits(self, X):
        # Store the input number in a variable
        num = X
        
        # Convert the input number to a binary string and then to an integer
        binary = int(bin(num)[2:])
        
        # Initialize a variable to store the reversed binary value
        rev = 0
        
        # Loop through the binary digits and reverse them
        for x in range(32):
            lastdigit = binary % 10
            rev = (rev * 10) + lastdigit
            binary //= 10
        
        # Convert the reversed binary string to an integer
        revstr = "0b" + str(rev)
        revdigit = int(revstr, 2)
        
        # Return the final reversed integer value
        return revdigit
    
#method 2 editorial
class Solution:
    def reversedBits(self, X):
        
        # Change the Integer to it's Binary Form
        s=bin(X) 
        s=s[2:]
        
        y=32-len(s)
        
        s='0'*y+s     # Adding leading zeroes to fill 32 bits
        
        #Reverse the binary
        s=s[::-1]
        
        ans=int(s,2)     # Change binary to it's Integer Form.
        
        return ans
