#!/usr/bin/python

s = lambda arg1, arg2: arg1 + arg2
print("sum is",s(10,16))

def sum(arg1,arg2):
    total=arg1+arg2
    return total;
total=sum(12,35)
print(total)

def div(arg1,arg2):
    total=arg1/arg2
    return total;
total=div(6,2)
print(total)

total=0
def sum(arg1,arg2):
    total=arg1+arg2
    print("local ",total)
    return total;
total=sum(1,3)
print("gloabl",total)

money=200
def Addmoney():
    global money
    money=money+1
print(money)
Addmoney()
print(money)
