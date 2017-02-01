#!/usr/bin/env python

integers = []
user_input = ''
total = 0
max_int = 0

while  user_input != 0:
    # Not bothered to wrap exception handling for non numeric input
    user_input = int(raw_input('Give me an int: '))
    integers.append(user_input)

for an_int in integers:
    total = total + an_int
    if an_int > max_int:
        max_int = an_int

print "Total: %s" % total
print "Max: %s" % max_int
