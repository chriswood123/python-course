#!/usr/bin/env python

first_int = int(raw_input("First integer: "))
second_int = int(raw_input("Second integer: "))

if first_int > second_int:
    print "First integer is highest: " + str(first_int)
elif first_int < second_int:
    print "Second integer is highest: " + str(second_int)
else:
    print "Both integers are equal"


