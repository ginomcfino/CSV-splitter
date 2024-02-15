import csv
import math

'''
Notes:

currently:
- assumes input file has no errors
- takes 1 file at a time
'''

def split_csv_file(in_file:str, out_prefix:str, num_rows:int=None, num_cells:int=None, use_header=True):
    '''
    Splits a large CSV file either by number of rows or number of cells

    specify directory name in out_prefix to directly output files into a directory.
    '''
    assert num_rows or num_cells, "either num_rows or num_cells has to be used."

    # convert num_cells to num_rows if num_cells specified
    if num_cells:
        num_cols = get_num_columns(in_file)
        num_rows = math.floor(num_cells / num_cols)

    # begin iter in_file
    row_cnt = 0
    file_cnt = 0

    with open(in_file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        headers = next(reader) if use_header else None

        rows = [] # rows to write to out file
        for row in reader:
            rows.append(row)
            row_cnt += 1

            if row_cnt >= num_rows:
                write_to_csv(f"{out_prefix}_{file_cnt}.csv", rows, headers)
                file_cnt += 1
                # reset rows and row counts
                rows = []
                row_cnt = 0

        if rows:
            write_to_csv(f"{out_prefix}_{file_cnt}.csv", rows, headers)
            
def write_to_csv(outpath:str, rows:list, headers):
    with open(outpath, 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        if headers and headers:
            writer.writerow(headers)
        writer.writerows(rows)

def get_num_columns(in_file:str):
    with open(in_file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        first_row = next(reader)
        num_columns = len(first_row)
    return num_columns

def run_prog():
    print('*'*25 + ' executing program ' + '*'*25)
    inpath = input('Hello, what is the path to your CSV file? \n')
    use_headers = input('Does the CSV file have headers? (y/n) ')
    if 'y' in use_headers:
        use_headers = True
    else:
        use_headers = False
    outpath = input('Where do you want to save the output files? ex. \'out_path/prefix\'\n')
    cnt_rows = input('Do you want to count by number of rows? y or yes if rows, n or no if columns.\n')
    cnt_rows = cnt_rows.lower()
    rows_cnt = None
    cells_cnt = None
    if 'y' in cnt_rows:
        while not rows_cnt:
            try:
                rows_cnt = input('Please input a number for # of rows to split by: ')
                rows_cnt = int(rows_cnt)
            except:
                try:
                    rows_cnt = int(input('Please enter a valid number for # of rows: '))
                except:
                    return
    else:
        while not cells_cnt:
            try:
                cells_cnt = input('Please input a number for # of cells to count by: ')
                cells_cnt = int(input)
            except:
                try:
                    cells_cnt = int(input('Please enter a valid number for # of cells: '))
                except:
                    return
    split_csv_file(inpath, outpath, rows_cnt, cells_cnt, use_headers)

# if __name__=='__main__':
#     run_prog()