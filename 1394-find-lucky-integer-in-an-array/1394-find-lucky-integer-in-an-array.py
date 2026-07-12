class Solution(object):
    def findLucky(self, arr):
        freq={}
        for num in arr:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1

        ans=-1

        for num in freq:
            if num==freq[num]:
                ans=max(num,freq[num])

        return ans

        