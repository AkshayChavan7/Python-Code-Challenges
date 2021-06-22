'''
Challenge 11: Generate a password

Input: Number of words in passphrase
Output: String of random words separated by spaces

>>> generate_passphrase(5)
vice fame tango abide verb
'''

import random


dictionary = {}
for line in open('c11.txt','r'):
    line = line.split('\n')[0]
    dictionary[line.split('\t')[0]] = line.split('\t')[1] 

#print(dictionary['21131'])

def generate_passphrase(n):

    passphrase = ''
    for i in range(n):
        num = ''
        for j in range(5):
            num += str(random.randrange(1,6))
        passphrase += dictionary[num] +' '
    print(passphrase)
        
generate_passphrase(7 )
