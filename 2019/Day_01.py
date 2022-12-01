#!/usr/bin/python


import math

# part 1(a)
#  100 lines of input



# calc fuel required based on mass (input value)
#  fuel = round_down(mass / 3) - 2 
def day1a(filename):
    sum = 0
    with open(filename, 'r') as infile:
        lines = infile.readlines()
        for line in lines:
            #print "line=%s" % line
            mass = int(line)
    
            #print "%d x %d x %d" % (l, w, h)
            fuel = math.floor(mass / 3) - 2
            print ("mass = %d, fuel = %d" % (mass, fuel))

            sum = sum + fuel
    print("sum is %d" % sum)

# calc fuel required based on mass (input value)
#  fuel = round_down(mass / 3) - 2 
# account for fuel for fuel 
def CalcFuel(mass):
    fuel = math.floor(mass / 3) - 2
    
    if (fuel > 0):
        return fuel + CalcFuel(fuel)
    else:
        return 0

def day1b(filename):
    sum = 0
    with open(filename, 'r') as infile:
        lines = infile.readlines()
        for line in lines:
            #print "line=%s" % line
            mass = int(line)
    
            #print "%d x %d x %d" % (l, w, h)
            fuel = CalcFuel(mass)
            print ("TOTAL mass = %d, fuel = %d" % (mass, fuel))

            sum = sum + fuel
    print("sum is %d" % sum)


# day1b("Day_01b.test")
day1b("Day_01a.input")
# correct 5055835

day1a("Day_01a.input")
#day1a("Day_01a.test")
# correct 3372463
