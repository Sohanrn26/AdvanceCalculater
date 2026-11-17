def get_number(message):
    while True:
        try:
            value = float(input(message))

            if value < 0:
                print("Please enter a positive number.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a number.")


def get_integer(message):
    while True:
        try:
            value = int(input(message))

            if value < 0:
                print("Please enter a positive number.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def emi_calculator():
    loan_amount = get_number("Enter loan amount: ")
    interest_rate = get_number("Enter annual interest rate (%): ")
    loan_years = get_integer("Enter loan tenure (years): ")

    if loan_years == 0:
        print("Loan tenure cannot be zero.")
        return

    monthly_rate = interest_rate / 12 / 100
    months = loan_years * 12

    if monthly_rate == 0:
        emi = loan_amount / months
    else:
        emi = (loan_amount * monthly_rate * (1 + monthly_rate) ** months) / \
              ((1 + monthly_rate) ** months - 1)

    total_payment = emi * months
    total_interest = total_payment - loan_amount

    print("\n----- EMI RESULT -----")
    print("Monthly EMI:", round(emi, 2))
    print("Total Payment:", round(total_payment, 2))
    print("Total Interest:", round(total_interest, 2))


def simple_interest():
    principal = get_number("Enter principal amount: ")
    rate = get_number("Enter annual interest rate (%): ")
    years = get_number("Enter time (years): ")

    interest = (principal * rate * years) / 100
    total_amount = principal + interest

    print("\n----- SIMPLE INTEREST RESULT -----")
    print("Interest:", round(interest, 2))
    print("Total Amount:", round(total_amount, 2))


def compound_interest():
    principal = get_number("Enter principal amount: ")
    rate = get_number("Enter annual interest rate (%): ")
    years = get_number("Enter time (years): ")
    frequency = get_integer("Enter compounding frequency per year: ")

    if frequency == 0:
        print("Compounding frequency cannot be zero.")
        return

    amount = principal * (1 + rate / (100 * frequency)) ** (frequency * years)
    interest = amount - principal

    print("\n----- COMPOUND INTEREST RESULT -----")
    print("Interest:", round(interest, 2))
    print("Final Amount:", round(amount, 2))


def gst_calculator():
    amount = get_number("Enter amount: ")
    gst_rate = get_number("Enter GST rate (%): ")

    gst = amount * gst_rate / 100
    final_amount = amount + gst

    print("\n----- GST RESULT -----")
    print("GST Amount:", round(gst, 2))
    print("Final Amount:", round(final_amount, 2))


def salary_calculator():
    monthly_salary = get_number("Enter monthly salary: ")

    annual_salary = monthly_salary * 12

    print("\n----- SALARY RESULT -----")
    print("Monthly Salary:", round(monthly_salary, 2))
    print("Annual Salary:", round(annual_salary, 2))


def savings_calculator():
    salary = get_number("Enter monthly salary: ")
    expenses = get_number("Enter monthly expenses: ")

    savings = salary - expenses

    print("\n----- SAVINGS RESULT -----")
    print("Monthly Savings:", round(savings, 2))

    if savings > 0:
        print("You are saving money every month.")
    elif savings == 0:
        print("You are breaking even.")
    else:
        print("Warning: Your expenses are higher than your salary.")


# ---------------- MAIN MENU ----------------

print("==============================")
print("     PERSONAL CALCULATOR")
print("==============================")

print("1. EMI Calculator")
print("2. Simple Interest")
print("3. Compound Interest")
print("4. GST Calculator")
print("5. Salary Calculator")
print("6. Monthly Savings Calculator")
print("7. Exit")

choice = input("Enter your choice: ")

if choice == "1":
    emi_calculator()

elif choice == "2":
    simple_interest()

elif choice == "3":
    compound_interest()

elif choice == "4":
    gst_calculator()

elif choice == "5":
    salary_calculator()

elif choice == "6":
    savings_calculator()

elif choice == "7":
    print("Thank you for using Personal Calculator!")

else:
    print("Invalid choice. Please select an option from 1 to 7.")