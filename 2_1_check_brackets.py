# python3
# check all breckets in give string, return 'Success' if the order and balance
# is right, either return the position of wrong item
# Example:
# foo(bar[i);
# Output:
# 10

import sys
import threading
from datetime import datetime
#from collections import OrderedDict
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False


class BracketCounter:
    def __init__(self, stack):
        self.stack = stack

    def count(self):
        opening_brackets_stack = []
        for i, el in enumerate(self.stack):
            i +=  1
            if el == '(' or el == '[' or el == '{':
                # fill the stack with open brackets
                opening_brackets_stack.append([i, el])
                pass
            if el == ')' or el == ']' or el == '}':
                try:
                    last_item_value = opening_brackets_stack[-1][1]
                    if Bracket(last_item_value, i).match(el):
                        opening_brackets_stack.pop()
                        pass
                    else:
                        return i
                except IndexError:
                    return i
        else:
            if opening_brackets_stack:
                return opening_brackets_stack[0][0]
            else:
                return 'Success'


def main():
    #tstart = datetime.now()
    text = sys.stdin.read()
    print(BracketCounter(text).count())
    #tend = datetime.now()
    #print(tend - tstart)


threading.Thread(target=main).start()
