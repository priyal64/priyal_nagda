# max function
from cmath import inf


def find_max(x,n):
    a=-inf
    ind=-1
    for i in range(0,n):
        if x[i]>a:
            a=x[i]
            ind=i
    return ind,a

#max_2 function
def find_second_max(x,n,ma_x,ind):
    a=-inf
    ind2=-1
    for i in range(0,n):
        if x[i]>a and x[i]!=ma_x and i!=ind:
            a=x[i]
            ind2=i
    return ind2,a

def main():
    x=[]
    n=int(input("enter the size of the list: "))
    print("please give the inputs: ")
    for i in range(n):
        ans=int(input())
        x.append(ans)
    ind,ma_x=find_max(x,n)
    ind2,max2=find_second_max(x,n,ma_x,ind)
    print("second max is: ",max2)
    print("at index: ",ind2)

main()