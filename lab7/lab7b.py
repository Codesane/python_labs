# lab7B.py
# @author Felix Ekdahl
# Student-ID: felno295
# http://www.ida.liu.se/~TDDD64/python/la/la7.shtml


to_sort = [34, 93, 23, 14, 56, 26, 17, 59, 75]

def quicksort(slist):
	if not slist:
		return slist
	else:
		pivot = slist[0]
		left = []
		right = []
		for i in slist[1:]:
			if i < pivot:
				left.append(i)
			else:
				right.append(i)
		
		return quicksort(left) + [pivot] + quicksort(right)

print(quicksort(to_sort))

