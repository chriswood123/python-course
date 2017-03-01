#!/usr/bin/env python

import csv
import sys

filename = sys.argv[1]

def is_reposnse_yes(response):
    if response in ['1', 'Yes', 'yes', 'y']:
        return True
    else:
        return False

def generate_reposnse_hash(values):
    respondents = {}
    columns = []
    row_count = 1
    for row in values:
        if row_count == 1:
            # if it's the first row grab the column labels
            columns = row
            row_count = row_count + 1
            continue
        column_count = 0
        for column in columns:
            column = column.strip(' ')
            if column == 'email':
                respondents[row[column_count]] = row
            column_count = column_count + 1
    # Turn hash with lists of responses as the value in to
    # hash with hashes of responses as value
    respondents_hashed = {}
    for k, v in respondents.iteritems():
        stripped_key = k.strip(' ')
        respondents_hashed[stripped_key] = {}
        col_count = len(columns) - 1
        while col_count > 0:
            stripped_column = columns[col_count].strip(' ')
            stripped_value = v[col_count].strip(' ')
            respondents_hashed[stripped_key][stripped_column] = stripped_value
            col_count = col_count - 1
    return respondents_hashed

surveys = []
for arg in sys.argv:
    if arg != sys.argv[0]:
        values = []
        with open(arg, 'r') as f:
            lines = csv.reader(f)
            for line in lines:
                values.append(line)
        surveys.append(generate_reposnse_hash(values))

# TODO: Join the muliple surveys, removing dupes, etc.
responses = surveys[1]
live_in_scotland = 0
yes_to_q2 = 0
for k, v in responses.iteritems():
    #print "%s: %s" % (k, v)
    if v['country'] == 'scotland':
        live_in_scotland = live_in_scotland + 1
    if is_reposnse_yes(v['q2']):
        yes_to_q2 = yes_to_q2 + 1

print "%i people live in scotland" % live_in_scotland
print "%i people answered yes to q2" % yes_to_q2

