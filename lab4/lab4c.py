import math

dx = 0.001

def glatta(func):
	return lambda x: ((func(x - dx) + func(x) + func(x + dx)) / 3)



glattad_sin = glatta(math.sin)

def upprepa(func, n, val):
	sum = 0
	for i in range(0, n):
		sum += func(val - dx) + func(val) + func(val + dx)
	print(sum, n)
	return sum / n

def mangfalt_glattad(func, n):
	return lambda x: upprepa(glatta(func), n, x)
	


	
mangfald = mangfalt_glattad(math.sin, 5)

print(mangfald(0.456))
