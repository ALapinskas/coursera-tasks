# Uses python3
# Take two lines of words for example short ports
# Count the Edit Distance between them:
# minimum number of operations(mistamaches, incertions and deletions) to make one word
# to another

import sys

def edit_distance(A, B):
    n = len(A)
    m = len(B)
    D = [[0]*(m+1) for _ in range(n+1)] # create empty matrix
    for i in range(0,n+1): #initialization of base case values
        D[i][0]=i
    for j in range(0,m+1):
        D[0][j]=j
    #print(str(D))
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            #print(str(i) + str(j))
            if A[i - 1] == B[j - 1]:
                D[i][j] = D[i-1][j-1]
                #print('D[i=' + str(i) + '][j=' + str(j) + '] = ' + str(D[i][j]))
            else:
                D[i][j] = min(D[i][j-1],D[i-1][j],D[i-1][j-1])+1
    #print(str(D))
    return D[i][j]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
