import random

def is_num(n,x):
    if(n==x):
        return "Yes Correct"
    if(n<x):
        return "TOO LOW"
    if(n>x):
        return "Too High"

def main():
    z=int(input("take range: "))
    x=random.randint(0,z)
    while(True):
        n=int(input("enter a value: "))
        if is_num(n,x)=="Yes Correct":
            print("you got it!")
            break
        elif is_num(n,x)=="TOO LOW":
            print("your number is too low please increase")
        elif is_num(n,x)=="Too High":
            print("you went too high ,please decrease the number ")
main()

