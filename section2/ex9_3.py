#!/usr/bin/env python
# coding: utf-8

def remove_duplicates(items):
    items_dict = {}
    # create a dict of unique items as keys
    for item in items:
        items_dict[item] = 0
    # set the values of dict keys to count of name occurances
    for key in items_dict.keys():
        for item in items:
            if item == key:
                items_dict[key] = items_dict[key] + 1
    # remove nanes from items list until only one occurance remaining
    for key, value in items_dict.iteritems():
        while value > 1:
            items.remove(key)
            value = value - 1
    return items

a = ["tom", "tom", "jane", "bob", "jim", "jane", "bob", "jane", "jane", "tom"]
remove_duplicates(a)

print(a)
