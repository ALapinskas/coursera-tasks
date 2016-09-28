# Uses python3
# count sum of fubinachi sequence of the given number
#
import sys

def fibonacci_sum(n):
   if n <= 2:
      count = 1
   else:
      count = 0
   F=[0,1]
   if n <= 1:
      return n

   #for i in range(2, to + 1):
   i = 2
   while i <= n:
      curr_num = F[i-1] + F[i-2]
      #print(str(i) + ' - ' + str(curr_num))
      if i >= 10:
        F.insert(i,curr_num % 10)
      else:
        F.insert(i,curr_num)
      i+=1
   count = sum(F) % 10
   return count

if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)
    print(fibonacci_sum(n))

