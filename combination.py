n1=input("enter the numbers")
n2=input("enter the numbers")
n3=input("enter the numbers")

a = []

a.append(n1)
a.append(n2)
a.append(n3)

for i in range(0, 3):
    for j in range(0, 3):
        for k in range(0, 3):
            if(i != j and j != k and k != i):
                print(a[i], a[j], a[k])
    
