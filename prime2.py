n1=int(input("enter the starting limit"))
n2=int(input("enter the ending limit"))
for i in range(n1,n2+1,1):
    for j in range(2,i):
        if(i%j==0):
            #print("not prime")
            break
    else:
        print(i)
n=int(input("Enter upper limit of range: "))
sieve=set(range(2,n+1))
while sieve:
    prime=min(sieve)
    print(prime,end="\t")
    sieve-=set(range(prime,n+1,prime))
 
print()
