import math

#  function for prime number
def is_prime(n):
    if n%2==0:
        return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i==0:
            return False
    return True

# display function
def display(n):
    print(n)

def main():
    while(True):
        n=int(input("enter upper limit value: "))
        p=int(input("enter lower limit: "))
        if(n>p and n>=0 and p>=0):
            break
        print("give a valid range: ")
    i=p
    
    ans=[]
    if(p<=3):
        ans.append(2)
    
    while(i<=n):
        if is_prime(i):
            ans.append(i)
        i+=1
    
    print("the prime numbers between ",n," and ",p," are: ")
    display(ans)
main()