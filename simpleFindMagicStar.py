import itertools

magicConstant = 26

…

constrainIndex = [[0,2,5,7], [1,2,3,4], [0,3,6,10], [7,8,9,10], [1,5,8,11], [4,6,9,11]]

star = [ x for x in range(1,13)]
print(star)

for solution in itertools.permutations(star):
            output = 1
            #print(solution)
            
            for constrain in constrainIndex:
            
                var = 0
                for index in constrain:
                    var += solution[index]
                    
                if var == magicConstant:
                    output *= 1
                else:
                    output *= 0
                    break
                
            if output:
                star = [x for x in solution]
                break
        
print(star)