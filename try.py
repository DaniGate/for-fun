var = "HOLA"
array = [ 3,2,5,21 ]
lst = ["a","b","c","d"]

zippedList = zip(array,lst)
for item in zippedList:
    print item
    
X = [[gg,ss] for gg, ss in zip(array,lst)]
for pair in X:
    print pair
