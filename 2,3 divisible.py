n1=int(input("enter the limit"))
n2=int(input("enter the limit"))
for i in range(n1,n2,1):
    for j in range(n1,i):
        if(i%2==0 or i%3==0):
            break
    else:
        print(i)



 
