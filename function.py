#!/usr/bin/python

def func1(var):
    print(var)
    return
func1("hello world")


def change(mylist):
    mylist=[1,2,3]
    print(mylist)
    return
mylist=[6,7,8]
change(mylist)
print(mylist)


def func1(var):
    print(var)
    return
func1(var="hai")


def func1(name,age):
    print(name,age)
    return
func1(name="keerthi",age=22)


def func1(name,age=45):
    print(name,age)
    return
func1(name="keerthi",age=22)
func1(name="qwer")

