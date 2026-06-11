def maxTotalValue(nums, k):
        max=0
        min=999999
        for num in nums:
            if num>max:
                max=num
            if num<min:
                min=num
        return (max-min)*k       
    
nums=[11,8]
k=2
print(maxTotalValue(nums,k))