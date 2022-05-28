import os
import csv
import json
from pathlib import Path

DATADIR = Path(os.getenv('KBC_DATADIR'))

INDIR = DATADIR / 'in'
OUTDIR = DATADIR / 'out'

CONFIG_FILE_PATH = DATADIR / 'config.json'
SOURCE_FILE_PATH = INDIR / 'tables' / 'input.csv'
RESULT_FILE_PATH = OUTDIR / 'tables' / 'output.csv'

with open(CONFIG_FILE_PATH) as f:
    cfg = json.load(f)

params = cfg['parameters']
PARAM_PRINT_LINES = params.get('print_lines', False)

print('Running...')
with open(SOURCE_FILE_PATH, 'r') as input, open(RESULT_FILE_PATH, 'w+', newline='') as out:
    reader = csv.DictReader(input)
    new_columns = reader.fieldnames
    # append row number col
    new_columns.append('row_number')
    writer = csv.DictWriter(out, fieldnames=new_columns, lineterminator='\n', delimiter=',')
    writer.writeheader()
    for index, l in enumerate(reader):
        # print line
        if PARAM_PRINT_LINES:
            print(f'Printing line {index}: {l}')
        # add row number
        l['row_number'] = index
        writer.writerow(l)
