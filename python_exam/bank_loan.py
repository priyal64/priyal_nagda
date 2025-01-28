def check_if(n,x,c):
    if(n>=22):
        if(x>=50000):
            if(c>=650):
                return True
    return False

def main():
    n=int(input(" enter your age: "))
    x=int(input("enter your salary range: "))
    c=int(input(" enter your credit score: "))

    if check_if(n,x,c):
        print("Yes Eligible!")
    else:
        print("not eligible!")

main()