# Helper functions to print messages in colors.

def print_blue(message):
    print(f"\033[94m{message}\033[0m")


def print_green(message):
    print(f"\033[92m{message}\033[0m")


def show_balance(balance):
    print_blue("-------------------------")
    print_blue(f"Your balance is ${balance:.2f}")
    print_blue("-------------------------")


def deposit():
    print_blue("-------------------------")
    amount = float(input("\033[94mEnter an amount to be deposited: \033[0m"))
    print_blue("-------------------------")

    if amount < 0:
        print_blue("-------------------------")
        print_blue("That's not a valid amount")
        print_blue("-------------------------")
        return 0
    else:
        return amount


def withdraw(balance):
    print_blue("-------------------------")
    amount = float(input("\033[94mEnter amount to be withdrawn: \033[0m"))
    print_blue("-------------------------")

    if amount > balance:
        print_blue("-------------------------")
        print_blue("Insufficient funds")
        print_blue("-------------------------")
        return 0
    elif amount < 0:
        print_blue("-------------------------")
        print_blue("Amount must be greater than 0")
        print_blue("-------------------------")
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print_green("**********************")
        print_green("   Banking Program   ")
        print_green("**********************")

        print_green("1.Show Balance")
        print_green("2.Deposit")
        print_green("3.Withdraw")
        print_green("4.Exit")
        print_green("**********************")

        choice = input("\033[92mEnter your choice (1-4): \033[0m")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print_blue("-------------------------")
            print_blue("That is not a valid choice")
            print_blue("-------------------------")

    print_blue("============================")
    print_blue("Thank you! Have a nice day!")
    print_blue("============================")


if __name__ == '__main__':
    main()