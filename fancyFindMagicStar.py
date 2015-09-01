import itertools
import random
import copy

allValues = [ x for x in range(1,13) ]
star = { "A" : , "B" : , "C" : , "D" : , "E" : , "F" : ,
         "G" : , "H" : , "I" : , "J" : , "K" : , "L" : }

constrainIndex = [[0,2,5,7], [1,2,3,4], [0,3,6,10], [7,8,9,10], [1,5,8,11], [4,6,9,11]]
combinations = [ "BCDE", "ACFH", "ADGK", "HIJK", "EGJL", "BFIL" ]

def sum_combination(dictio,index):
    sum = 0
    for position in combinations[index]:
        sum += dictio[position]
    return sum

count = 0
for permut4 in itertools.permutations(allValues,4):
    if sum(permut4) == 26:
        lessValues8 = copy.deepcopy(allValues)
        for value in permut4:
            
            lessValues8.remove(value)

        for permut3 in itertools.permutations(lessValues8,3):
            if sum(permut3) + permut4[2] == 26:
                lessValues5 = copy.deepcopy(lessValues8)

                for value in permut3:
                    #print " Removing value ",value," from list ",lessValues5)
                    lessValues5.remove(value)
                #print " Remaining values: ",lessValues5

                for permut2 in itertools.permutations(lessValues5,2):
                    if sum(permut2) + permut4[0] + permut3[2] == 26:
                        lessValues3 = copy.deepcopy(lessValues5)

                        for value in permut2:
                            #print " Removing value ",value," from list ",lessValues3)
                            lessValues3.remove(value)
                        #print " Remaining values: ",lessValues3

                        for permut1 in itertools.permutations(lessValues3,2):
                            if sum(permut1) + permut4[2] + permut3[0] == 26:
                                lessValues1 = copy.deepcopy(lessValues3)

                                for value in permut1:
                            #print " Removing value ",value," from list ",lessValues3)
                                    lessValues1.remove(value)
                                #print " Remaining value: ",lessValues1

                                if permut3[2] + permut2[1] + permut1[1] + lessValues1[0] == 26:
                                    print "Success!"
                                    print " First line: ",permut4
                                    print " Second line: ",permut3," ",permut4[2]
                                    print " Third line: ",permut2," ",permut4[0],permut3[2]
                                    print " Fourth line: ",permut1," ",permut4[2],permut3[0]
                                    break

count += 1
if count == 20:
    input("continue?")
    count = 0
