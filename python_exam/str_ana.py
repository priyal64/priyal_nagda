def rever(s,n):
    x=""
    for i in range(n-1,-1,-1):
       x+=s[i] 
    return x

def is_letter(s):
    if(s>='a' and s<='z' or s>='A' and s<='Z'):
        return True
    return False
    
def count_vow(s,n):
    v=0
    c=0
    d=0
    sp=0
    for i in range(0,n+1):
        if is_letter(s[i]):
            if (s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U'):
                v+=1
            else:
                c+=1
        elif s[i]>="0" and s[i]<="9":
            d+=1
        else:
            sp+=1
        return [v,c,d,sp]


def main():
    n=int(input(" enter string length(): "))
    s=input(" enter string ")
    x=rever(s,n)
    v=count_vow(s,n)
    print(" the number of vowels are :",v[0])
    print(" the number of consonants are : ",v[1])
    print(" the number of digits are: ",v[2])
    print(" the number of special characters are: ",v[3])

    print(" if reversed then: ",x)
main()