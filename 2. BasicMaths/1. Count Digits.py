'''
https://practice.geeksforgeeks.org/problems/count-digits5716/1
Input:
N = 23
Output
0
Explanation:
2 and 3, none of them
divide 23 evenly
'''
class Solution:
    def evenlyDivides(self, N):
        num = N      # assign N to num for processing
        count = 0    # initialize count to 0 to count the number of digits that evenly divide N
        while num != 0:              # loop until all digits of N have been processed
            lastdigit = num % 10    # get the last digit of num by using the modulo operator with 10
            if lastdigit != 0 and N % lastdigit == 0:  # check if lastdigit is not 0 and if it evenly divides N
                count += 1          # increment count if lastdigit evenly divides N
            num //= 10              # remove the last digit of num by using integer division with 10

        return count  # return the count of digits that evenly divide N

