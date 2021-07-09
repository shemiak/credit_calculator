import sys
from math import log
from math import ceil
from math import floor
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--type', '-t')
parser.add_argument('--payment', '-p')
parser.add_argument('--principal', '-pr')
parser.add_argument('--periods', '-per')
parser.add_argument('--interest', '-i')
args = parser.parse_args()
args_ = sys.argv


def plur_or_sing(digit):
    if digit == 1:
        return ''
    else:
        return 's'


def calculate_number_payments(loan_principal, monthly_payment, loan_interest):
    loan_interest /= (12 * 100)
    base = 1 + loan_interest
    months_ = log(monthly_payment / (monthly_payment - loan_interest * loan_principal), base)
    years = months_ / 12
    if years % 12 == 0:
        print(f'It will take {years} {plur_or_sing(years)} to repay the loan!')
    else:
        years_int = int(years)
        months = ceil((years - years_int) * 12)
        if months == 12:
            print(f'It will take {int(years) + 1} year{plur_or_sing(years)} to repay the loan!')
        else:
            print(
                f'It will take {years_int} year{plur_or_sing(years)} and {months} month{plur_or_sing(months)} to repay the loan!')
    sum_of_payments = ceil(months_) * monthly_payment
    print(f'\nOverpayment = {ceil(sum_of_payments - loan_principal)}')


def calculate_annuity(loan_principal, number_of_periods, loan_interest):
    loan_interest /= (100 * 12)
    annuity_payment = loan_principal * (loan_interest * pow(1 + loan_interest, number_of_periods)) / (
            pow(1 + loan_interest, number_of_periods) - 1)
    print(f'Your monthly payment = {ceil(annuity_payment)}!')
    sum_of_payments = number_of_periods * ceil(annuity_payment)
    print(f'\nOverpayment = {ceil(sum_of_payments - loan_principal)}')


def calculate_loan_principal(annuity_payment, number_of_periods, loan_interest):
    loan_interest /= (100 * 12)
    loan_principal = annuity_payment / (loan_interest * pow(1 + loan_interest, number_of_periods) / (
            pow(1 + loan_interest, number_of_periods) - 1))
    print(f'Your loan principal = {floor(loan_principal)}!')
    sum_of_payments = number_of_periods * annuity_payment
    print(f'\nOverpayment = {ceil(sum_of_payments - loan_principal)}')


def calculate_diff_payments(principal, periods, interest):
    interest /= (100 * 12)
    period = []
    for month in range(periods):
        payment = (principal / periods) + interest * (principal - (principal * month / periods))
        period.append(ceil(payment))
        print(f'Month {month + 1}: payment is {ceil(payment)}')
    sum_of_payments = sum(period)
    print(f'\nOverpayment = {sum_of_payments - principal}')


if len(args_) < 4:
    print('Incorrect parameters')
else:
    if args.type == 'annuity':
        if args.principal is not None and args.payment is not None and args.interest is not None:
            calculate_number_payments(int(args.principal), int(args.payment), float(args.interest))
        elif args.principal is not None and args.periods is not None and args.interest:
            calculate_annuity(int(args.principal), int(args.periods), float(args.interest))
        elif args.payment is not None and args.periods is not None and args.interest is not None:
            calculate_loan_principal(int(args.payment), int(args.periods), float(args.interest))
        else:
            print('Incorrect parameters')
    elif args.type == 'diff':
        if args.principal is not None and args.periods is not None and args.interest is not None:
            calculate_diff_payments(int(args.principal), int(args.periods), float(args.interest))
        else:
            print('Incorrect parameters')
    else:
        print('Incorrect parameters')
