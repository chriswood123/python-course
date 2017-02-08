#!/usr/bin/env python

# Make sure nothing below here runs
quit()

#
# Use built in functions
#
ints = []

while True:
    i = int(raw_input("Give me a number:"))
    if i == 0:
        break
    ints.append(i)
# Rather than a for loop to compare and add (see section2/ex2.py)
print 'largest: ', max(ints)
print 'total: ', sum(ints)

#
# The assert statement evaluates a condition (in this case various equality tests) and will cause Python to quit if false, and do nothing if true.
#
assert parse_dim_string("45 20 15") == [45, 20, 15]

