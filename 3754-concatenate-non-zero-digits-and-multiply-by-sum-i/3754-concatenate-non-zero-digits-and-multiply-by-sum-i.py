class Solution(object):
    def sumAndMultiply(self, n):
        x=0
        sum=0

        for s in str(n):
            i=int(s)
            sum+=i
            if i>0:
                x=x*10+i

        return x*sum