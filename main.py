# Bank System

def create_account():
    account_number = input("Enter account number: ")
    name = input("Enter name: ")
    balance = input("Enter initial balance: ")

    with open("accounts.txt", "a") as file:
        file.write(f"{account_number},{name},{balance}\n")

    print("Account created successfully!")

def deposit():
    account_number = input("Enter account number: ")
    amount = input("Enter amount to deposit: ")

    with open("accounts.txt", "r+") as file:
        data = file.readlines()
        file.seek(0)
        for line in data:
            info = line.strip().split(",")
            if info[0] == account_number:
                info[2] = str(int(info[2]) + int(amount))
                file.write(",".join(info) + "\n")
            else:
                file.write(line)
        file.truncate()

    print("Deposit successful!")

def withdraw():
    account_number = input("Enter account number: ")
    amount = input("Enter amount to withdraw: ")

    with open("accounts.txt", "r+") as file:
        data = file.readlines()
        file.seek(0)
        for line in data:
            info = line.strip().split(",")
            if info[0] == account_number:
                if int(info[2]) >= int(amount):
                    info[2] = str(int(info[2]) - int(amount))
                    file.write(",".join(info) + "\n")
                else:
                    print("Insufficient balance!")
                    file.write(line)
            else:
                file.write(line)
        file.truncate()

    print("Withdrawal successful!")

def display_balance():
    account_number = input("Enter account number: ")

    with open("accounts.txt", "r") as file:
        for line in file:
            info = line.strip().split(",")
            if info[0] == account_number:
                print(f"Balance: {info[2]}")

while True:
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display Balance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        display_balance()
    elif choice == "5":
        break
    else:
        print("Invalid choice!")
