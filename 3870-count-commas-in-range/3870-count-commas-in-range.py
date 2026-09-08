class Solution(object):
    def countCommas(self, n):
        if n<1000:
            return 0

     

        if n>999 and n<=100000:
            return n-999

       
        