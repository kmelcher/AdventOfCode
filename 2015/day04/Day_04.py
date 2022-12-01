#!/usr/bin/python

import hashlib

# Day 4


def day4a(puzzleInput, numZeros):
    i = 0
    while True:
        key = puzzleInput + str(i)
        #print ("key is %s" % key)
        m = hashlib.md5()
        #print("hash is %s" % m)
        m.update(key.encode('utf-8'))
        hash = m.hexdigest()
        #print "input %s hash %s" % (key, hash)

        matchCount = 0
        for pos in range(0, numZeros):
            if hash[pos] == "0":
                matchCount += 1
            else:
                break

        if matchCount == numZeros:
            print("input %s index %d hash %s" % (key, i, hash))
            return i
            break
        i += 1

#day4a("abcdef")

print( "part 1 is %d" % day4a("iwrupvqb", 5))
print( "part 2 is %d" % day4a("iwrupvqb", 6))