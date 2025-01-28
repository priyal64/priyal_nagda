# check multiplesof 3
def mul_3(n):
    if n%3==0:
        return True
    return False

# check multiples of 5
def mul_5(n):
    if n%5==0:
        return True
    return False
def mul_5andmul_3(n):
    if mul_3(n) and mul_5(n):
        return True
    return False

# main function
def main():
    n=int(input("enter upper limit: "))
    for i in range(1,n+1):
        if mul_3(i):
            if mul_5(i):
                print("FizzBuzz")
            else:
                print("Fizz")
        elif mul_5(i):
            print("Buzz")
        else:
            print(i)
main()
