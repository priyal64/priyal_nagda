# password checker

def check_caps(s,n):
    
    for i in range(0,n):
        if(s[i]>="A" and s[i]<="Z"):
            return True
    return False
        

def check_small(s,n):
    for i in range(0,n):
        if(s[i]>="a" and s[i]<="z"):
            return True
    return False

def check_digi(s,n):
    for i in range(0,n):
        if(s[i]>="0" and s[i]<="9"):
            return True
    return False

def check_special(s,n):
    for i in range(0,n):
        if(s[i]=='/' or s[i]=='!'or s[i]=='@' or s[i]=='#' or s[i]=='%' or s[i]=='^' or s[i]=='&' or s[i]=='*' or s[i]=='(' or s[i]==')' or s[i]=='_' or s[i]=='-' or s[i]=='+'):
            return True
    return False

def main():
    n=int(input("enter the length of the string: "))
    
    if n>=8:
        s=input("enter string: ")
        if check_caps(s,n) and check_small(s,n) and check_digi(s,n) and check_special(s,n):
            print("strong password ")
        
        else:
            if check_caps(s,n)==False:
                print("please add capital letter to the password")
            if check_small(s,n)==False:
                print("please include small letter to the password")

            if check_digi(s,n)==False:
                print("please include a digit in to the password")
            if check_special(s,n)==False:
                print("please include a special character to the password")
    else:
        print("increase the length to 8")
        
main()
        
