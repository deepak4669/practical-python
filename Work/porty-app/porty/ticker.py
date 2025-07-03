from .follow import follow
from . import report
import csv
from . import tableformat

def ticker(portfile, logfile, fmt='txt'):
    portfolio = report.read_portfolio(portfile)
    rows = parse_stock_data(follow(logfile))
    rows = filter_symbols(rows, portfolio)

    formatter = tableformat.create_formatter(fmt)
    headers = ['Name', 'Price', 'Change']
    formatter.headings(headers)

    for row in rows:
        rowdata = [row['name'], f'{row['price']:0.2f}', f'{row['diff']:0.2f}']
        formatter.row(rowdata)

def filter_symbols(rows, names):
    return (row for row in rows if row['name'] in names)

def convert_types(rows, types):
    return ([func(val) for func, val in zip(types, row)] for row in rows)

def make_dicts(rows, headers):
    return (dict(zip(headers, row)) for row in rows)

def select_columns(rows, indices):
    return ([row[index] for index in indices] for row in rows)

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'diff'])
    return rows

if __name__ == '__main__':
    lines = follow('Data/stocklog.csv')
    rows = parse_stock_data(lines)
    for row in rows:
        print(row)
