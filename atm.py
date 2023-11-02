print("WELCOME TO ATM MACHINE")
a=input("What is your username : ")
print("Welcome to bank",a)
a=input("Create Password : ")
b=input("Enter password : ")
if b==a:
    print("Login Successful")
while(b!=a):
    print("Wrong password")
    b=input("Enter password again : ")
    if b==a:
        print("Login Successful")
        break

if b==a:
    
    c=int(input("Enter the current amount in your bank account : "))
    
    
    while True:
        print("\n")
        print("1) ADD MONEY \n2) WITHDRAW MONEY\n3) CHECK BALANCE\n4) LOGOUT\n ")
        d=int(input("Enter Choice :"))
        if d==1:
            e=int(input("Enter amount you want to add :"))
            c=c+e
            print("New amount is :",c)
        if d==2:
            f=int(input("Enter amount you want to withdraw :"))
            if f>c:
                print("Poor kid")
            else:
                c=c-f
                print("New amount is :",c)
        if d==3:
            print(c)
        if d==4:
            print("THANK YOU")
            break;
        
        
