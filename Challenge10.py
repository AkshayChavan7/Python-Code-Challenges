'''
Challenge 10: Write a Python function to count the number of unique words and how often each occurs.


Input: path to a text file
Output: print message with:
 - total number of words
 - top 20 most frequent words
 - number of occurences for top 20
'''
import re

def count_words(path):
    para = []
    for line in open(path, 'r'):
        for word in re.sub('\W',' ',line).split(' '):
            if word!='':
                para.append(word)
    unique_words = set(para)
    #print(len(unique_words))
    top_words = {}
    for uw in unique_words:
        count = 0
        for word in para:
            if uw == word:
                count+=1
        top_words[uw]=count
    top_words = {k: v for k, v in sorted(top_words.items(), key=lambda item: item[1], reverse = True)}
    cnt = 0
    print('-------------------------------')
    print('SR NO.\tWORDS\t\tCOUNTS')
    print('-------------------------------')
    for word,count in top_words.items():
        if cnt == 20:
            break
        print('{}\t{}\t\t{}'.format(cnt+1,word,count))
        cnt+=1
        
count_words('c10.txt')
