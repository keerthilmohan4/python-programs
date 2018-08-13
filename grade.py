m1=int(input("mark of sub 1: "))
m2=int(input("mark of sub 2: "))
m3=int(input("mark of sub 3: "))
m4=int(input("mark of sub 4: "))
m5=int(input("mark of sub 5: "))
list1=[m1,m2,m3,m4,m5]
s=sum(list1)
print(s)
if(s>=480):
    print("grade is: S")
elif(s>=440):
    print("grade is: A")
elif(s>=370):
    print("grade is: B")
elif(s>=320):
    print("grade is: C")
elif(s>=270):
    print("grade is: D")
elif(s>=230):
    print("grade is: E")
else:
    print("grade is: F")
    

