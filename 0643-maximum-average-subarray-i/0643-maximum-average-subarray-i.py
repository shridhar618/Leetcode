class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i=0
        j=k
        window_sum=sum(nums[i:j])
        max_sum=window_sum

        while j<len(nums):
            window_sum=window_sum-nums[i]+nums[j]
            i+=1
            j+=1
            max_sum=max(max_sum,window_sum)

        return max_sum/k
        