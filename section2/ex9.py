#!/usr/bin/env python

def email_has_one_at(text):
    at_count = 0
    for char in text:
        if char == '@':
            at_count = at_count + 1
    if at_count == 1:
        return True
    else:
        return False


def email_ends_with_dot_com(text):
    tld = text.split('.')[-1]
    if tld == 'com':
        return True
    else:
        return False

def email_has_no_spaces(text):
    string_index = text.find(' ')
    if string_index == -1:
        return True
    else:
        return False


def email_has_only_valid_chars(text):
    valid_chars = ['@', '.', '_', '-']
    for char in valid_chars:
        text = text.replace(char, '')
    return text.isalnum()

def is_valid_email(text):
    if email_has_one_at(text) and \
       email_ends_with_dot_com(text) and \
       email_has_only_valid_chars(text) and \
       email_has_no_spaces(text):
        return True
    else:
        return False

#Example tests:
assert is_valid_email("moe@moestavern.com")
assert not is_valid_email("moe@@moestavern.com")
assert is_valid_email("moe@moestavern.springfield.com")
assert not is_valid_email("moe@moestavern.net")
assert not is_valid_email("m oe@moestavern.com")
assert is_valid_email("moe-szyslak@moestavern.com")
assert is_valid_email("moe_szyslak@moestavern.com")
assert not is_valid_email("moe$szyslak@moestavern.com")
