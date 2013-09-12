


def powerset(lst):
	if not lst:
		return [[]]
	applist = []
	for i in powerset(lst[1:]):
		subs = []
		subs.append(lst[0])
		subs.extend(i)
		applist.append(subs)
		applist.append(i)
	return  applist


print(powerset(['a', 'b', 'c']))
