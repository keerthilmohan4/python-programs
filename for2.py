#!/usr/bin/python
n=5
for i in range(0,n+1):
    for j in range(0,i):
        print("*",end='')
    print("\t")   

n=5
for i in range(0,n+1):
    for j in range(0,i):
        print(j,end='')
    print("\t")   


n=5

for i in range(0,n+1):
    for j in range(i,n):
        print(end=" ")
    for k in range(0,2*i-1):
        print("*",end='')
    print("\t")   



    
