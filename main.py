from bank import Bank

bank = Bank()


def atm_menu(account):
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction History")
        print("5. Logout")

        choice = input("Choose option: ")

        if choice == "1":
            print("Balance:", account.check_balance())

        elif choice == "2":
            amt = int(input("Enter amount: "))
            print(account.deposit(amt))
            bank.save_data()

        elif choice == "3":
            amt = int(input("Enter amount: "))
            print(account.withdraw(amt))
            bank.save_data()

        elif choice == "4":
            print("\nTransaction History:")
            for item in account.get_history():
                print("-", item)

        elif choice == "5":
            print("Logged out.")
            break

        else:
            print("Invalid choice")


def main():
    while True:
        print("\n====== PYTHON BANK ATM ======")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            name = input("Enter name: ")
            pin = int(input("Set 4-digit PIN: "))
            balance = int(input("Initial balance: "))
            print(bank.create_account(name, pin, balance))

        elif choice == "2":
            name = input("Enter name: ")
            pin = int(input("Enter PIN: "))

            account = bank.login(name, pin)
            if account:
                print(f"Welcome {name} 👋")
                atm_menu(account)
            else:
                print("Invalid credentials")

        elif choice == "3":
            print("Thank you for using ATM.")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
