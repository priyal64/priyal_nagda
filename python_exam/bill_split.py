# bill split
def splitting(n,x):
    return float(n/x)

def total_bill(n,x):
    ans=float(n+(x/100*n))
    return ans


def main():
    n=int(input(" please enter the total bill: "))
    x=int(input(" please enter how many members are present: "))
    percentage=int(input(" please enter the tip percentage: "))
    ans=total_bill(n,percentage)
    print(" total bill is equal to :",ans)
    split=splitting(ans,x)
    print(" the bill splitted per person is: ",split)

main()
