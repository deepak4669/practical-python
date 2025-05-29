# Abstract Base Class
class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit the single row of table data
        '''
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10+' ')*len(headers))

    def row(self, rowdata):
        for row in rowdata:
            print(f'{row:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Emit a table in CSV format
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Emit a table in HTML format
    '''
    def headings(self, headers):
        print('<tr>', end = '')
        for header in headers:
            print(f'<th>{header}</th>', end = '')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end = '')
        for d in rowdata:
            print(f'<td>{d}</td>', end = '')
        print('</tr>')

class FormatError(Exception):
    pass

def create_formatter(fmt = 'txt'):
    if fmt == 'txt':
        return TextTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter()
    elif fmt == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown Format Specified {fmt}')

def print_table(data, attrs, formatter):
    formatter.headings(attrs)
    
    for rowdata in data:
        curr_row = [str(getattr(rowdata, attr)) for attr in attrs]
        formatter.row(curr_row)

        


