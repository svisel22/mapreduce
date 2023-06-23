#!/usr/bin/env python

# Import the sys library 
# for writing and reading the standard input and output
import sys

# Example Input data (minipurchase.txt)
# Input is tabulator (\t) separated
# New Line (\n) indicates a new record.
# Input will be piped into the standard input (e.g. with cat on the command line)
# Fields (Date, Time, Item, Category, Sales, Payment):
# 2012-12-31	16:26	Anaheim	Men's Clothing		205.96	Visa
# 2012-12-31	16:29	Irvine	Women's Clothing	22.47		Cash
# 2012-12-31	16:30	Laredo	Women's Clothing	444.19	Cash

# The mapper transforms the input into key-value pairs.
# We are only interested in the payment and the sales
# We create pairs of payment type (key) and sales (value)
# The values are not yet aggregated! (This is done by the reducer)

# Example Output data (Key=payment, Value=Sales)
# Visa		205.96
# Cash		11.32
# Cash		444.19
# Output is tabulator (\t) separated 
# New Line (\n) indicates a new record
# Output is writing to the standard output

# For each new line in the standard input (stdin) 


for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 6:
        raise ValueError("Invalid input: Tuple does not have six elements")
    date, time, item, category, sales, payment = data
    
    if category in ['Computers', 'Cameras', 'Video Games']:
        sys.stdout.write("{0}\t{1}\n".format(category, sales))





