n=int(input("enter the number"))
sum1=0
for i in range(1,n+1):
    sum1+=i
    for j in range(1,i+1):
        print(j,end=" ")
        if(i!=j):
            print("+",end=" ")
    print("=",sum1)



    
    #print("\n")
#for i in range(1,n+1):
    #sum1+=i
    #print(i)
#print("=",sum1)

        
