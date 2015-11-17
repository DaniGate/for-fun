#!/usr/bin/python


import itertools
import random
import copy
import time

class MagicStar:

    def __init__(self,nPoints):
        self.nPoints = nPoints
        self.listPositions = "ABCDEFGHIJKL"
        self.star = { "A" : 0 ,
                      "B" : 0 ,
                      "C" : 0 ,
                      "D" : 0 ,
                      "E" : 0 ,
                      "F" : 0 ,
                      "G" : 0 ,
                      "H" : 0 ,
                      "I" : 0 ,
                      "J" : 0 ,
                      "K" : 0 ,
                      "L" : 0 }
        self.newstar = [ ]
        self.nValues = nPoints * 2
        self.nConstrains = nPoints

        if self.nPoints == 6:
            self.magicConstant = 26
            self.combinations = [ "ACFH" , "BCDE" , "BFIL" , "ADGK" , "HIJK" , "EGJL" ]
#            self.constrainIndex = [[0,2,5,7], [1,2,3,4], [0,3,6,10], [7,8,9,10], [1,5,8,11], [4,6,9,11]]
            self.spacedValues = [2,3,4,8,9,10]
            self.emptyPositions = [ self.combinations[0] , "JL" , "GK" , "I" ]
        if self.nPoints == 7:
            self.magicConstant = 30
            self.star["M"] = 0
            self.star["N"] = 0
            self.combinations = [ "ACEG" , "ADHJ" , "BCDF" , "BEIM" , "FHKN" , "GILN" , "JKLM" ]
            self.listPositions += "MN"
#            self.constrainIndex = [[0,2,4,6], [0,3,7,9], [1,2,3,5], [1,4,8,12], [5,7,10,13], [6,8,11,13], [9,10,11,12]]
            self.spacedValues = []
            self.emptyPositions = [ self.combinations[0] , "JL" , "GK" , "I" ]
        if self.nPoints == 8:
            self.magicConstant = 34
            self.star["M"] = 0
            self.star["N"] = 0
            self.star["O"] = 0
            self.star["P"] = 0
#            A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P
#            0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
            self.combinations = [ "ACFH" , "ADGI" , "BCDE" , "BFJL" , "EGKO" , "HJMP" , "IKNP" , "LMNO" ]
#            self.constrainIndex = [[0,2,5,7], [0,3,6,8], [1,2,3,4], [1,5,9,11], [4,6,10,14], [7,9,12,15], [8,10,13,15], [11,12,13,14]]
            self.spacedValues = []
            self.listPositions += "MNOP"
            self.emptyPositions = [ self.combinations[0] , "JL" , "GK" , "I" ]

    def printParameters(self):
        print str(self.nPoints)+" Points"
        print str(self.nValues)+" Values"
        print str(self.nConstrains)+" Constrains"
        return

    def getStar(self):
        return self.star


    def randomStar(self):
        orderedStar = [ x for x in range(1,self.nValues+1) ]
        randomStar = [ ]

        print("Star with "+str(self.nPoints)+" points ==> Values from 1 to "+str(self.nValues))
        for i in range(self.nValues):
            randomIndex = random.randint(1,len(orderedStar))-1
            randomStar.append(orderedStar[randomIndex])
            orderedStar.remove(orderedStar[randomIndex])

        for i in range(len(self.listPositions)):
            self.star[self.listPositions[i]] = randomStar[i]

        return self.star

    def findStar(self):
        """ Find a solution to the magic star puzzle """

        print "Star with "+str(self.nPoints)+" points ==> Values from 1 to "+str(self.nValues)

        def sum_combination(combination):
            sum = 0
            for position in combination:
                sum += self.star[position]
            return sum

        def print_combination(combination):
            print "%s = " % combination,
            for position in combination:
                print self.star[position]," + ",
            print " = ",sum_combination(combination)
            return

        allValues = [x for x in range(1,self.nValues+1)]
        count = 0
        for permut4 in itertools.permutations(allValues,4):
            count4 = 0
            for pos4 in self.emptyPositions[0]:
                # Fill the empty positions of the star with the numbers of the current iteration
                self.star[pos4] = permut4[count4]
                count4 += 1
            if sum_combination(self.combinations[0]) == self.magicConstant:
                lessValues8 = copy.deepcopy(allValues)
                for value in permut4:
                    lessValues8.remove(value)

                for permut3 in itertools.permutations(lessValues8,3):
                    count3 = 0
                    for pos3 in self.emptyPositions[1]:
                        # Fill the empty positions of the star with the numbers of the current iteration
                            self.star[pos3] = permut3[count3]
                            count3 += 1
                    if sum_combination(self.combinations[1]) == self.magicConstant:
                        lessValues5 = copy.deepcopy(lessValues8)
                        for value in permut3:
                            lessValues5.remove(value)
                        #print " Remaining values: ",lessValues5
