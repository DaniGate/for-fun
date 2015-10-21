import itertools
import random
import time

class MagicStar:

    def __init__(self,nPoints):
        self.nPoints = nPoints
        self.star = { "A" : ,
                      "B" : ,
                      "C" : ,
                      "D" : ,
                      "E" : ,
                      "F" : ,
                      "G" : ,
                      "H" : ,
                      "I" : ,
                      "J" : ,
                      "K" : ,
                      "L" : }
        self.newstar = [ ]
        self.nValues = nPoints * 2
        self.nConstrains = nPoints
        self.kBoost = 0

        if self.nPoints == 6:
            self.magicConstant = 26
            self.combinations = [ "BCDE", "ACFH", "ADGK", "HIJK", "EGJL", "BFIL" ]
            self.constrainIndex = [[0,2,5,7], [1,2,3,4], [0,3,6,10], [7,8,9,10], [1,5,8,11], [4,6,9,11]]
            self.spacedValues = [2,3,4,8,9,10]
        if self.nPoints == 7:
            self.magicConstant = 30
            self.constrainIndex = [[0,2,4,6], [0,3,7,9], [1,2,3,5], [1,4,8,12], [5,7,10,13], [6,8,11,13], [9,10,11,12]]
            self.spacedValues = []
        if self.nPoints == 8:
            self.magicConstant = 34
            self.constrainIndex = [[0,2,5,7], [0,3,6,8], [1,2,3,4], [1,5,9,11], [4,6,10,14], [7,9,12,15], [8,10,13,15], [11,12,13,14]]
            self.spacedValues = []

    def printParameters(self):
        print(str(self.nPoints)+" Points")
        print(str(self.nValues)+" Values")
        print(str(self.nConstrains)+" Constrains")
        return

    def getStar(self):
        return self.star

    def findStar(self):
        """ Find a solution to the magic star puzzle """

        orderedStar = [ x for x in range(1,self.nValues+1) ]
        randomStar = [ ]

        print("Star with "+str(self.nPoints)+" points ==> Values from 1 to "+str(self.nValues))
        for i in range(self.nValues):
            randomIndex = random.randint(1,len(orderedStar))-1
            randomStar.append(orderedStar[randomIndex])
            orderedStar.remove(orderedStar[randomIndex])

        # self.star = [ x for x in range(1,self.nValues+1) ] # tmp

        count = 0
        if self.kBoost:
            previous = [[0 for x in range(4)] for x in range(4)]

        for solution in itertools.permutations(randomStar):
            output = 1

            for constrain in self.constrainIndex:

                step = self.constrainIndex.index(constrain)
                if self.kBoost and previous[step][0] == solution[constrain[0]] and previous[step][1] == solution[constrain[1]] and previous[step][2] == solution[constrain[2]] and previous[step][3] == solution[constrain[3]]: # skip combinations that do not meet a previously checked constrain
                    output = 0
                    break

                if output == 0:
                    break
                #print(solution)
                sum = 0
                for index in constrain:
                    sum += solution[index]

                if sum == self.magicConstant:
                    output *= 1
                    if self.kBoost:
                        previous[step] = [0 for x in range(4)]
                else:
                    output *= 0
                    if self.kBoost:
                        for i in range(0,4):
                            previous[step][i] = solution[constrain[i]]
                        print("previous = ",previous)
                        break

            count +=1
            if count == 100:
                count = 0
                #answer = input("Continue?")

            if output:
                self.star = solution
                break

        return


    def printStar(self):
        """ Print the current star on screen """
        so = [ "" ] * self.nValues
        for sol in self.star:
            if sol < 10:
                if self.star.index(sol) in self.spacedValues:
                    so[self.star.index(sol)] = "-"+str(sol)
                else:
                    so[self.star.index(sol)] = "  "+str(sol)
            else:
                so[self.star.index(sol)] = str(sol)

        if self.nPoints == 6:
            print("            ",so[0],"           ")
            print("              /  \           ")
            print("             /    \          ")
            print(so[1]+"----"+so[2]+"----"+so[3]+"----"+so[4],sep="")
            print("   \      /           \     / ")
            print("     \  /     ~~     \  / ")
            print("    ",so[5],"      |",self.magicConstant,"|    ",so[6],sep="")
            print("     /  \     ~~     /  \ ")
            print("    /     \           /     \ ")
            print(so[7],"----",so[8],"----",so[9],"----",so[10],sep="")
            print("             \    /          ")
            print("              \  /           ")
            print("            ",so[11],"           ")
            print()

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
        print(after-before," ticks")
        mean += after - before
        i += 1

    mean /= N
    print(mean," mean ticks")
    return mean


myStar = MagicStar(6)
myStar.findStar()
myStar.printStar()

print("Finished!")
