#!/usr/bin/python#
# Karl D. Melcher

# Advent of Code 2022
# day 01 Calorie Counting


# read lines until spaces or EOF
# last line in input file will be a blank line
# keep track each elf max
# stop once you hit blank or EOF
# return max
def rankElves(filename):
    with open(filename, 'r') as infile:
        lines = infile.readlines()
        maxSumList = []
        elfSum = 0
        for line in lines:
            line = line.strip()
            if (len(line) == 0):
                # print("elfSum=%d" % elfSum)
                maxSumList.append(elfSum)
                elfSum = 0
            else:
                # print("line=%s" % line)
                elfSum += int(line)
    return maxSumList


def day1a(filename):
    return max(rankElves(filename))


def day1b(filename):
    elves = rankElves(filename)
    assert len(elves) >= 3
    elves.sort(reverse=True)
    return sum(elves[:3])


print("Advent of Code day 01")

sample = day1a("day01.sample.input.txt")
print("part 1 sample data result: %d" % sample)
assert (sample == 24000)

day1aresult = day1a("day01.input.txt")
print("part 1 result: %d" % day1aresult)
assert (day1aresult == 65912)

# part 2

sample = day1b("day01.sample.input.txt")
print("part 2 sample data result: %d" % sample)
assert (sample == 45000)

day1bresult = day1b("day01.input.txt")
print("part 2 result: %d" % day1bresult)
assert (day1bresult == 195625)

print("Done.")
