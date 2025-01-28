import math


# multi_function
def multiplication_table(n):
    for i in range(1,11):
        print(n ," * ",i," = ",n*i)

def main():
    n=int(input("please enter a number whose multiplication table you want: "))
    print("the multiplication table of the number is: ",n)

    multiplication_table(n)

main()