import itertools
import random
import copy
import time


def sum_combination(combination,dictioStar):
    sum = 0
    for position in combination:
        sum += dictioStar[position]
    return sum

class MagicStar:

    def __init__(self,nPoints):
        self.nPoints = nPoints
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
        self.kBoost = 0

        if self.nPoints == 6:
            self.magicConstant = 26
            self.combinations = [ "ACFH" , "BCDE" , "BFIL" , "ADGK" , "HIJK" , "EGJL" ]
#            self.constrainIndex = [[0,2,5,7], [1,2,3,4], [0,3,6,10], [7,8,9,10], [1,5,8,11], [4,6,9,11]]
            self.spacedValues = [2,3,4,8,9,10]
        if self.nPoints == 7:
            self.magicConstant = 30
            self.star["M"] = 0
            self.star["N"] = 0
            self.combinations = [ "ACEG" , "ADHJ" , "BCDF" , "BEIM" , "FHKN" , "GILN" , "JKLM" ]
#            self.constrainIndex = [[0,2,4,6], [0,3,7,9], [1,2,3,5], [1,4,8,12], [5,7,10,13], [6,8,11,13], [9,10,11,12]]
            self.spacedValues = []
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

    def printParameters(self):
        print str(self.nPoints)+" Points"
        print str(self.nValues)+" Values"
        print str(self.nConstrains)+" Constrains"
        return

    def getStar(self):
        return self.star



    def findStar(self):
        """ Find a solution to the magic star puzzle """

        print "Star with "+str(self.nPoints)+" points ==> Values from 1 to "+str(self.nValues)

        allValues = [x for x in range(1,self.nValues+1)]
        count = 0
        for permut4 in itertools.permutations(allValues,4):
            for i in range(0,4):
                self.star[self.combinations[0][i]] = permut4[i]
            if sum_combination(self.combinations[0],self.star) == self.magicConstant:
                lessValues8 = copy.deepcopy(allValues)
                for value in permut4:
                    lessValues8.remove(value)

                for permut3 in itertools.permutations(lessValues8,3):
                    for i in range(0,3):
                        self.star[self.combinations[1][i]] = permut3[i]
                    if sum_combination(self.combinations[1],self.star) == self.magicConstant:
                        lessValues5 = copy.deepcopy(lessValues8)

                        for value in permut3:
                            lessValues5.remove(value)
                        #print " Remaining values: ",lessValues5
# DOES NOT WORK BEYOND THIS POINT!
                        for permut2a in itertools.permutations(lessValues5,2):

                            for i in range(0,2):
                                self.star[self.combinations[2][i]] = permut2a[i]
                            if sum_combination(self.combinations[2],self.star) == self.magicConstant:
                                lessValues3 = copy.deepcopy(lessValues5)
                                
                                for value in permut2a:
                                    print " Removing value ",value," from list ",lessValues3
                                    lessValues3.remove(value)
                                #print " Remaining values: ",lessValues3

                                for permut2b in itertools.permutations(lessValues3,2):
                                    for i in range(0,2):
                                        self.star[self.combinations[3][i]] = permut2b[i]
                                    if sum_combination(self.combinations[3],self.star) == self.magicConstant:
                                        lessValues1 = copy.deepcopy(lessValues3)

                                        for value in permut2b:
                                    #print " Removing value ",value," from list ",lessValues3)
                                            lessValues1.remove(value)
                                        #print " Remaining value: ",lessValues1

                                        for i in range(0,2):
                                            self.star[self.combinations[4][i]] = lessValues1[0]

                                        if sum_combination(self.combinations[4],self.star) == self.magicConstant:
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
        for letter in "ABCDEFGHIJKLMNOP":
            if self.star[letter] < 10:
                if self.star[letter] in self.spacedValues:
                    pos[letter] = "-"+str(self.star[letter])
                else:
                    pos[letter] = " "+str(self.star[letter])
            else:
                pos[letter] = str(self.star[letter])
            if ( self.nPoints == 6 and letter == "L" ) or ( self.nPoints == 7 and letter == "N" ):
                break

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

star6 = MagicStar(6)
star6.findStar()
#star6.printStar()
