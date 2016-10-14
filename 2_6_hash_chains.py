# python3
# In this task we have implement hash chains,
# The program should support next operations
# add string - add string to the hash table, ignore, if have one
# remove string - remove string from the table
# find string - return 'true' or 'false' if table contains such string or not
# check i - output the content of i-th list in the table. If such is empty, output blank line
# when inserting a new string, a hash table, you must insert on the beginning of the string
# Output must print the result each check and find operation
#
# Example:
# 5
# 12
# add world
# add HellO
# check 4
# find World
# find world
# del world
# check 4
# del HellO
# add luck
# add GooD
# check 2
# del good
#
# Output:
# HellO world
# no
# yes
# HellO
# GooD luck
import threading
import sys
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.n = int(input())
        self.hash_table = {}

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ((ans % self.bucket_count) + self.bucket_count) % self.bucket_count

    def write_chain(self, chain):
        line = ''
        for item in self.hash_table[chain]:
            line += item + ' '
        if line == '':
            print()
        else:
            print(line)

    def read_query(self):
        return Query(input().split())

    # creating a hash table with chaining values
    def add_to_hash_row(self, row_number, current_item):
        if row_number in self.hash_table:
            if current_item not in self.hash_table[row_number]:
                current_chain = self.hash_table[row_number]
                self.hash_table[row_number] = [current_item] + current_chain
        else:
            self.hash_table[row_number] = [current_item]

    # Find string in given hash table row
    def find_string(self, hash_row, string):
        row_to_search = self.hash_table[hash_row]
        if string in row_to_search:
            print('yes')
        else:
            print('no')

    # Remove item from hash table
    def remove_item_or_pass(self, hash_item, item):
        if hash_item in self.hash_table:
            chain = self.hash_table[hash_item]
            if item in chain:
                chain.remove(item)

    def process_query(self, query):
        if query.type == 'check':
            # check the string in hash table and print it out
            if query.ind in self.hash_table:
                self.write_chain(query.ind)
            else:
                print()
        else:
            # find a hash
            hash_item = self._hash_func(query.s)
            if query.type == 'find':
                # write yes or no
                if hash_item in self.hash_table:
                    self.find_string(hash_item, query.s)
                else:
                    print('no')
            elif query.type == 'add':
                # Rewrite, to save chains in a hash table
                self.add_to_hash_row(hash_item, query.s)
            # else query is del, so we pop element if so
            else:
                self.remove_item_or_pass(hash_item, query.s)

    def process_queries(self):
        # run process-queries
        for i in range(self.n):
            self.process_query(self.read_query())


def main():
    # take user input
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    # process user input
    proc.process_queries()

threading.Thread(target=main).start()