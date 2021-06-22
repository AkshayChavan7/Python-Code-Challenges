'''
Challenge 9: Simulate a dice (Monte-Carlo Simulation)

Input: Function should accept an arbitrary number of numbers representing the number of sides on each die.
Output: Output the probability for each outcome after simulation
'''

import random

def roll_dice(s):
    nums = s.split(',')

    for i in range(len(nums)):
        nums[i]=int(nums[i])
    #print(nums)
    iterations = 1000000
    probs = []

    low,high = len(nums), sum(nums)
    for i in range(low, high+1):
        probs.append(0)
    #print(probs)
    for i in range(iterations):
        n = random.randrange(low,high+1)
        print(n)
        probs[n-low]+=1

    print('--- OUTCOME PROBABILITY ---')
    for i in range(len(probs)):
        probs[i]= probs[i]/iterations
        print((i+3),'=>',probs[i]*100)
    #print('Total = ',sum(probs))
        


roll_dice(input('Enter numbers:'))
    
