'''
Challenge 4: Find all list items

Input:
 example = [ [ [1, 2, 3], 2, [1, 3] ], [1, 2, 3]]
 >>>index_all(example,2)

Output:
 [ [0, 0, 1], [0, 1], [1,1] ]
'''

def index_all(l, n):
    indices = []
    for i in range(len(l)):
        if l[i] == n:
            indices.append([i])
            #print('*', indices)
        elif isinstance(l[i],list):
            #print('#',l[i])
            for index in index_all(l[i],n):
                #print(index)
                indices.append([i]+index)
    return indices

example = [ [ [1, 2, 3], 2, [1, 3] ],
            [1, 2, 3]
          ]
print(index_all(example,2))
