#!/usr/bin/python#
# Karl D. Melcher

# Advent of Code 2022
# day 03 The Rucksack filler


def findCommonChar(s1, s2):
    # print("s1:%s" % s1)
    # print("s2:%s" % s2)

    for char1 in s1:
        for char2 in s2:
            if char1 == char2:
                return char1


# read lines until spaces or EOF
def day03a(filename):
    result = 0

    with open(filename, 'r') as infile:
        lines = infile.readlines()

        for line in lines:
            line = line.strip()
            # print("input=%s" % line)
            # split compartement content
            half = int(len(line)/2)
            c1 = line[:half]
            c2 = line[half:]
            # print("c1:%s" % c1)
            # print("c2:%s" % c2)
            dup = findCommonChar(c1, c2)
            if (dup >= 'a' and dup <= 'z'):
                score = ord(dup) - ord('a') + 1
            else:
                score = ord(dup) - ord('A') + 27
            # print("common = %s %d" % (dup,score))

            result += score

    return result


def findCommonChar3(s1, s2, s3):

    for char1 in s1:
        for char2 in s2:
            for char3 in s3:
                if (char1 == char2) and (char1 == char3):
                    return char1


# read lines until spaces or EOF
def day03b(filename):
    result = 0

    with open(filename, 'r') as infile:
        lines = infile.readlines()

        assert (len(lines) % 3 == 0)   # must be multiple of 3 lines

        for firstLine in range(0, len(lines), 3):
            half = int(len(lines)/2)
            s1 = lines[firstLine].strip()
            s2 = lines[firstLine+1].strip()
            s3 = lines[firstLine+2].strip()

            dup = findCommonChar3(s1, s2, s3)

            if (dup >= 'a' and dup <= 'z'):
                score = ord(dup) - ord('a') + 1
            else:
                score = ord(dup) - ord('A') + 27

            # print("common = %s %d" % (dup,score))

            result += score

    return result


# print("Advent of Code day 03")

sample = day03a("day03.sample.input.txt")
# print("part 1 sample data result: %d" % sample)
assert (sample == 157)


result = day03a("day03.input.txt")
# print("part 1 result: %d" % result)
assert (result == 8233)

# part 2
# print("\n Part 2 \n")

sample = day03b("day03.sample.input.txt")
# print("part 1 sample data result: %d" % sample)
assert (sample == 70)

result = day03b("day03.input.txt")
# print("part 2 result: %d" % result)
assert (result == 2821)

# print("Done.")
