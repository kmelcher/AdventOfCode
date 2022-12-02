#!/usr/bin/python# 
# Karl D. Melcher

# Advent of Code 2022
# day 02 Rock Paper Scissors

# rock beats scissors
# scissors beats paper 
# Paper beats rock


rockCode = "A"
paperCode = "B"
scissorCode = "C"

myPlayRock = "X"
myPlayPaper = "Y"
myPlayScissors = "Z"

resultDraw = "Y"
resultLoss = "X"
resultWin = "Z"

rockScore = 1
paperScore = 2
scissorScore = 3

lossScore = 0
drawScore = 3
winScore = 6

# read lines until spaces or EOF
def play(filename):
    with open(filename, 'r') as infile:
        lines = infile.readlines()

        totalScore = 0
        
        for line in lines:
            roundScore = 0
            line = line.strip()
            (opponentPlay, myPlay) = line.split(' ')
            print ("play: op=%s me=%s" % (opponentPlay, myPlay))
                
            if opponentPlay == rockCode:
                if myPlay == myPlayRock:
                    roundScore += rockScore + drawScore
                    #print("Draw")
                elif myPlay == myPlayPaper:
                    #print("win")
                    roundScore += paperScore + winScore
                else: # scissors
                    roundScore += scissorScore + lossScore
                    #print("loss")
            elif opponentPlay == paperCode:
                #print("paper")
                if myPlay == myPlayRock:
                    roundScore += rockScore + lossScore
                    #print("Loss")
                elif myPlay == myPlayPaper:
                    #print("draw")
                    roundScore += paperScore + drawScore
                else: # scissors
                    roundScore += scissorScore + winScore
                    #print("win")
               
            elif opponentPlay == scissorCode:
                #print("scissors")
                if myPlay == myPlayRock:
                    roundScore += rockScore + winScore
                    #print("win")
                elif myPlay == myPlayPaper:
                    #print("loss")
                    roundScore += paperScore + lossScore
                else: # scissors
                    roundScore += scissorScore + drawScore
                    #print("draw")
            else:
                print("default")
            
            totalScore += roundScore
            
            print("round=%d, total=%d" % (roundScore, totalScore))    
                        

    return totalScore

# read lines until spaces or EOF
def play2(filename):
    with open(filename, 'r') as infile:
        lines = infile.readlines()

        totalScore = 0
        
        for line in lines:
            roundScore = 0
            line = line.strip()
            (opponentPlay, result) = line.split(' ')
            print ("play: op=%s result=%s" % (opponentPlay, result))
                
            if opponentPlay == rockCode:
                if result == resultWin:
                    roundScore += paperScore + winScore
                elif result == resultDraw:
                    roundScore += rockScore + drawScore
                else: # loss
                    roundScore += scissorScore + lossScore
            elif opponentPlay == paperCode:
                if result == resultWin:
                    roundScore += scissorScore + winScore
                elif result == resultDraw:
                    roundScore += paperScore + drawScore
                else: # loss
                    roundScore += rockScore + lossScore
               
            elif opponentPlay == scissorCode:
                if result == resultWin:
                    roundScore += rockScore + winScore
                elif result == resultDraw:
                    roundScore += scissorScore + drawScore
                else: # loss
                    roundScore += paperScore + lossScore
            else:
                print("default")
            
            totalScore += roundScore
            
            print("round=%d, total=%d" % (roundScore, totalScore))    
                        

    return totalScore
  


print("Advent of Code day 02")        
        
sample = play("day02.sample.input.txt")
print( "part 1 sample data result: %d" % sample)
assert (sample == 15)


day2aresult = play("day02.input.txt")
print( "part 1 result: %d" % day2aresult)
assert (day2aresult == 11063)

# part 2
print("\n")

sample = play2("day02.sample.input.txt")
print( "part 2 sample data result: %d" % sample)
assert (sample == 12)

day2bresult = play2("day02.input.txt")
print( "part 2 result: %d" % day2bresult)
assert (day2bresult == 10349)

print("Done.")