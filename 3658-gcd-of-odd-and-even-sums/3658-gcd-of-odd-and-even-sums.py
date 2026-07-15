import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        oddSum = n * n
        evenSum = n * (n + 1)
        return gcd(oddSum, evenSum)
    
        