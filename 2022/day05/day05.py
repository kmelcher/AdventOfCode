#!/usr/bin/python#
# Karl D. Melcher

# Advent of Code 2022
# day 05 Supply Stacks

import io


# find and return the index of the line with the stack numbers " 1..2..3"
def findStackNumbers(lines):
    for i in range(0, len(lines)):
        line = lines[i].strip()
        # print("line=%s" % line)
        if line[0] == '1':
            return i
    assert True  # did not find it!


# strip the square brackets off and return just the letter
def getCrateLetter(crateText):
    return crateText[1:2].strip()


def loadStacks(lines, stackEndIndex):
    # get the number of stacks by finding the biggest number
    nums = lines[stackEndIndex].split()
    # print("last num is %s" % nums[-1])
    numStacks = int(nums[-1])
    # print("num stacks is %d" % numStacks)

    # a stack is just a list
    # make a list of lists
    stacks = []
    for i in range(0, numStacks):
        stacks.append([])

    # starting on the bottom, read the stack rows and push content
    # on stacks(queues) if not empty
    for i in range(stackEndIndex-1, -1, -1):
        # print("processing row %d (len=%d)" % (i,len(lines[i])))
        # print("{%s}" % lines[i])
        # each stack has text 4 chars wide.
        for j in range(0, numStacks):
            # print("j=%d" % j)
            if (j*4 >= len(lines[i])):  # Watch for empty stacks at end.
                # print("nothing left...")
                break
            crate = getCrateLetter((lines[i])[j*4:j*4+4])
            # print("found crate {%s}" % crate)
            if len(crate) > 0:
                stacks[j].append(crate)

    return stacks


# possibly use this to write a better "showStacks()"
def print_to_string(*args, **kwargs):
    output = io.StringIO()
    print(*args, file=output, **kwargs)
    contents = output.getvalue()
    output.close()
    return contents


def showStacks(stacks):
    print("Stacks: (%d)" % len(stacks))
    for i in range(0, len(stacks)):
        for j in range(0, len(stacks[i])):
            print("stk:%d %d %s" % (i, j, stacks[i][j]))


def getTopRow(stacks):
    topStr = ""

    # print("%d stacks" %len(stacks))
    for i in range(0, len(stacks)):
        s = stacks[i]
        # print("stack %d len=%d" % (i,len(s)))
        top = len(s)-1
        if top < 0:
            print("empty")
        else:
            # print("%s" % (s[top]))
            topStr += s[top]
    return topStr


def processMoves(firstMoveIndex, lines, stacks, craneModel):
    for line in lines[firstMoveIndex:]:
        line = line.strip()
        # print("%s" % line)

        parts = line.split()
        count = int(parts[1])
        fromStackIndex = int(parts[3]) - 1  # adjust for index
        toStackIndex = int(parts[5]) - 1

        fromStack = stacks[fromStackIndex]
        toStack = stacks[toStackIndex]
        if craneModel == 9000:
            for i in range(0, count):
                crate = fromStack.pop()
                toStack.append(crate)

        elif craneModel == 9001:
            crates = []
            for i in range(0, count):
                crates.append(fromStack.pop())
            crates.reverse()
            for i in range(0, count):
                toStack.append(crates[i])

        else:
            print("bad model crane.")
            assert True


# read lines until spaces or EOF
def day05a(filename, craneModel):
    result = ""
    with open(filename, 'r') as infile:
        lines = infile.readlines()

        for i in range(0, len(lines)):
            lines[i] = lines[i].rstrip()      # strip trailing spaces only

        stackEndIndex = findStackNumbers(lines)
        # print("Stack end index is %d" % stackEndIndex)

        stacks = loadStacks(lines, stackEndIndex)
        # showStacks(stacks)
        result = getTopRow(stacks)

        firstMoveIndex = stackEndIndex + 2
        processMoves(firstMoveIndex, lines, stacks, craneModel)

        # showStacks(stacks)
        result = getTopRow(stacks)

    return result


print("Advent of Code day 05")

sample = day05a("day05.sample.input.txt", 9000)
print("part 1 sample data result: \"%s\"" % sample)
assert (sample == "CMZ")

result = day05a("day05.input.txt", 9000)
print("part 1 result: %s" % result)
assert (result == "VRWBSFZWM")

# part 2
print("\n Part 2 \n")

sample = day05a("day05.sample.input.txt", 9001)
print("part 1 sample data result: \"%s\"" % sample)
assert (sample == "MCD")

result = day05a("day05.input.txt", 9001)
print("part 1 result: %s" % result)
assert (result == "RBTWJWMCF")

print("Done.")
