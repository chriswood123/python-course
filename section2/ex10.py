#!/usr/bin/env python

import csv
import sys


with open(sys.argv[1], 'r') as f:
    values = csv.reader(f)
    respondents = {}
    columns = []
    row_count = 1
    for row in values:
        if row_count == 1:
            columns = row
            row_count = row_count + 1
            continue
        column_count = 0
        for column in columns:
            column = column.strip(' ')
            if column == 'email':
                respondents[row[column_count]] = row
            column_count = column_count + 1

live_in_scotland = 0
yes_to_q2 = 0
respondents_hashed = {}
for k,v in respondents.iteritems():
    stripped_key = k.strip(' ')
    respondents_hashed[stripped_key] = {}
    col_count = len(columns) - 1
    while col_count > 0:
        stripped_column = columns[col_count].strip(' ')
        stripped_value = v[col_count].strip(' ')
        respondents_hashed[stripped_key][stripped_column] = stripped_value
        col_count = col_count - 1

print "%i people live in scotland" % live_in_scotland
print "%i people answered yes to q2" % yes_to_q2

for k,v in respondents_hashed.iteritems():
    print k
    print v
