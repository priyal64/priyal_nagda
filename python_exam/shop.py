def add_cart(l,n,d,s):
    s+=d
    l.append({n,d})
    return s




def main():
    s=0
    l=[{}]
    n=(input("enter name of the item: "))
    d=int(input("enter the price of the item: "))
    s=add_cart(l,n,d,s)
    print(" the list items are: ",l)
    print(" the total amount in cart is: ",s)

main()
