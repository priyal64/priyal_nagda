# factorial number
import math


# fact
def fact_of_num(n):
    ans=1
    for i in range(2,n+1):
        ans*=i

    # x[n]=ans
    return ans

def main():
    while True:
        n=int(input("please enter the number :"))
        if n>=0:
            break
        print("please enter positive number only")
        
        
             # x=[]
        
        
    
    print("the answer is: ")
    ans=fact_of_num(n)
    print(ans)
main()
    
        

