def isleap(x):
    if x%100==0:
        if x%400==0:
            return True
    else:
        if x%4==0:
            return True
    return False

def main():
    n=int(input(" enter the year to check if it is leap year or not: "))
    if isleap(n):
        print(" Leap Year")
    else:
        print("not a leap year")
main()