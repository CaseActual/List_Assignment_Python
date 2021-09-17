# zcrowell_list_assignment.py
# list min, max, sum, and average for random ints
# last edited by Zane Crowell - Oct. 11, 2020
# CSCI 111 Section 002

import random

# create variables + empty python list
numList = []
listSum = int(0)
maxNum = int(-5)
minNum = int(105)
listAvg = float(0.0)

# create count-controlled while loop to populate 1,000 random integers (between 1 & 100) to the list
while len(numList) < 1000:
    numList.append(random.randrange(1,101))
    
# calculate list average    
listAvg = (listSum / len(numList))

# use for statement to iterate list:
for n in numList:
    # sum of values in list
    listSum += n
    # maximum of the values in list
    if n > maxNum:
        maxNum = n
    # minimum of the values in list
    if n < minNum:
        minNum = n

listAvg = (listSum / len(numList))

# print number of elements in list
print("The number of elements in the list is: ", len(numList))

# print the results of the for loop    
print("The sum of this list is:", listSum)
print("The largest integer in this list is:", maxNum)
print("The smallest integer in this list is:", minNum)

# print list average and round the result to two decimals
print("The average of this list is:", round(listAvg, 2))






    
        








