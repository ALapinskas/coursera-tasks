# python3
import hash_chains
import names
import random

_multiplier = 263
_prime = 1000000007

def generator():
    f = open('test.txt', 'w')
    r = open('results.txt', 'w')
    n = 10000
    m = random.randrange(n/5, n, 1)
    results_table = []
    result = ''
    f.write(str(m) + '\n')
    f.write(str(n) + '\n')
    for x in range(1, n):
        directive = random.choice(['add', 'del', 'find'])
        if directive != 'check':
            name = names.get_first_name()
            hash = _hash_func(name, m)
            if directive == 'add':
                if name not in results_table:
                    results_table.append(name)
            elif directive == 'find':
                if name in results_table:
                    result = 'yes'
                else:
                    result = 'no'
                r.write(str(result) + '\n')
            elif directive == 'del':
                if name in results_table:
                    results_table.remove(name)
            number = ''
        else:
            name = ''
            number = random.randrange(10, 99, 1)
        #f.write('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
        f.write(directive + ' ' + str(number) + name + '\n')
        if x % 99 == 0:
            print('1000 lines printed, processed...')


def _hash_func(word, m):
    ans = 0
    for c in reversed(word):
        ans = (ans * _multiplier + ord(c)) % _prime
    return ((ans % m) + m) % m


if __name__ == '__main__':
    #generator()
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()