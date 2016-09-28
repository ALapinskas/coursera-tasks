# Uses python3
# The first line contains an iteger n and a sequence a0 < a1 < ... < an-1 of n pairwise
# distinct positive integers in increasing order, the next line integer k
# and positive integers b0,b1,...,bk-1
# Find all i from 0 to k - 1, output an index 0 <= j <= n - 1, 
# such that ai = bi or -1 in there is no such index
# Example:
# 5 1 5 8 12 13
# 5 8 1 23 1 11
# Output: 2 0 -1 0 -1

import sys

def binary_search(a, x):
    low, high = 0, len(a)
    # write your code here
    i = 1
    #print('length a:' + str(len(a)))
    while low <= high:
        mid = int(round(low + (high-low)/2))
        #print('iteration:' + str(i) + ' / mid =' + str(mid))
        if mid >= len(a):
            if int(x) == int(a[mid - 1]):
                #print('stop while iteration overflow')
                return mid - 1
            else:
               #print('stop loop - overflow')
               return - 1
        if int(x) == int(a[mid]):
            #print('stop while')
            return mid
        elif int(x) < int(a[mid]):
            high = mid - 1
        else:
            low = mid + 1
        i += 1
    #print('end while')
    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        # print(linear_search(a, x), end = ' ')
        print(binary_search(a, x), end = ' ')
