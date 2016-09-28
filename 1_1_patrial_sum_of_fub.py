# Uses python3
# Computed the sum of fubinachi numbers
#
import sys

def get_fibonacci_partial_sum(from_, to):
   if from_ <= 2:
      sum = 1
   else:
      sum = 0
   F=[0,1]
   if to <= 1:
      return to

   #for i in range(2, to + 1):
   i = 2
   while i <= to:
      curr_num = F[i-1] + F[i-2]
      #print(str(i) + ' - ' + str(curr_num))
      if i >= 10:
        F.insert(i,curr_num % 10)
      else:
        F.insert(i,curr_num)
      if i >= from_:
        sum = sum + F[i]
        if sum >= 10:
          sum = sum % 10
      i+=1

   return sum

if __name__ == '__main__':
    input = sys.stdin.readline()
    from_, to = map(int, input.split())
    print(get_fibonacci_partial_sum(from_, to))
