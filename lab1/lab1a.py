# lab1a.py
# @author Felix Ekdahl
# Student-ID: felno295
# Assignment 1A from: www.ida.liu.se/~TDDC66/python/la/la1.shtml

def fak(n, i, k):
    if not i == 0 and not k == 1:
        return fak(n*i, i-1, k-1)
    else:
        return n


def main():
    n = 1000
    k = 4
    b = fak(n, n-1, k)//fak(k, k-1, k)
    print(b)

main()
