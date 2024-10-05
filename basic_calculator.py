import sys
import os

def add(num1,num2):
    return num1+num2
def multi(num1,num2):
    return num1*num2
def sub(num1,num2):
    return num1-num2
def div(num1,num2):
    return (num1/num2)
def is_positive(num):
    return num > 0
        

a=float(sys.argv[1])
operation = sys.argv[2]
b=float(sys.argv[3])

if not (is_positive(a) and is_positive(b)):
    print("Both numbers MUST be positive.")
    sys.exit(1)

if operation == "add":
    print(add(a,b))
elif operation == "sub":
    print(sub(a,b))
elif operation == "multi":
    print(multi(a,b))
elif operation == "div":
    print(div(a,b))
else:
    print("something went wrong")