# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    portfolio = []

    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            holding = {}
            holding['name'] = record['name']
            holding['shares'] = int(record['shares'])
            holding['price'] = float(record['price'])
            portfolio.append(holding)

    return portfolio

def read_prices(filename):
    prices = {}

    with open(filename) as file:
        rows = csv.reader(file)
        for row in rows:
            if len(row)>=2:
                prices[row[0]] = float(row[1])

    return prices

def make_report(portfolio, prices):
    report = []

    for holding in portfolio:
        name = holding['name']
        shares = holding['shares']
        price = prices[name]
        change = price - holding['price']
        report.append((name, shares, price, change))

    return report

portfolio = read_portfolio('Data/portfoliodate.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)

headers = ['Name', 'Shares', 'Price', 'Change']
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')

print(f'{'':_>10} {'':_>10} {'':_>10} {'':_>10}')

for name, share, price, diff in report:
    print(f'{name:>10s} {share:>10d} {price:>10.2f} {diff:>10.2f}')


