class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
                if nums.count(num) > len(nums) // 2:
                    return num
                
        