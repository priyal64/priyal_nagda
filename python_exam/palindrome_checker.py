#  palindrome_function
def is_pal(s,n):
    ans=0
    
    for i in range(0,int(n/2)+1):
        if(s[i]==s[n-i-1]):
            # continue
            ans+=1
        else:
            return False
    return True

def main():
    n=int(input("enter length of the string: "))
    print("please give string: ")
    s=input()
    print(s[0])
    if is_pal(s,n):
        print("string is palindrome ")
    else:
        print("string is not palindrome")
main()