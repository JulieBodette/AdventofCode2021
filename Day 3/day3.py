#day 2
#read from text file
text_file = open("testdata.txt", "r")
lines = text_file.readlines() #global
#print(lines)

"""
#convert all to int and make new list
betterlines = []
for line in lines:
    newline = int(line)
    betterlines.append(newline)
"""
#print(betterlines)
gamma = ""

def calc_gamma(gamma,index):
    numones = 0
    numzeros = 0
    for line in lines:
        if line[index] == "1": #data file contains strings
            numones += 1
        elif line[index] == "0":
            numzeros += 1
    #determine if more ones or zeros and add correponding number to answer
    #this is to calculate gamma rate
    if numones > numzeros:
        gamma = gamma + "1"
    elif numones < numzeros:
        gamma = gamma + "0"
    else:
        #ones and zeros are equal
        print("error, equal amounts of 1 and 0")
    return gamma

for i in range(5): #5 for test data, change to 12 for real data
    gamma = calc_gamma(gamma,i)

print("gamma is", gamma)
        

#epsilon is the opposite of gamma
#every 0 in gamma is a 1 in epsilon
epsilon = ""
for i in range(len(gamma)):
    if gamma[i] == "0":
        epsilon = epsilon + "1"
    elif gamma[i] == "1":
        epsilon = epsilon + "0"
    else:
        print("error, character in gamma is not 0 or 1")

print("epsilon is", epsilon)
        
    


input("press enter to exit")
