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


# ---------------- CALCULATION FUNCTIONS ----------------

def calculate_emi(loan_amount, interest_rate, loan_years):
    monthly_rate = interest_rate / 12 / 100
    months = loan_years * 12

    if months == 0:
        return 0, 0, 0

    if monthly_rate == 0:
        emi = loan_amount / months
    else:
        emi = (loan_amount * monthly_rate * (1 + monthly_rate) ** months) / \
              ((1 + monthly_rate) ** months - 1)

    total_payment = emi * months
    total_interest = total_payment - loan_amount

    return emi, total_payment, total_interest


def calculate_simple_interest(principal, rate, years):
    interest = (principal * rate * years) / 100
    total_amount = principal + interest

    return interest, total_amount


def calculate_compound_interest(principal, rate, years, frequency):
    if frequency == 0:
        return 0, 0

    amount = principal * \
             (1 + rate / (100 * frequency)) ** (frequency * years)

    interest = amount - principal

    return interest, amount


def calculate_gst(amount, gst_rate):
    gst = amount * gst_rate / 100
    final_amount = amount + gst

    return gst, final_amount


def calculate_salary(monthly_salary):
    annual_salary = monthly_salary * 12

    return annual_salary


def calculate_savings(salary, expenses):
    savings = salary - expenses

    return savings


# ---------------- USER INTERFACE FUNCTIONS ----------------

def emi_calculator():
    loan_amount = get_number("Enter loan amount: ")
    interest_rate = get_number("Enter annual interest rate (%): ")
    loan_years = get_integer("Enter loan tenure (years): ")

    emi, total_payment, total_interest = calculate_emi(
        loan_amount,
        interest_rate,
        loan_years
    )

    if loan_years == 0:
        print("Loan tenure cannot be zero.")
        return

    print("\n----- EMI RESULT -----")
    print("Monthly EMI:", round(emi, 2))
    print("Total Payment:", round(total_payment, 2))
    print("Total Interest:", round(total_interest, 2))


def simple_interest():
    principal = get_number("Enter principal amount: ")
    rate = get_number("Enter annual interest rate (%): ")
    years = get_number("Enter time (years): ")

    interest, total_amount = calculate_simple_interest(
        principal,
        rate,
        years
    )

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

    interest, amount = calculate_compound_interest(
        principal,
        rate,
        years,
        frequency
    )

    print("\n----- COMPOUND INTEREST RESULT -----")
    print("Interest:", round(interest, 2))
    print("Final Amount:", round(amount, 2))


def gst_calculator():
    amount = get_number("Enter amount: ")
    gst_rate = get_number("Enter GST rate (%): ")

    gst, final_amount = calculate_gst(amount, gst_rate)

    print("\n----- GST RESULT -----")
    print("GST Amount:", round(gst, 2))
    print("Final Amount:", round(final_amount, 2))


def salary_calculator():
    monthly_salary = get_number("Enter monthly salary: ")

    annual_salary = calculate_salary(monthly_salary)

    print("\n----- SALARY RESULT -----")
    print("Monthly Salary:", round(monthly_salary, 2))
    print("Annual Salary:", round(annual_salary, 2))


def savings_calculator():
    salary = get_number("Enter monthly salary: ")
    expenses = get_number("Enter monthly expenses: ")

    savings = calculate_savings(salary, expenses)

    print("\n----- SAVINGS RESULT -----")
    print("Monthly Savings:", round(savings, 2))

    if savings > 0:
        print("You are saving money every month.")
    elif savings == 0:
        print("You are breaking even.")
    else:
        print("Warning: Your expenses are higher than your salary.")


# ---------------- MAIN MENU ----------------

def main():
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


if __name__ == "__main__":
    main()