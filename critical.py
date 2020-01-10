   
from random import randint

# low number, high number, effect
# open file
crit_array = []
with open('criticals.txt') as fp:
    # load the criticals.txt into an array
    crit_array = fp.readlines()
    # find the highest number for range of random number generator
    h = int(crit_array[-1].split(", ")[1])
    # generate a random number between 1 and highest number
    rNum = randint(1, h)
    # print(crit_array, rNum)
    array_length = len(crit_array)
    for i in range(array_length):
        while rNum >= int(crit_array[i].split(", ")[0]) and rNum <= int(crit_array[i].split(", ")[1]):
            effect = crit_array[i].split(", ")[2]
            print("Random Number from 1 to " + str(h) +": " + str(rNum))
            print("Random Critical Effect: " + effect)
            break
fp.close()
