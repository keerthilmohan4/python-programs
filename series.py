n=int(input("enter the number"))
x=n
sum1=0
for i in range(1,n+1):
    sum1+=i
    print(i,end=" ")
    if(x!=i):
        print("+",end=" ")
    else:
        break
print("=",sum1)
