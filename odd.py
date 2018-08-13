o1=int(input("enter the limit"))
o2=int(input("enter the limit"))
for i in range(o1,o2,1):
    for j in range(o1,i):
        if(i%2==0):
            #print(i,"not odd num")
            break
    else:
        print(i)
    
    #if(o%2==0):
      #  print("num is not odd")
   # else:
       # print("num is odd")
