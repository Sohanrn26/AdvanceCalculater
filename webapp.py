from flask import Flask, request, render_template_string

from AdvanceCalculater import (
    calculate_emi,
    calculate_simple_interest,
    calculate_compound_interest,
    calculate_gst,
    calculate_salary,
    calculate_savings
)

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Personal Calculator</title>
    <style>
        body {
            font-family: Arial;
            background: #f1f3f6;
            padding: 40px;
        }
        .container {
            background: white;
            max-width: 550px;
            margin: auto;
            padding: 30px;
            border-radius: 12px;
        }
        input, select, button {
            width: 100%;
            padding: 12px;
            margin: 8px 0;
            box-sizing: border-box;
        }
        button {
            background: #2563eb;
            color: white;
            border: none;
            cursor: pointer;
        }
        .result {
            background: #e5f5e9;
            padding: 15px;
            margin-top: 15px;
            white-space: pre-line;
        }
        .error {
            color: red;
        }
    </style>
</head>

<body>
<div class="container">

    <h1>Personal Calculator</h1>

    <form method="POST">

        <label>Select Calculator</label>
        <select name="calculator">
            <option value="emi">EMI Calculator</option>
            <option value="simple">Simple Interest</option>
            <option value="compound">Compound Interest</option>
            <option value="gst">GST Calculator</option>
            <option value="salary">Salary Calculator</option>
            <option value="savings">Monthly Savings</option>
        </select>

        <input type="number" step="any" min="0"
               name="amount" placeholder="Amount / Principal / Salary">

        <input type="number" step="any" min="0"
               name="rate" placeholder="Interest rate / GST rate (%)">

        <input type="number" step="any" min="0"
               name="years" placeholder="Time / Loan tenure (years)">

        <input type="number" min="0"
               name="frequency" placeholder="Compounding frequency per year">

        <input type="number" step="any" min="0"
               name="expenses" placeholder="Monthly expenses">

        <button type="submit">Calculate</button>

    </form>

    {% if result %}
        <div class="result">{{ result }}</div>
    {% endif %}

    {% if error %}
        <p class="error">{{ error }}</p>
    {% endif %}

</div>
</body>
</html>
"""


def get_number(name):
    value = request.form.get(name, "").strip()
    return float(value) if value else 0.0


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    error = None

    if request.method == "POST":

        try:
            choice = request.form.get("calculator")

            amount = get_number("amount")
            rate = get_number("rate")
            years = get_number("years")
            expenses = get_number("expenses")

            frequency_text = request.form.get("frequency", "").strip()
            frequency = int(frequency_text) if frequency_text else 0

            if min(amount, rate, years, expenses, frequency) < 0:
                raise ValueError("Please enter non-negative values.")

            if choice == "emi":

                if years <= 0 or not years.is_integer():
                    raise ValueError("Loan tenure must be a positive whole number.")

                emi, total, interest = calculate_emi(
                    amount, rate, int(years)
                )

                result = (
                    f"Monthly EMI: {emi:.2f}\n"
                    f"Total Payment: {total:.2f}\n"
                    f"Total Interest: {interest:.2f}"
                )

            elif choice == "simple":

                interest, total = calculate_simple_interest(
                    amount, rate, years
                )

                result = (
                    f"Interest: {interest:.2f}\n"
                    f"Total Amount: {total:.2f}"
                )

            elif choice == "compound":

                if frequency <= 0:
                    raise ValueError("Frequency must be greater than zero.")

                interest, total = calculate_compound_interest(
                    amount, rate, years, frequency
                )

                result = (
                    f"Interest: {interest:.2f}\n"
                    f"Final Amount: {total:.2f}"
                )

            elif choice == "gst":

                gst, total = calculate_gst(amount, rate)

                result = (
                    f"GST Amount: {gst:.2f}\n"
                    f"Final Amount: {total:.2f}"
                )

            elif choice == "salary":

                annual = calculate_salary(amount)

                result = (
                    f"Monthly Salary: {amount:.2f}\n"
                    f"Annual Salary: {annual:.2f}"
                )

            elif choice == "savings":

                savings = calculate_savings(amount, expenses)

                result = f"Monthly Savings: {savings:.2f}"

            else:
                raise ValueError("Invalid calculator selection.")

        except ValueError as e:
            error = str(e) or "Please enter valid values."

    return render_template_string(
        HTML,
        result=result,
        error=error
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)