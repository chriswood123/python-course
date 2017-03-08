#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script for creating past dated git commits. For the github green dots.

Usage:

    >>> cheat 27/2 'my commit message'

    will trigger:

    >>>git commit -m 'my commit message
    >>>git commit --amend --no-edit --date='Wed 27 Feb 21:56:23 2016'
"""
import sys, subprocess, datetime, os

def commit(msg):
    """
    Will send:
    git commit -m 'your message'
    """
    cmd = "git commit -m '{0}' ".format(msg)
    if is_debug():
        print cmd
        return 0
    else:
        return subprocess.call(cmd)

def construct_date(date_str):
    now = datetime.datetime.now()
    # Get date elements
    date_elements = date_str.split('/')
    if get_date_format() == 'gb':
        day = int(date_elements[0])
        month = int(date_elements[1])
    elif get_date_format() == 'us':
        month = int(date_elements[0])
        day = int(date_elements[1])
    # Test if year defined
    # Set to current year if not
    if len(date_elements) == 3:
        year = int(date_elements[2])
        if year < 100:
            year = year + 2000
    else:
        year = now.year
    # Construct new date in format git likes
    new_date = datetime.datetime(year, month, day, now.hour, now.minute,
                now.second)
    return new_date.strftime('%a %d %b %H:%M:%S %Y')

def amend(date_str):
    """
    Will send:
    git commit --amend --no-edit --date='Wed 03 Feb 21:56:23 2016'
    """
    # Build git command string
    cmd = "git commit --amend --no-edit --date='{0}'".format(construct_date(date_str))
    if is_debug():
        print cmd
        return 0
    else:
        return subprocess.call(cmd)

def is_debug():
    try:
        if os.environ['DEBUG'] == 'true':
            return True
        else:
            return False
    except KeyError:
        return False

def get_date_format():
    try:
        date_format_env = os.environ['DATE_FORMAT'].lower()
        if date_format_env == 'gb':
            date_format = 'gb'
        elif date_format_env == 'us':
            date_format = 'us'
        else:
            date_format = 'gb'
    except KeyError:
        date_format = 'gb'
    return date_format

if is_debug():
    print "Debug mode"
# Check correct number of args given
# If too many infer that commit message not in quotes
if commit(sys.argv[2]) == 0:
    amend(sys.argv[1])
else:
    print "Please pass a date and 'message in quotes'"
