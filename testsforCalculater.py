from AdvanceCalculater import (
    calculate_emi,
    calculate_simple_interest,
    calculate_compound_interest,
    calculate_gst,
    calculate_salary,
    calculate_savings
)


def test_simple_interest():
    interest, total = calculate_simple_interest(100000, 8, 3)

    assert interest == 24000
    assert total == 124000


def test_compound_interest():
    interest, amount = calculate_compound_interest(100000, 8, 3, 1)

    assert round(interest, 2) == 25971.2
    assert round(amount, 2) == 125971.2


def test_gst():
    gst, total = calculate_gst(10000, 18)

    assert gst == 1800
    assert total == 11800


def test_salary():
    annual_salary = calculate_salary(30000)

    assert annual_salary == 360000


def test_savings():
    savings = calculate_savings(30000, 22000)

    assert savings == 8000


def test_emi():
    emi, total_payment, total_interest = calculate_emi(
        500000,
        8.5,
        5
    )

    assert round(emi, 2) == 10258.27
    assert round(total_payment, 2) == 615495.94
    assert round(total_interest, 2) == 115495.94