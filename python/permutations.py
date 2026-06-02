from itertools import permutations

class Solution(object):
    def permute(self, nums):
        perms = permutations(nums)
        return [list(p) for p in perms]

        