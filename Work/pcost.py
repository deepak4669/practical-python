# pcost.py
import sys
import csv
from report import read_portfolio

def portfolio_cost(file_name):
    total_cost = 0.0

    portfolio = read_portfolio(file_name)

    for holding in portfolio:
        total_cost += holding['shares']*holding['price']

    return total_cost

def main(argv):
    total_cost = portfolio_cost(argv[1])
    print('Total Cost:', total_cost)

if __name__ == '__main__':
    argv = sys.argv
    main(argv)
