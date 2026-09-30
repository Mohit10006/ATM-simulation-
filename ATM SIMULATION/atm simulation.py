print("================================")
print("       WELCOME TO SIMPLE ATM")
print("================================")

name = ""
account = ""
pin = ""
balance = 0
created = False

deposit1 = 0
deposit2 = 0
withdraw1 = 0
withdraw2 = 0

while True:

    print("\n----------- ATM MENU -----------")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # CREATE ACCOUNT
    if choice == "1":

        if created == True:
            print("Account already exists.")
        else:
            print("\n----- CREATE ACCOUNT -----")

            name = input("Enter your name: ")
            account = input("Create account number: ")
            pin = input("Create 4 digit PIN: ")

            if len(pin) != 4:
                print("PIN must contain 4 digits.")
                name = ""
                account = ""
                pin = ""
            else:
                balance = 0
                created = True
                print("Account created successfully!")

    # LOGIN
    elif choice == "2":

        if created == False:
            print("Please create an account first.")

        else:
            print("\n--------- LOGIN ---------")

            entered_account = input("Enter account number: ")
            entered_pin = input("Enter PIN: ")

            if entered_account == account and entered_pin == pin:

                print("\nLogin successful!")
                print("Welcome", name)

                while True:

                    print("\n-------- ATM SERVICES --------")
                    print("1. Check Balance")
                    print("2. Deposit Money")
                    print("3. Withdraw Money")
                    print("4. Mini Statement")
                    print("5. Change PIN")
                    print("6. Logout")

                    option = input("Enter your choice: ")

                    # BALANCE
                    if option == "1":
                        print("\nYour balance is Rs.", balance)

                    # DEPOSIT
                    elif option == "2":

                        amount = int(input("Enter amount to deposit: "))

                        if amount <= 0:
                            print("Enter a valid amount.")
                        else:
                            balance = balance + amount

                            if deposit1 == 0:
                                deposit1 = amount
                            else:
                                deposit2 = amount

                            print("Money deposited successfully.")
                            print("Current balance: Rs.", balance)

                    # WITHDRAW
                    elif option == "3":

                        amount = int(input("Enter amount to withdraw: "))

                        if amount <= 0:
                            print("Enter a valid amount.")

                        elif amount > balance:
                            print("Insufficient balance.")

                        else:
                            balance = balance - amount

                            if withdraw1 == 0:
                                withdraw1 = amount
                            else:
                                withdraw2 = amount

                            print("Please collect your cash.")
                            print("Current balance: Rs.", balance)

                    # MINI STATEMENT
                    elif option == "4":

                        print("\n------- MINI STATEMENT -------")
                        print("Account Holder:", name)
                        print("Account Number:", account)
                        print("Current Balance: Rs.", balance)

                        if deposit1 != 0:
                            print("Deposit:", deposit1)

                        if deposit2 != 0:
                            print("Deposit:", deposit2)

                        if withdraw1 != 0:
                            print("Withdrawal:", withdraw1)

                        if withdraw2 != 0:
                            print("Withdrawal:", withdraw2)

                        print("------------------------------")

                    # CHANGE PIN
                    elif option == "5":

                        old_pin = input("Enter old PIN: ")

                        if old_pin == pin:

                            new_pin = input("Enter new 4 digit PIN: ")

                            if len(new_pin) == 4:
                                pin = new_pin
                                print("PIN changed successfully.")
                            else:
                                print("PIN must contain 4 digits.")

                        else:
                            print("Wrong PIN.")

                    # LOGOUT
                    elif option == "6":
                        print("You have been logged out.")
                        break

                    else:
                        print("Invalid choice.")

            else:
                print("Invalid account number or PIN.")

    # EXIT
    elif choice == "3":
        print("\nThank you for using Simple ATM.")
        break

    else:
        print("Invalid choice. Please try again.")