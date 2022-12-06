#!/usr/bin/python#
# Karl D. Melcher

# Advent of Code 2022
# day 06 Tuning Trouble


# detect first time the "markerLen" most recent
# chars were all different (no dups)
def processSignal(signal, markerLen):
    result = 0

    sample = []   # 4 most recent chars

    index = 0
    foundDup = True

    while index < len(signal) and foundDup:

        if len(sample) >= markerLen:
            del sample[0]
        sample.append(signal[index])

        # print("sample = [%s] (len=%d)" % (sample,len(sample)))

        if len(sample) >= markerLen:
            x = sample.copy()
            x.sort()
            # print("sample sorted = [%s]" % x)
            foundDup = False
            for j in range(0, markerLen-1):
                if x[j] == x[j+1]:
                    # print("found dup")
                    foundDup = True

        index += 1

    print("result is %d" % index)
    return index


# read lines until spaces or EOF
def mainA(filename, markerLen):
    result = ""
    with open(filename, 'r') as infile:
        lines = infile.readlines()

        for i in range(0, len(lines)):
            lines[i] = lines[i].rstrip()      # strip trailing spaces only
            result = processSignal(lines[i], markerLen)

    return result


print("Advent of Code day 05")

assert 7 == processSignal("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4)
assert 5 == processSignal("bvwbjplbgvbhsrlpgdmjqwftvncz", 4)
assert 6 == processSignal("nppdvjthqldpwncqszvftbrmjlhg", 4)
assert 10 == processSignal("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4)
assert 11 == processSignal("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4)


sample = mainA("day06.sample.input.txt", 4)
print("part 1 sample data result: \"%s\"" % sample)
assert sample == 7

result = mainA("day06.input.txt", 4)
print("part 1 result: %s" % result)
assert (result == 1343)

# part 2
print("\n Part 2 \n")

assert 19 == processSignal("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14)
assert 23 == processSignal("bvwbjplbgvbhsrlpgdmjqwftvncz", 14)
assert 23 == processSignal("nppdvjthqldpwncqszvftbrmjlhg", 14)
assert 29 == processSignal("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14)
assert 26 == processSignal("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14)

result = mainA("day06.input.txt", 14)
print("part 2 result: %d" % result)
assert (result == 2193)

print("Done.")
