# report.py
#
# Exercise 2.4

import csv
from fileparse import parse_csv
from portfolio import Portfolio
import sys
import stock
import tableformat

def read_portfolio(filename):
    with open(filename) as file:
        portdicts = parse_csv(file, select_cols=['name', 'shares', 'price'], types=[str, int, float])

    portfolio = [stock.Stock(s['name'], s['shares'], s['price']) for s in portdicts]

    return Portfolio(portfolio)

def read_prices(filename)->dict:
    '''
    Read prices from CSV file for stock name and price data
    '''
    with open(filename) as file:
        prices = dict(parse_csv(file, types=[str, float], has_headers=False))
    return prices

def make_report(portfolio, prices):
    report = []

    for holding in portfolio:
        name = holding.name
        shares = holding.shares
        price = prices[name]
        change = price - holding.price
        report.append((name, shares, price, change))

    return report

def print_report(report, formatter):
    headers = ['Name', 'Shares', 'Price', 'Change']
    formatter.headings(headers)

    for name, share, price, diff in report:
        rowdata = [name, str(share), f'{price:0.2f}', f'{diff:0.2f}']
        formatter.row(rowdata)

def portfolio_report(portfolio_file, prices_file, fmt = 'txt'):
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)
    report = make_report(portfolio, prices)

    formatter = tableformat.create_formatter(fmt)

    print_report(report, formatter)

def main(argv):
    if len(argv)==4:
        portfolio_report(argv[1], argv[2], argv[3])
    else:
        portfolio_report(argv[1], argv[2])

if __name__ == '__main__':
    argv = sys.argv
    main(argv)

