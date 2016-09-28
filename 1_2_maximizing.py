# Uses python3
# The first line contains an integer n, and the second - a sequence 
# of integers a1,a2,...an, and the third sequence on integers b1,b2,...bn
# Need to partition them into pairs ai,bi such as the sum of their products is muximized
# for example
# 3
# 1 3 -5
# -2 4 1
# Output: 23
# 23 = 3 x 4 + 1 x 1 + (-5) x (-2)
#
import sys

def get_optimal_value(capacity, weights, values):
	# items importance (v/w)
	items_cap = []
	# current vaules of items in knapsack
	items_vals = 0
	# current weigth of knapsack
	curr_weigth = 0
	# make an array of items inportance
	i = 0
	while i < len(values):
		#print(values[i]/weights[i])
		items_cap.append(values[i]/weights[i])
		i += 1
	# main checking loop
	i = 0
	while curr_weigth < capacity:
		# take the largest importance item from the list
		if not items_cap:
			break
		maxitemindex = items_cap.index(max(items_cap))
		# if it overflow the knapsack place, cut it before placing
		if capacity - curr_weigth < weights[maxitemindex]:
			items_vals += items_cap[maxitemindex] * (capacity - curr_weigth)
			curr_weigth += weights[maxitemindex] * (capacity - curr_weigth)
		else:
			curr_weigth += weights[maxitemindex]
			items_vals += values[maxitemindex]
			items_cap.remove(max(items_cap))
		#print('iteration passed, curr-weight: ' + str(curr_weigth) + '; #items-vals: ' + str(items_vals))
		
	# uncomment for debug
	#print ('items-cap - ' + str(items_cap))
	#print ('capacity - ' + str(capacity))
	#print ('weights - ' + str(weights))
	#print ('values - ' + str(values))
	return items_vals


if __name__ == "__main__":
	data = list(map(int, sys.stdin.readline().split()))
	n, capacity = data[0:2]
	values = data[2:(2 * n + 2):2]
	weights = data[3:(2 * n + 2):2]
	opt_value = get_optimal_value(capacity, weights, values)
	print("{:.4f}".format(opt_value))
