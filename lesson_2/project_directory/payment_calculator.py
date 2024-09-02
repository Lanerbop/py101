import os
import json

with open('payment_calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

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

    def input_validation_for_retry():
        nonlocal retry
        while True:
            if retry in ["y", "n"]:
                break

            prompt(MESSAGES["retry_calculator_invalid"])
            retry = input().lower()

    def get_loan_outstanding():
        prompt(MESSAGES["outstanding_loan"])
        loan_outstanding = input()

        while invalid_float(loan_outstanding):
            prompt(MESSAGES["outstanding_loan_invalid"])
            loan_outstanding = input()

        return loan_outstanding

    def get_apr():
        prompt(MESSAGES["apr"])
        apr = input()
        while invalid_float(apr):
            prompt(MESSAGES["apr_invalid"])
            apr = input()

        return apr

    def display_welcome_message():
        prompt(MESSAGES["welcome_message"])

    def display_result():
        prompt(MESSAGES["display_result"] + monthly_payment)

    def display_try_again_question():
        prompt(MESSAGES["retry_calculator_question"])

    def get_loan_duration():
        prompt(MESSAGES["loan_duration"])
        loan_duration_months = input()
        while invalid_float(loan_duration_months):
            prompt(MESSAGES["loan_duration_invalid"])
            loan_duration_months = input()

        return loan_duration_months


    clear()

    display_welcome_message()

    # MAIN LOOP
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

        input_validation_for_retry()
        
        if retry == 'n':
            clear()
            prompt(MESSAGES["goodbye_message"])
            break

        clear()

calculator()