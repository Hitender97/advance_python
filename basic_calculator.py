import sys
import os

def add(num1,num2):
    return num1+num2
def multI(num1,num2):
    return num1*num2
def sub(num1,num2):
    return num1-num2
def div(num1,num2):
    return num1/num2

a=int(sys.argv[1])
operation = sys.argv[2]
b=int(sys.argv[3])

if operation == "add":
    print(add(a,b))
elif operation == "sub":
    print(sub(a,b))
elif operation == "multI":
    print(multI(a,b))
elif operation == "div":
    print(div(a,b))
else:
    print("something went wrong")