import os

def prompt(message):
    return print(f"==> {message}")

def invalid_float(number_as_string):
    if number_as_string in ["nan", "inf", "infinity"]:
        return True

    try:
        float(number_as_string)
    except ValueError:
        return True
    
    if float(number_as_string) < 0:
        return True

    return False

os.system('clear')

prompt("Welcome to Monthly Payment Calculator")

while True:
    prompt("What is the outstanding loan amount in dollars? (Ex: '13500')")
    loan_outstanding = input()
    while invalid_float(loan_outstanding):
        prompt("Please only type positive numbers. (Hint: Don't use '$'"
            " or ',' in your number.)")
        loan_outstanding = input()

    loan_outstanding = float(loan_outstanding)


    prompt("What is the APR of the loan in percentage format? (Ex: '15.7')")
    apr = input()
    while invalid_float(apr):
        prompt("Please only type positive numbers. (Hint: Don't use"
               " the '%' sign.)")
        apr = input()

    apr = float(apr) / 100
    monthly_apr = apr / 12


    prompt("What is the outstanding loan duration in months?")
    loan_duration_months = input()
    while invalid_float(loan_duration_months):
        prompt("Please only type numbers")
        loan_duration_months = input()

    loan_duration_months = int(float(loan_duration_months))
    # loan_duration_months rounds down to nearest integer if it
    # is a decimal, which is desired and logical!


    # Monthly Payment Calculation
    if loan_duration_months == 0:
        monthly_payment = loan_outstanding
    elif monthly_apr == 0:
        monthly_payment = round((loan_outstanding / loan_duration_months), 2)
    else:
        monthly_payment = round((loan_outstanding * (monthly_apr / (1
            - (1 + monthly_apr)**(-1 * loan_duration_months)))), 2)

    monthly_payment = f"{monthly_payment:.2f}" # display to 2 decimal places


    prompt("Your monthly payment is: $" + str(monthly_payment))
    prompt("Would you like to use Monthly Payment Calculator again? y/n")
    retry = input().lower()
    while True:
        if retry in ["y", "n"]:
            break

        prompt('Please enter "y" or "n".')
        retry = input().lower()

    if retry == 'n':
        os.system('clear')
        prompt("Goodbye!")
        break

    os.system('clear')