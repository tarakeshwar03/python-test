a=int(input("enter the number:"))
if a%2!=0:
    print("WEIRD")
elif a%2==0:
    if a==2 or a==3 or a==4 or a==5:
        print("NOT WEIRD")
    elif a>20:
        print("NOT WEIRD")