# DOES NOT WORK BEYOND THIS POINT!
                        for permut2a in itertools.permutations(lessValues5,2):
                            count2a = 0
                            for pos2a in self.emptyPositions[2]:
                        # Fill the empty positions of the star with the numbers of the current iteration
                                self.star[pos2a] = permut2a[count2a]
                                count2a += 1
                            if sum_combination(self.combinations[2]) == self.magicConstant:
                                lessValues3 = copy.deepcopy(lessValues5)

                                for value in permut2a:
                                    lessValues3.remove(value)
                                #print " Remaining values: ",lessValues3

                                for permut2b in itertools.permutations(lessValues3,2):
                                    count2b = 0
                                    for pos2b in self.emptyPositions[3]:
                                        # Fill the empty positions of the star with the numbers of the current iteration
                                        self.star[pos2b] = permut2b[count2b]
                                        count2b += 1
                                    if sum_combination(self.combinations[3]) == self.magicConstant:
                                        lessValues1 = copy.deepcopy(lessValues3)
                                        print_combination(self.combinations[1])

                                        if self.magicConstant > 6:
                                            count2c = 0
                                            for pos2c in self.emptyPositions[4]:
                                                # Fill the empty positions of the star with the numbers of the current iteration
                                                self.star[pos2c] = permut2c[count2c]
                                                count2c += 1
                                            if sum_combination(self.combinations[4]) == self.magicConstant:
                                                lessValues1 = copy.deepcopy(lessValues3)

                                            if self.magicConstant > 7:
                                                count2d = 0
                                                for pos2d in self.emptyPositions[5]:
                                                    # Fill the empty positions of the star with the numbers of the current iteration
                                                    self.star[pos2d] = permut2d[count2d]
                                                    count2d += 1
                                                    if sum_combination(self.combinations[5]) == self.magicConstant:
                                                        lessValues1 = copy.deepcopy(lessValues3)
                                                        for value in permut2c:
                                                            lessValues1.remove(value)
                                            else:
                                                for value in permut2d:
                                                    lessValues1.remove(value)
                                        else:
                                            for value in permut2b:
                                                lessValues1.remove(value)
                                        #print " Remaining value: ",lessValues1

                                        count3 = 0
                                        for pos3 in self.emptyPositions[3]:
                                            # Fill the empty positions of the star with the numbers of the current iteration
                                            self.star[pos3] = permut3[count3]
                                            count3 += 1

                                        if sum_combination(self.combinations[4]) == self.magicConstant:
                                            print "Success!"
                                            print " First line: ",permut4
                                            print " Second line: ",permut3," ",permut4[2]
                                            print " Third line: ",permut2," ",permut4[0],permut3[2]
                                            print " Fourth line: ",permut2b," ",permut4[2],permut3[0]
                                            break

                                        count += 1
                                        if count == 20:
                                            input("continue?")
                                            count = 0


    def printStar(self):
        """ Print the current star on screen """
        pos = { "A" : "" }
        for letter in self.listPositions:
            if self.star[letter] < 10:
                if self.star[letter] in self.spacedValues:
                    pos[letter] = "-"+str(self.star[letter])
                else:
                    pos[letter] = " "+str(self.star[letter])
            else:
                pos[letter] = str(self.star[letter])

        if self.nPoints == 6:
            print "            ",pos["A"]
            print "              /  \           "
            print "             /    \          "
            print pos["B"],"----",pos["C"],"----",pos["D"],"----",pos["E"]
            print "   \      /           \     / "
            print "     \  /     ~~     \  / "
            print "    ",pos["F"],"      |",self.magicConstant,"|    ",pos["G"]
            print "     /  \     ~~     /  \ "
            print "    /     \           /     \ "
            print pos["H"],"----",pos["I"],"----",pos["J"],"----",pos["K"]
            print "             \    /          "
            print "              \  /           "
            print "            ",pos["L"],"           "
            print

        return


def measureMeanTime(star):
    """ Calculate the mean time to run findStar() """

    mean = 0.0
    N = 20
    i = 0
    while i < N:
        before = time.clock()
        star.findStar()
        after = time.clock()
        print after-before," ticks"
        mean += after - before
        i += 1

    mean /= N
    print mean," mean ticks"
    return mean
