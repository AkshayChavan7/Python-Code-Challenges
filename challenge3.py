'''
Challenge 3: Sorting of words

Input: 'banana ORANGE apple'
Output: 'apple banana ORANGE'

Input: 'string of words'
Output: 'of string words'
'''

#print(str.casefold('akshay'))


def sort_words(s):
    s= s.split(' ')
    d = {}
    for word in s:
        d[str.casefold(word)] = word
    sorted_keys = sorted(d.keys())

    ans = ''
    for key in sorted_keys:
        ans+=d[key]+' '

    return ans

print(sort_words('string of words'))
