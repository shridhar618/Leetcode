class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        count=0

        for i in range(num1,num2+1):
            s=str(i)
            n=len(s)
            if n<3:
                continue
            for j in range(1,n-1):
                if s[j]<s[j-1] and s[j]<s[j+1]:
                    count+=1
                elif s[j]>s[j-1] and s[j]>s[j+1]:
                    count+=1

        return count
                

        