#!/usr/bin/env python

import csv
import sys

with open(sys.argv[1], 'r') as f:
    values = csv.reader(f)
    respondents = {}
    for row in values:
        if row[0] == 'id':
            continue
        email = row[1].lstrip()
        respondents[email] = row

live_in_scotland = 0
yes_to_q2 = 0
for k,v in respondents.iteritems():
    if v[2] == ' scotland':
        live_in_scotland = live_in_scotland + 1
    if v[4] == ' 1':
        yes_to_q2 = yes_to_q2 + 1

print "%i people live in scotland" % live_in_scotland
print "%i people answered yes to q2" % yes_to_q2
