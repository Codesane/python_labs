# lab4B.py
# @author Felix Ekdahl
# Student-ID: felno295
# Assignment 4B from: http://www.ida.liu.se/~TDDC66/python/la/la4.shtml

from math import pow

def generera_hojdfunktion(h0, v0, t0, a): return lambda t: h0 + v0 * (t - t0) + a * 0.5 * pow((t - t0), 2)

h_fas_ett = generera_hojdfunktion(0, 0, 0, 290)

fasEtt = h_fas_ett(5)
print(fasEtt)

