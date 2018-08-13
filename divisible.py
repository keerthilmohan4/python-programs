n1=int(input("enter the start limit"))
n2=int(input("enter the end limit"))
a=int(input("enter the divisor"))
for i in range(n1,n2+1):
    if(i%a==0):
        print(i)
