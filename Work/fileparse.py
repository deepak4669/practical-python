# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(rows, select_cols = None, types=None, has_headers=True, silence_errors=True):
    '''
    Parse a CSV file into list of records
    '''
    if select_cols and not has_headers:
        raise RuntimeError(f'Select argument requires headers')

    try:
        if has_headers:
            headers = next(rows)

        if select_cols:
            indices = [headers.index(col) for col in select_cols]
            headers = select_cols 
        else:
            indices = []

        records = []
        for row_number, row in enumerate(rows, start=1):
            if not row:
                continue

            if indices:
                row = [row[index] for index in indices]

            try:
                if types:
                    row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f'Row {row_number}: Couldn"t Convert {row}')
                    print(f'Row {row_number}: Reason {e}')

            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = row
            records.append(record)
    except TypeError as e:
        print(f'There is some conversion error {e}')
        raise

    return records

