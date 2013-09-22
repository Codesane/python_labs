# lab4C.py
# @author Felix Ekdahl
# Student-ID: felno295
# Assignment 4C from: http://www.ida.liu.se/~TDDD64/python/la/la4.shtml

import math

dx = 0.001

def glatta(fn):
	return lambda x: ((fn(x - dx) + fn(x) + fn(x + dx)) / 3)

glattad_sin = glatta(math.sin)

def mangfalt_glattad(fn, n):
	for i in range(n):
		fn = glatta(fn)
	return fn
	
print(mangfalt_glattad(math.sin, 5)(0.456))
print(mangfalt_glattad(lambda x: x**2, 5)(4))
