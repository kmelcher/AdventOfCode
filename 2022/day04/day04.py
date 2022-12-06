#!/usr/bin/python#
# Karl D. Melcher

# Advent of Code 2022
# day 04 Camp Cleanup


def contains(rangeA, rangeB):
    (a1, a2) = rangeA.split("-")
    (b1, b2) = rangeB.split("-")
    return int(a1) >= int(b1) and int(a2) <= int(b2)


# visual display of range
def showRange(rangeIn):
    (a1, a2) = rangeIn.split("-")
    a1 = int(a1)
    a2 = int(a2)

    for i in range(0, 10, 1):
        if (i >= a1) and i <= a2:
            print(i, end='')
        else:
            print(".", end='')
    print()


# read lines until spaces or EOF
def day04a(filename):
    result = 0

    with open(filename, 'r') as infile:
        lines = infile.readlines()

        for line in lines:
            line = line.strip()
            # print("input=%s" % line)
            # split compartement content
            (rangeA, rangeB) = line.split(",")
            # print("\nA=:%s B=%s" % (rangeA, rangeB))
            # showRange(rangeA)
            # showRange(rangeB)
            if contains(rangeA, rangeB) or contains(rangeB, rangeA):
                result += 1

    return result


def overlap(rangeA, rangeB):
    (a1, a2) = rangeA.split("-")
    (b1, b2) = rangeB.split("-")
    return not (int(a2) < int(b1) or int(a1) > int(b2))


# read lines until spaces or EOF
def day04b(filename):
    result = 0

    with open(filename, 'r') as infile:
        lines = infile.readlines()

        for line in lines:
            line = line.strip()
            # print("input=%s" % line)

            (rangeA, rangeB) = line.split(",")
            # showRange(rangeA)
            # showRange(rangeB)

            if overlap(rangeA, rangeB) or overlap(rangeB, rangeA):
                result += 1

    return result


print("Advent of Code day 04")

sample = day04a("day04.sample.input.txt")
print("part 1 sample data result: %d" % sample)
assert (sample == 2)

sample = day04a("day04.sample2.input.txt")
print("part 1 sample2 data result: %d" % sample)
assert (sample == 8)

result = day04a("day04.input.txt")
print("part 1 result: %d" % result)
assert (result == 496)

# part 2
print("\n Part 2 \n")

sample = day04b("day04.sample.input.txt")
print("part 2 sample data result: %d" % sample)
assert (sample == 4)

sample = day04b("day04.sample2.input.txt")
print("part 2 sample2 data result: %d" % sample)
assert (sample == 13)

result = day04b("day04.input.txt")
print("part 2 result: %d" % result)
assert (result == 847)

print("Done.")
