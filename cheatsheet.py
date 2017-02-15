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

#
# Return conditional result
#
# Rather than
if thing == other_thing:
    return True
else:
    return False
# You can do this
return thing == other_thing

#
# 'in' operator
stuff = ['mouse', 'keyboard', 'monitor']
if 'mouse' in stuff:
    print 'yay'

#
# set built in type
#
# like a list but unique elements only
names = ["tom", "tom", "jane", "bob", "jim", "jane", "bob", "jane"]
print set(names)
# output: set(['jane', 'bob', 'jim', 'tom'])
# can convert back in to a list:
print list(set(names))
# output: ['jane', 'bob', 'jim', 'tom']

#
# Function defaults are created when the function is defined rather then when called
# This can cause issues with mutable defaults, e.g.
def append_to(element, to=[]):
    to.append(element)
    return to

print(append_to(12))
print(append_to(14))
# Outputs:
# [12]
# [12, 14]
# You can solve this like so
def append_to(element, to=None):
    if to is None:
        to = []
    to.append(element)
    return to
