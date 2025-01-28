# ATM Simulation
# - Create a program to simulate an ATM where users can:
# - Check balance
# - Deposit money
# - Withdraw money
# - Exit
# - Use functions for each operation and implement proper input validation (e.g., insufficient
# balance for withdrawal).
# 1--i can create list in list where many users are present 
# 2--or i can create a list where only one users everything is given
# for 2 i can do is
# s.no name age money  
def balance(l,x):
    return l[x][3]

def withdraw(l,x,amount):
    if(l[x][3]>amount):
        print(" deducted from account")
        l[x][3]=l[x][3]-amount
    else:
        print("can't deduct  ")
    return l

def deposit(l,x,amount):
    l[x][3]=l[x][3]+amount
    print("the amount is deposited ")
    return l

def main():
    l=[[0,'xyz',20,19000],[1,'name',22,20000],[2,'pqrs',22,30000],[3,'abcd',23,30200]]
    
    while(True):
        s=int(input(" enter 1 for checking balance ,2 for depositing , 3 for withdrawing :"))
        if s==1:
            a=int(input("please enter s.no :"))
            ans=balance(l,a)
            print(" the balance is: ",ans)
        elif s==2:
            a=int(input("please enter your s.no :"))
            b=int(input("please enter the amount to be deposit: "))
            l=deposit(l,a,b)
        elif s==3:
            a=int(input("please enter your s.no: "))
            b=int(input(" please enter the amount to be withdrawn:"))
            l=withdraw(l,a,b)
        else:
            break

main()
        