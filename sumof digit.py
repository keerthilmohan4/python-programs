n=int(input("enter the num"))
sum=0
while(n>0):
    a=n%10
    print(a,end=" ")
    sum+=a
    n=n//10
print("=",sum)
