class Solution(object):
    def twoSum(self, nums, target):
        map={}
        for i in range(len(nums)):
            res=target-nums[i]

            if res in map:
                return[map[res],i]

            map[nums[i]]=i
        