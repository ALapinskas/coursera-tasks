# Uses python3
# take two digits at the first line
# 10 4 for example - first - the capacity of knapsack, second is not used the number of items
# the second line consists of numbers - each is item, the value is the number
# The goal: is to count the maximum number of items value you could take,
# the items are no dividible
#
import sys

def optimal_weight(W, w):
    # write your code here
    n = len(w)
    m = W
    result = 0
    res = [[0]*(m+1) for _ in range(n+1)] # create empty matrix
    for i in range(0,n+1): #initialization of base case values
        res[i][0]=i
    for j in range(0,m+1):
        res[0][j]=j
    #print(str(res))
    #print(n)
    for i in range(0,n + 1):
        for j in range(0,m + 1):
            #print('i=' + str(i) + ' and j=' + str(j))
            if i == 0 or j == 0:
                res[i][j] = 0 #fill the started lines with zeros
            elif w[i - 1] > j:
                res[i][j] = res[i - 1][j]
            else:
                res[i][j] = max(w[i - 1] + res[i - 1][j - w[i - 1]], res[i - 1][j])
            #print(str(res))
    return res[n][W] #optimal weight

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
