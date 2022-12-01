#!/usr/bin/python


#import text


def day2a(filename, noun, verb):
    sum = 0
    with open(filename, 'r') as infile:
        lines = infile.readlines()
        for line in lines:
            # load list of comma separated integers into a zero-based array 
            numbers = line.split(",") 
            print ("found %d numbers" % len(numbers))
            print (numbers)
            #for i in range(0,10):
            #    print (numbers[i])
            numbers[1] = str(noun)
            numbers[2] = str(verb)

            index = 0
            while index < len(numbers):
                print ("numbers[%d] = %d" % (index, int(numbers[index])))
                opCode = int(numbers[index])
                print ("opCode = %d" % opCode)

                if (opCode == 1):
                    print ("Got ADD")
                    a = int(numbers[int(numbers[index+1])])
                    b = int(numbers[int(numbers[index+2])])
                    dest = int(numbers[index+3])
                    numbers[dest] = a + b
                    print("[%d] = %d" % (dest,numbers[dest]))
                    index = index + 4
                elif (opCode == 2):
                    print ("Got MULT")
                    a = int(numbers[int(numbers[index+1])])
                    b = int(numbers[int(numbers[index+2])])
                    dest = int(numbers[index+3])
                    numbers[dest] = a * b
                    print("[%d] = %d" % (dest,numbers[dest]))
                    index = index + 4
                elif (opCode == 99):
                    print ("DONE")
                    index = 99999
                else:
                    print ("ERROR")
                    index = 99999
            print ("Result = %d" % numbers[0])
            return numbers[0]

    #print("sum is %d" % sum)

def day2b():
    for noun in range(0,100):
        for verb in range (0,100):
            result = day2a("Day_02a.input", noun, verb)
            if (result == 19690720):
                print ("FOUND IT: %d %d " % (noun, verb))
                return 
    



day2b()
# answer: 67 18
# day2a("Day_02a.test")
# day2a("Day_02a.input", 12, 2)
# wrong: 394702
# correct 3850704

#day1a("Day_01a.input")
#day1a("Day_01a.test")
