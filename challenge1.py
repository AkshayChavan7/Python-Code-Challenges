'''
Challenge 1: Write a function to get all prime factors of given number
Input: 630
Output: [2,3,3,5,7]

Logic: 2*3*3*5*7
'''

def get_next_prime(n):
    k = n+1
    flag = False
    while True:
        for i in range(2,k):
            #print(k,i)
            if k%i==0:
                flag = True
                break
            if i==k-1:
                return k
        if flag:
            k+=1
        #else:
        #    return k

def get_prime_factors(n):
    ans = []
    factor = 2
    while n>1:
        if n%factor==0:
            ans.append(factor)
            n = n/factor
        else:
            factor = get_next_prime(factor)
    print(ans)

#print(get_next_prime(5))
get_prime_factors(13)
