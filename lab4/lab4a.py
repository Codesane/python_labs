# lab4A.py
# @author Felix Ekdahl
# Student-ID: felno295
# Assignment 4A from: http://www.ida.liu.se/~TDDD64/python/la/la4.shtml


def powerset(lst):
	if not lst:
		return [[]]
	applist = []
	applist.extend(powerset2(lst, powerset(lst[1:]), []))
	return applist


def powerset2(lst, iter, retList = []):
	if not iter:
		return retList
	subs = list(lst[0]) + list(iter[0])
	retList.append(subs)
	retList.append(iter[0])
	return powerset2(lst, iter[1:], retList)

print(powerset(['a', 'b']))
