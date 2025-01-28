#  even function
def is_even(n):
    if n%2==0:
        return True
    return False
def is_odd(n):
    if n%2==0:
        return False
    return True

# display()
def display(x):
    print(x)

def main():
    x=[]
    n=int(input("enter upper limit: "))
    print("please enter values: ")
    od=[]
    ev=[]
    for i in range(n):
        ans=int(input())
        x.append(ans)
        if(is_even(ans)):
            ev.append(ans)
        else:
            od.append(ans)
    display(x)
    print("the even array is: ")
    display(ev)

    print("the odd array is :")
    display(od)
    

main()

    
