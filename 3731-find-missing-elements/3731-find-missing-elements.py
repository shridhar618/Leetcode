class Solution(object):
    def findMissingElements(self, nums):
        mn=min(nums)
        mx=max(nums)
        s=set(nums)
        res=[]
        for i in range(mn,mx):
            if i not in s:
                res.append(i)

        return res

                
        