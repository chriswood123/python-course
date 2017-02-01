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
