#!/usr/bin/env python

def remove_duplicates(items):
    counts = {}
    unduplicated = []
    for item in items:
        counts[item] = 0
    for key in counts.keys():
        unduplicated.append(key)
    return unduplicated

a = ["tom", "tom", "jane", "bob", "jim", "jane", "bob", "jane"]
b = remove_duplicates(a)

print(b)
