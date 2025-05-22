# mortgage.py
#
# Exercise 1.7
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
month_required = 0;

while principal > 0:
    curr_payment = payment
    if month_required>=extra_payment_start_month and month_required<=extra_payment_end_month:
        curr_payment += extra_payment

    curr_payed = min(principal*(1+rate/12), curr_payment)

    principal = round(principal * (1+rate/12) - curr_payed, 2)
    total_paid = round(total_paid + curr_payed, 2)
    month_required += 1

    print(f'{month_required} month required, ${total_paid:0.2f} Total Paid, ${principal:0.2f}')

print('Total paid', total_paid)
print('Months', month_required)
