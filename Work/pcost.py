# pcost.py
import sys
import csv

def portfolio_cost(file_name):
    total_cost = 0.0

    with open(file_name) as file:
        rows = csv.reader(file)
        headers = next(rows)

        for rowno, line in enumerate(rows, start=1):
            record = dict(zip(headers, line))
            try:
                nShares = int(record['shares'])
                price = float(record['price'])
                total_cost+= nShares*price
            except ValueError:
                print(f'Row {rowno}: Bad row: {line}')

    return total_cost

if len(sys.argv)==2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

total_cost = portfolio_cost(filename)
print('Total Cost', total_cost)

