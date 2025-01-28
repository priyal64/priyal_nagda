#  pattern

def pattern(n):
    
    for i in range(1,n+1):
        a=""
        for j in range(i):
            a+="*"
        print(a)
def reverse_pattern(n):
    for i in range(n,0,-1):
        a=""
        for j in range(i):
            a+="*"
        print(a)
def main():
    n=int(input(" enter the value: "))
    x=int(input("please enter 1 for forward print and 2 for reverse print "))
    if x==1:
        pattern(n)
    else:
        reverse_pattern(n)

main()