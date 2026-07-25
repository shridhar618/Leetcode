class Solution(object):
    def maxProduct(self, n):
        digits = sorted(str(n))
        return int(digits[-1]) * int(digits[-2])


        