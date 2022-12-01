# Advent of Code 2020  
# Day 01 a
#
# read input file
# Find 2 entries that add up to 2020
# multiple them to get the solution


# read all entries into a dictionary 
# iterate over them.  Calc target = 2020 - value.
# If target exists, multiple them and done.

def day1a(filename):
    dict = {}
    with open(filename, 'r') as infile:
        lines = infile.readlines()
        for line in lines:
            print("line=%s" % line)
            dict[line]

    



day1a("Day_01a.input")