
file = "expenses.txt"


def welcome():

    print("Personal Expense Tracker")
    print("-------------------------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Remove Expense")
    print("5. Exit")
    print("-------------------------")
    print("")


def load_expenses():

    expenses = []

    try:
        with open(file, "r") as f:
            for line in f:
                category, amount = line.strip().split(",")
                expenses.append(
                    {"category": category, "amount": float(amount)})

    except FileNotFoundError:
        print("No expense file found. Starting with an empty list.")

    except (ValueError, TypeError) as e:
        print(f"Invalid expense data: {e}")

    return expenses


def save_expenses(expenses):

    with open(file, "w") as f:
        for e in expenses:
            f.write(f'{e["category"]},{e["amount"]}\n')


def add_expense(expenses):

    try:
        category = input("Enter expense category: ").strip()

        if not category or "," in category:
            print("Please enter a valid category.")
            return

        amount = float(input("Enter expense amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        expenses.append({"category": category, "amount": amount})
        save_expenses(expenses)
        print("Expense added successfully.")

    except ValueError:
        print("Invalid amount input.")

    except OSError as e:
        print(f"File error: {e}")


def view_expenses(expenses):

    if not expenses:
        print("\nThere are no expenses to view.")
        return

    print("\nExpenses:")
    i = 1

    for e in expenses:
        print(f'{i}. {e["category"]} = {e["amount"]}$')
        i += 1

    print()


def total_expense(expenses):

    total = 0

    for e in expenses:
        total += e["amount"]

    print(f"Your total expenditure is: {total}$")


def remove_expense(expenses):

    if not expenses:
        print("\nThere are no expenses to remove.")
        return

    view_expenses(expenses)

    try:
        number = int(input("Enter expense number to remove: "))

        if number >= 1 and number <= len(expenses):
            removed = expenses.pop(number - 1)
            save_expenses(expenses)
            print(
                f'Removed: {removed["category"]} - '
                f'{removed["amount"]}$'
            )

        else:
            print("Invalid number.\n")

    except ValueError:
        print("Enter a valid number.\n")

    except OSError as e:
        print(f"File error: {e}")


def main():

    expenses = load_expenses()

    while True:
        welcome()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total_expense(expenses)

        elif choice == "4":
            remove_expense(expenses)

        elif choice == "5":
            print("Thank you for using the program.")
            return

        else:
            print("Invalid input.")


main()
