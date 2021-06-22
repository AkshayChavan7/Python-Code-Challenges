'''
Challenge 2: Write a python function to check if string is palindrome or not

Input: level
Output: True

Input: hello world
Output: False

Input: Go hang a salami - I'm a lasagna hog.
Output: True
'''

def isChar(ch):
    if (ord(ch)>=65 and ord(ch)<=90) or (ord(ch)>=97 and ord(ch)<=122):
        return True
    else:
        return False

def is_palindrome(s):
    s1=''
    for ch in s:
        if isChar(ch):
            s1+=ch
    #flag= False
    for i in range(len(s1)//2):
        print(str.capitalize(s1[i]),str.capitalize(s1[-(i+1)]))
        if str.capitalize(s1[i])!=str.capitalize(s1[-(i+1)]):
            return False
    return True

print(is_palindrome("Go hang a salami - I'm a lasagna hog."))
#a=str.capitalize('akshay')
#print(a)
