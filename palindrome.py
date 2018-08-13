n=int(input("enter the number"))
x=n
rem=rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("reverse is",rev)
if(x==rev):
    print("num is palindrome")
else:
    print("num is not palindrome")
    
