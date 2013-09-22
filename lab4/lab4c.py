import math

dx = 0.001

def glatta(fn):
	return lambda x: ((fn(x - dx) + fn(x) + fn(x + dx)) / 3)

glattad_sin = glatta(math.sin)

def mangfalt_glattad(fn, n):
	for i in range(n):
		fn = glatta(fn)
	return fn
	
mangfald = mangfalt_glattad(math.sin, 5)

print(mangfald(0.456))
