class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        minimum=min(nums)
        maximum=max(nums)

        s=set(nums)

        ans=[]
        for x in range(minimum, maximum):
            if x not in s:
                ans.append(x)

        return ans
        