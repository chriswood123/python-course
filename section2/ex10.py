#!/usr/bin/env python

import csv
import sys

filename = sys.argv[1]

def is_reposnse_yes(response):
    if response in ['1', 'Yes', 'yes', 'y']:
        return True
    else:
        return False

def generate_reposnse_list(values):
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
    return (respondents, columns)

def generate_reposnse_dict(response_list, columns):
    respondents_hashed = {}
    for k, v in response_list.iteritems():
        stripped_key = k.strip(' ')
        respondents_hashed[stripped_key] = {}
        col_count = len(columns) - 1
        while col_count > 0:
            stripped_column = columns[col_count].strip(' ')
            stripped_value = v[col_count].strip(' ')
            respondents_hashed[stripped_key][stripped_column] = stripped_value
            col_count = col_count - 1
    return respondents_hashed

def combine_surveys(surveys):
    combined_survey = {}
    for survey in surveys:
        for key, value in survey.iteritems():
            combined_survey[key] = value
    return combined_survey

surveys = []
for arg in sys.argv[1:]:
    sys.argv[1:]
    values = []
    with open(arg, 'r') as f:
        lines = csv.reader(f)
        for line in lines:
            values.append(line)
    response_list, columns = generate_reposnse_list(values)
    response_dict = generate_reposnse_dict(response_list, columns)
    surveys.append(response_dict)

combined_survey = combine_surveys(surveys)
live_in_scotland = 0
yes_to_q2 = 0
for k, v in combined_survey.iteritems():
    #print "%s: %s" % (k, v)
    if v['country'] == 'scotland':
        live_in_scotland = live_in_scotland + 1
    if is_reposnse_yes(v['q2']):
        yes_to_q2 = yes_to_q2 + 1

print "%i people live in scotland" % live_in_scotland
print "%i people answered yes to q2" % yes_to_q2

