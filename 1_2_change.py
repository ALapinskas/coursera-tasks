# Uses python3
# Find the minimum coins needed to checge the input value into coins with denominations
# 1, 5 and 10
# Example: 28
# Output: 6
# 28 = 10 + 10 + 5 + 1 + 1 + 1
#
import sys

def get_change(m):
    #write your code here
	coins = [1, 5, 10]
	summa = 0
	value = 0
	while summa <= m and coins:
		maxnum = max(coins)
		if maxnum <= (m - summa):
			summa = summa + maxnum
			value += 1
		else:
			if maxnum in coins:
				coins.remove(maxnum)
	return value

if __name__ == '__main__':
    m = int(sys.stdin.readline())
    print(get_change(m))
