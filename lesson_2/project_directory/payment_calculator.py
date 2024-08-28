# monthly payment calculator

# input will be the loan amount, apr, and loan duration in months
# output will be the monthly payment

# edge cases include a loan duration of 0, decimals used on months
# (decimals used for months is fine bc python rounds down
# if int is used which results in accurate output)

# main data structure will be floats

# plug in values into monthly payment formula and return value

def prompt(message):
    return print(f"==> {message}")

def invalid_float(number_as_string):
    try:
        float(number_as_string)
    except ValueError:
        return True

    return False


prompt("Welcome to Monthly Payment Calculator")

while True:
    prompt("What is the outstanding loan amount in dollars?")
    loan_outstanding = input()
    while invalid_float(loan_outstanding):
        prompt("Please only type numbers. (Hint: Don't use '$'"
            " or ',' in your number.)")
        loan_outstanding = input()
    loan_outstanding = float(loan_outstanding)

    prompt("What is the APR of the loan in percentage format? (Ex: '15.7')")
    apr = input()
    while invalid_float(apr):
        prompt("Please only type numbers. (Hint: Don't use the '%' sign.)")
        apr = input()
    apr = float(apr) / 100
    monthly_apr = apr / 12

    prompt("What is the outstanding loan duration in months?")
    loan_duration_m = input()
    while invalid_float(loan_duration_m):
        prompt("Please only type numbers")
        loan_duration_m = input()
    loan_duration_m = int(float(loan_duration_m))

    if loan_duration_m != 0:
        monthly_payment = round((loan_outstanding * (monthly_apr / (1
            - (1 + monthly_apr)**(-1 * loan_duration_m)))), 2)
    else:
        monthly_payment = loan_outstanding

    prompt("Your monthly payment is: $" + str(monthly_payment))
    prompt("Would you like to use Monthly Payment Calculator again? y/n")
    retry = input().lower()
    while True:
        if retry.startswith('n') or retry.startswith('y'):
            break

        prompt('Please enter "y" or "n".')
        retry = input().lower()

    if retry[0] == 'n':
        break