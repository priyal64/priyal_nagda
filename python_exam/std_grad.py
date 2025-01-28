def is_pass(n):
    if n>35:
        return True
    return False

def is_a(n):
    if n>=410:
        return True
    return False

def is_b(n):
    if(n>350 and n<410):
        return True
    return False

def is_c(n):
    if(n>275 and n<=350):
        return True
    return False

def main():
    s=input("enter student's name: ")
    a=0
    print(" enter 5 subject marks please: ")
    for i in range(5):
        ans=int(input())
        if(is_pass(ans)):
            a+=ans
        # print(s,"passed the test with marks:",a)
        else:
            print(" student failed in one subject")
    if(is_a(a)):
        print(s,"got A grade with marks as: ",a)
    elif(is_b(a)):
        print(s,"got B grade with marks as: ",a)
    elif(is_c(a)):
        print(s,"got C grade with as:",a)
    elif(is_pass(a)):
        print(s,"passed the test with marks:",a)
    else:
        print(s,"failed the test with marks:",a)
main()

    

