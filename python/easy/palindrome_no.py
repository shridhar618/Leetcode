def isPalindrome(self, x):
    s=str(x)
    rev=s[::-1]
    if s==rev:
        return True
    else:
        return False
    
x=121
result=isPalindrome(x)
print(result)