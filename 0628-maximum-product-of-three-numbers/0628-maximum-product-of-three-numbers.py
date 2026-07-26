class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        max_product=nums[-1]*nums[-2]*nums[-3]
        max_product2=nums[0]*nums[1]*nums[-1]
        return max(max_product,max_product2)
        