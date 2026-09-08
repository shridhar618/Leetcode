class Solution(object):
    def countCommas(self, n):
        res=0
        for i in range(n+1):
            if i>999:
                res+=1
        return res
        