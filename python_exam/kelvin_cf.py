def c_to_k(c):
    return float(c+273.15)

def k_to_c(k):
    return float(k-273.15)


def c_to_f(c):
    return float((9/5)*c+32)

def f_to_c(f):
    return float((f-32)*(5/9))

def main():
    s=input(" enter f or c or k  for farenheit ,celsuis , kelvin to mention which value you have: ")
    x=float(input(" enter the value "))
    if s=="c":
        z=input(" enter f or k for what value you want celsius to convert into ")
        if z=="f":
            
            ans=c_to_f(x)
        else:
            ans=c_to_k(x)
    elif s=="k":
        z=input(" enter f or c for what value you want kelvin to convert into ")
        if z=="c":
            ans=k_to_c(x)
        else:
            a=k_to_c(x)
            ans=c_to_f(a)

    elif s=="f":
        z=input(" enter c or k so that farenheit can be converted to that: ")
        if z=="c":
            ans=f_to_c(x)
        else:
            a=f_to_c(x)
            ans=c_to_k(a)

    print(" after the conversion the answer is: ",ans)


main()


    