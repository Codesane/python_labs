# lab3B.py
# @author Felix Ekdahl
# Student-ID: felno295
# Assignment 3B from: http://www.ida.liu.se/~TDDC66/python/la/la3.shtml

SC = {"sant" : 1, "falskt" : 0, "ELLER" : 1, "OCH" : 2}

def logikvarde(st, vars):
	vars["sant"] = "sant"
	vars["falskt"] = "falskt"
	l1 = getBool(st)
	l2 = getBool(l1[1][2])
	return (SC[vars[l1[1][0]]] if l1[0] else not SC[vars[l1[1][0]]]) + (SC[vars[l2[1]]] if l2[0] else not SC[vars[l2[1]]]) >= SC[l1[1][1]]

def getBool(st, bVal = True):
	return getBool(st[1], not bVal) if st[0] == "ICKE" else (bVal, st)
	

print(logikvarde(["öppen_dörr", "OCH", "katten_borta"], 
               {"öppen_dörr" : "falskt", "katten_borta" : "sant", "katten_sover" : "sant"}))
	
