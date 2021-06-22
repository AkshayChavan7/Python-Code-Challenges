'''
Challenge 6: Save a dictionary

save_dict(): Create a function which will take file path and dictionary as input and will write that dictionary into the specified file.
get_dict(): Create a function which will take file path as input and will read dictionary object from the file
'''



import json


def save_dict(path,d):
    #d = {'A':'Akshay','C':'Chavan'}
    fs = open(path, 'w')
    fs.write(str(d))
    fs.close()


def get_dict(path):
    fs = open(path,'r')
    line = fs.readline()
    #d = dict(json.loads(json.dumps(line)))
    d = eval(line)
    print(d['A'])

    
d = {'A':'Akshay','C':'Chavan'}
path = 'C:/Users/Akshay Chavan/Desktop/Python Challenges/dict.json'
save_dict(path,d)
get_dict(path)    

