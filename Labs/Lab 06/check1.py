"""
Lab 6 Checkpoint 1
Author: Samuel Marks
CSCI1100 Spring 2018
"""
bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]

lines = "-------------------------"
print(lines)
for x in range(len(bd)):
    empty = ""
    for i in range(len(bd[x])):
        if i == 0:
            empty += "|"
        empty += " " + bd[x][i]
        if (i+1)%3 == 0:
            empty += " |"  
    print(empty)
    if (x+1)%3 == 0:
        print(lines)