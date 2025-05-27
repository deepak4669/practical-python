# report.py
#
# Exercise 2.4

import csv
from fileparse import parse_csv
import sys

def read_portfolio(filename):
    with open(filename) as file:
        rows = csv.reader(file)
        portfolio = parse_csv(rows, select_cols=['name', 'shares', 'price'], types=[str, int, float])
    return portfolio

def read_prices(filename)->dict:
    '''
    Read prices from CSV file for stock name and price data
    '''
    with open(filename) as file:
        rows = csv.reader(file)
        prices = dict(parse_csv(rows, types=[str, float], has_headers=False))
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

def print_report(report):
    headers = ['Name', 'Shares', 'Price', 'Change']
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')

    print(f'{'':_>10} {'':_>10} {'':_>10} {'':_>10}')

    for name, share, price, diff in report:
        print(f'{name:>10s} {share:>10d} {price:>10.2f} {diff:>10.2f}')

def portfolio_report(portfolio_file, prices_file):
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)
    report = make_report(portfolio, prices)
    print_report(report)

def main(argv):
    portfolio_report(argv[1], argv[2])

if __name__ == '__main__':
    argv = sys.argv
    main(argv)

