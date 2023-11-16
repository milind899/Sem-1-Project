print("WELCOME TO ATM MACHINE")
a = input("What is your username: ")
account_type = input("Enter account type (Savings/Current): ")
print("Welcome to", account_type, "account,", a)

# Set initial password
a_password = input("Create Password: ")

# Login loop
while True:
    b = input("Enter password: ")
    if b == a_password:
        print("Login Successful")
        break
    else:
        print("Wrong password")

# Initialize account balance and other variables
c = int(input("Enter the current amount in your bank account: "))
minimum_balance = 500
interest_rate = 0.02
transaction_history = []

# Main menu loop
while True:
    print("\n1) ADD MONEY\n2) WITHDRAW MONEY\n3) CHECK BALANCE\n4) DISPLAY TRANSACTION HISTORY\n5) LOGOUT\n")
    d = int(input("Enter Choice: "))

    if d == 1:
        e = int(input("Enter amount you want to add: "))
        c = c + e
        print("New amount is:", c)

    elif d == 2:
        f = int(input("Enter amount you want to withdraw: "))
        if f > c:
            print("Insufficient funds")
        elif account_type.lower() == "savings":
            print("Withdrawal failed. Can't withdraw money from savings account")
        else:
            c = c - f
            print("New amount is:", c)

    elif d == 3:
        print("Balance:", c)

    elif d == 4:
        print("Transaction History:")
        for transaction in range(0,len(transaction_history)-1):
            print(transaction_history[transaction])

    elif d == 5:
        print("THANK YOU")
        break

    # Add interest for savings account
    if account_type.lower() == "savings" and d==1:
        interest = c * interest_rate
        c += interest
        print("Interest added:", interest)

    # Record transaction in history
    transaction_history.append(f"Transaction: {d}, Amount: {e if d == 1 else f}, Balance: {c}")
