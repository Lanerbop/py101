import os

def calculator():

    def clear():
        os.system('clear')

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

    def get_loan_outstanding():
        prompt("What is the outstanding loan amount in dollars? (Ex: '13500')")
        loan_outstanding = input()

        while invalid_float(loan_outstanding):
            prompt("Please only type positive numbers. (Hint: Don't use '$'"
                " or ',' in your number.)")
            loan_outstanding = input()

        return loan_outstanding

    def get_apr():
        prompt("What is the APR of the loan in percentage format?"
               " (Ex: '15.7')")
        apr = input()
        while invalid_float(apr):
            prompt("Please only type positive numbers. (Hint: Don't use"
                " the '%' sign.)")
            apr = input()

        return apr

    def display_welcome_message():
        prompt("Welcome to Monthly Payment Calculator")

    def display_result():
        prompt("Your monthly payment is: $" + monthly_payment)

    def display_try_again_question():
        prompt("Would you like to use Monthly Payment Calculator again? y/n")

    def get_loan_duration():
        prompt("What is the outstanding loan duration in months?")
        loan_duration_months = input()
        while invalid_float(loan_duration_months):
            prompt("Please only type numbers")
            loan_duration_months = input()

        return loan_duration_months


    clear()

    display_welcome_message()


    while True:
        loan_outstanding = get_loan_outstanding()
        loan_outstanding = float(loan_outstanding)

        apr = get_apr()
        apr = float(apr) / 100
        monthly_apr = apr / 12

        loan_duration_months = get_loan_duration()
        loan_duration_months = int(float(loan_duration_months))
        # loan_duration_months rounds down to nearest integer if input
        # contains a decimal, which is desired and logical!


        # Monthly Payment Calculation
        if loan_duration_months == 0:
            monthly_payment = loan_outstanding
        elif monthly_apr == 0:
            monthly_payment = round((loan_outstanding
                                    / loan_duration_months), 2)
        else:
            monthly_payment = round((loan_outstanding * (monthly_apr /
            (1- (1 + monthly_apr)**(-1 * loan_duration_months)))), 2)

        monthly_payment = f"{monthly_payment:.2f}" # display to 2 decimal place


        display_result()

        display_try_again_question()
        retry = input().lower()
        while True:
            if retry in ["y", "n"]:
                break

            prompt('Please enter "y" or "n".')
            retry = input().lower()

        if retry == 'n':
            clear()
            prompt("Goodbye!")
            break

        clear()

calculator()