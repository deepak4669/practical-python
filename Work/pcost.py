# pcost.py
import sys
import csv

def portfolio_cost(file_name):
    total_cost = 0.0

    with open(file_name) as file:
        rows = csv.reader(file)
        headers = next(rows)

        for line in rows:
            try:
                total_cost += int(line[1])*float(line[2])
            except ValueError:
                print('Parsing Gone Bad', line)

    return total_cost

if len(sys.argv)==2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

total_cost = portfolio_cost(filename)
print('Total Cost', total_cost)

