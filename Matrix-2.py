from itertools import zip_longest
#python program to print all permutation with repetition of characters
def toString(stringl):
    print("")
    for i in range(len(stringl)):
        print(stringl[i])
    return '-'.join(stringl)

#the main function that recursively prints all repeated
#permutations of hte given string It uses data[] to store
#all permutations one by one
def allLexicorgraphicRecur(string, data, last, index):
    length = len(string)

#one by one fix all characters at the given index and
#recur for the subsequent indexes
    for i in range(length):
    #fix the ith character at index and if this is not the 
    #ast index then recursively call for higher indexes
        data[index] = string[i]
    #if this is the last index then print the string
    #stored in data
        if index==last:
            print (toString(data))
        else:
            allLexicorgraphicRecur(string, data,last, index+1)
#this function sorts input string
#allocate memory for data
def allLexicorgraphic(string):
    length = len(string)

# create a temp array that will used by 
#alllexicographiRecu
    data = [""]*(length+1)

    string = sorted(string)

    allLexicorgraphicRecur(string, data, length-1, 0)

#Driver program
Degree90 = [[1,1],
            [1,1],
            [2,2]]
Degree0 = [[1,1,2],
           [1,1,2]]
Degree180 = [[2,1,1],
             [2,1,1]]
Degree90 = [[2,2],
            [1,1],
            [1,1]]
TotalList = [[0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0]]


NewList = [x for x in zip_longest(TotalList, Degree90, fillvalue=[0])]
for i in range(len(NewList)):
    print(NewList[i])
print()
#string = "ABCD"
#print ("all permutation with repetition of " + string + " are: ")
#allLexicorgraphic(string)
for i in range(len(Degree90)):
    print(Degree90[i])
#hello world
print()
for i in range(len(TotalList)):
    print(TotalList[i])
