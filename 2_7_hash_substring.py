# python3
# search pattern P string in given string T
# return all positions of matches in given string
# Example:
# aba
# abacaba
# output:
# 0 4
import threading


class SearchSubsting:
    def __init__(self, pattern, text):
        self.p = pattern
        self.t = text
        self.pNum = [ord(self.p[i]) for i in range(len(self.p))]
        self.tNum = [ord(self.t[i]) for i in range(len(self.t))]
        self.lenP = len(self.p)
        self.lenT = len(self.t)

    @staticmethod
    def print_occurrences(output):
        for value in output:
            print(value, end=" ")

    def rabin_karp(self):
        bigP = 1000000007 # 5 ** (self.lenT * self.lenP)
        x = 22313 # random.randint(1, bigP - 1)
        result = []
        pHash = self.poly_hash(self.pNum, bigP, x)
        H = self.precompute_hashes(bigP, x)
        for i in range(0, len(self.t) - len(self.p) + 1):
            if pHash != H[i]:
                continue
            currentstring = self.t[i:(i + self.lenP)]
            if currentstring == self.p:
                result.append(i)
        self.print_occurrences(result)

    def poly_hash(self, k, p, x):
        hash_val = 0
        length = len(k) - 1
        for i in range(length, -1, -1):
            hash_val = (hash_val * x + k[i]) % p
        return hash_val

    def precompute_hashes(self, p, x):
        H = [0] * (self.lenT - self.lenP + 1)
        S = [self.tNum[i] for i in range(self.lenT - self.lenP, self.lenT)]
        H[self.lenT - self.lenP] = self.poly_hash(S, p, x)
        y = 1
        length = self.lenT - self.lenP - 1
        for i in range(1, self.lenP+1):
            y = (y * x) % p
        for i in range(length, -1, -1):
            H[i] = ((x * H[i + 1] + self.tNum[i] - y * self.tNum[i + self.lenP]) % p + p) % p;
        return H


def main():
    SearchSubsting(input().rstrip(), input().rstrip()).rabin_karp()

threading.Thread(target=main).start()