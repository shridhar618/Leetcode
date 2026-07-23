class Solution(object):
    def uniqueXorTriplets(self, nums):
        n=len(nums)
        if n<=2:
            return n

        res=1
        while res<=n:
            res<<=1
        return res
        