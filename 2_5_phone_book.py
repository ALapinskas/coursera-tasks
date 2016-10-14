# python3
# this program should take to things,
# first line the number of operations,
# Next - operations with interactive phone book,
# Add number name, del number, find number
# Output will process this operations, find returns the name,
# or not found, if name not fount in book
# Example:
# 5
# add 911 polly
# add 8910434 mom
# del 911
# find 8910434
# find 8910434
# Output:
# mom
# not found

from datetime import datetime
import threading
import sys
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


# read current data input
def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


# write responces to output
def write_responses(result):
    print('\n'.join(result))


def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = {}
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            #if contacts.get(cur_query.number) != None :
            #break
            #for contact in contacts:
                #if contact.number == cur_query.number:
                #    contact.name = cur_query.name
                #    break
            #else: # otherwise, just add it
            contacts[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            if contacts.get(cur_query.number) != None:
                contacts.pop(cur_query.number)
            #for j in range(len(contacts)):
                #if contacts[j].number == cur_query.number:
                #    contacts.pop(j)
                #    break
        else:
            response = 'not found'
            # for query type find
            #print(contacts)
            if contacts.get(cur_query.number) != None:
                response = contacts[cur_query.number]
            #for contact in contacts:
            #    if contact.number == cur_query.number:
            #        response = contact.name
            #        break
            result.append(response)
    return result

#if __name__ == '__main__':
def main():
    write_responses(process_queries(read_queries()))

threading.Thread(target=main).start()