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

def is_0or1_most(index):
    numones = 0
    numzeros = 0
    mostcommon = "error" #set to 0 or 1
    for line in lines:
        if line[index] == "1": #data file contains strings
            numones += 1
        elif line[index] == "0":
            numzeros += 1
    if numones == 0 and numzeros == 0: #in case it gets to /n at the end
        print("error no ones or zeros")
        return mostcommon
    #determine if more ones or zeros
    if numones > numzeros:
        mostcommon = "1"
    elif numones < numzeros:
        mostcommon = "0"
    else:
        #ones and zeros are equal
        mostcommon = "1"
        print("equal amounts of 1 and 0")
    return mostcommon



index = 0 #doing for first digit only
digit = is_0or1_most(0)
print(digit)
remaininglines = [] #store the binary numbes not yet eliminated from list
for line in lines:
    if line[index] == digit:
        remaininglines.append(line)

print(remaininglines)
"""
for i in range(12): #5 for test data, 12 for real data
    print(i)

   
#convert to decimal
#note: bin() is used to go from binary to decimal
gamma_int = int(gamma, 2) # 2 us because we are staring in binary (base 2)
epsilon_int = int(epsilon, 2)

print("gamma as decimal", gamma_int)
print("epsilon as decimal", epsilon_int)

answer = gamma_int*epsilon_int

print("gamma*epsilon =",answer)
"""

input("press enter to exit")
