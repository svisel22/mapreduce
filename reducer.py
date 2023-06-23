#!/usr/bin/env python

import sys

# The input will be in the form of key-value pairs
# It is sorted according to the key
# Each key value pair will be in a new line
# The key and the value are seperated by a tab (\t)
# The key is the payment type and the value is the sales

# Example input data (Key=Payment, Value=Sales)
# Input is ordered by the key
# Visa  205.96
# Cash  11.32
# Cash  444.19

# We want to sum all values with the same key
# Example output data (Key=Payment, Value=Sum of Sales)
# Visa  205.96
# Cash  455.51





count_threshold = 114
previous_key = None
count = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    key = data[0]

    if previous_key is not None and previous_key != key:
        if count > count_threshold:
            sys.stdout.write("{0}\n".format(previous_key))
        count = 0

    count += 1
    previous_key = key

if previous_key is not None and count > count_threshold:
    sys.stdout.write("{0}\n".format(previous_key))





























    





