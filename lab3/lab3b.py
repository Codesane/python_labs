# lab3B.py
# @author Felix Ekdahl
# Student-ID: felno295
# Assignment 3B from: http://www.ida.liu.se/~TDDD64/python/la/la4.shtml

LOGIC = {"ELLER" : 1, "OCH" : 2}
TEXT_TO_BOOL = {"falskt" : False, "sant" : True}

def logikvarde(st, vars, bVal = True):
	vars["sant"] = "sant"
	vars["falskt"] = "falskt"
	if st[0] == "ICKE":
		if isinstance(st[1], str):
			if st[1] in vars.keys():
				return not TEXT_TO_BOOL[vars[st[1]]] if bVal else TEXT_TO_BOOL[vars[st[1]]]
		return logikvarde(st[1], vars, not bVal)
	elif st[0] in vars.keys():
		lhBool = logikvarde(st[2], vars)
		vlVar = TEXT_TO_BOOL[vars[st[0]]]
		return (lhBool + vlVar) >= LOGIC[st[1]] if bVal else not (lhBool + vlVar) >= LOGIC[st[1]]
	elif isinstance(st, str):
		return TEXT_TO_BOOL[vars[st]]
	else:
		return bVal;



print(logikvarde(["ICKE", ["ICKE", ["ICKE", ["katten_sover", "ELLER", ["ICKE", "katten_sover"]]]]],
               {"katten_sover": "falskt"}))
