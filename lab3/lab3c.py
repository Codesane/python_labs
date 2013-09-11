from math import fabs, sqrt

map = []


def nollstall_bradet():
	map.clear()
	

def ar_platsen_ledig(x, y):
	for i in map:
		if i[1] == [x, y]:
			return False
	return True

def placera_figur(x, y, spelare):
	if(ar_platsen_ledig(x, y)):
		map.append([spelare, [x, y]])
		return True
	else:
		return False

def vilken_figur(x, y):
	for i in map:
		if i[1] == [x, y]:
			return i[0]
	return False

def ta_bort_figur(x, y):
	for i in range(0, len(map)):
		if map[i][1] == [x, y]:
			map.pop(i)
			return True
	return False

def flytta_figur(fx, fy, tx, ty):
	if ar_platsen_ledig(tx, ty):
		placera_figur(tx, ty, vilken_figur(fx, fy))
		ta_bort_figur(fx, fy)
		return True
	else:
		return False

def rakna(dir, d, spelare):
	lookIndex = 0 if dir == "kolumn" else 1
	cnt = 0
	for i in map:
		if i[1][lookIndex] == d and i[0] == spelare:
			cnt += 1
	print(cnt)
	
def narmaste_figur(x, y):
	retVal = ()
	minLen = -1
	for i in map:
		dst = sqrt(fabs(x - i[1][0])**2 + fabs(y - i[1][1])**2)
		if minLen == -1 or minLen > dst:
			minLen = dst
			retVal = (i[1][0], i[1][1])
	return retVal
