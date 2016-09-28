# Uses python3
# Given a set of n segments {[a0,b0],[a1,b1],...,[an-1,bn-1]}
# Find the minimum number of m points such that each segment contains at least one point
# Example:
# 3
# 1 3
# 2 5
# 3 6
# Output:
# 1
# 3

import sys
from collections import namedtuple
import operator

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #print(segments)
	#sort the segments by the minimum right point
    # segments = sorted(segments, key=lambda i: i[1])
    segments = sorted(segments, key=operator.itemgetter(0))
    segments = sorted(segments, key=operator.itemgetter(1))
    #print(segments)
    #looping segmants
    prevstart = 0
    prevend = 0
    for s in segments:
        #if it first iteration, set the point, and checking variable for the next iterations
        if prevstart == 0:
            prevstart = s.end
            prevend = s.end
            points.append(s.end)
            #print('first iteration')
        else:
		#check if the starting point larger then the previos seted point - set another point
            if s.start > prevend:
                points.append(s.end)
                prevstart = s.start
                prevend = s.end
                #print('iteration' + str(s.end))
    return points

if __name__ == '__main__':
    input = sys.stdin.readline()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
