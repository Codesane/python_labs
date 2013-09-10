# lab3A.py
# @author Felix Ekdahl
# Student-ID: felno295
# Assignment 3A from: http://www.ida.liu.se/~TDDC66/python/la/la3.shtml



lst1 = ("_", ".")
lst2 = (" ", "|")

def dela_rekursiv(instr, sum1 = "", sum2 = ""):
	if len(instr) == 0:
		return (sum1, sum2)
	else:
		if instr[0] in lst1 or instr[0].islower():
			sum1 += instr[0]
		elif instr[0] in lst2 or instr[0].isupper():
			sum2 += instr[0]
		return dela_rekursiv(instr[1:], sum1, sum2)

def dela_iterativ(instr):
	sum1 = ""
	sum2 = ""
	for i in instr:
		if i in lst1 or i.islower():
			sum1 += i
		elif i in lst2 or i.isupper():
			sum2 += i
	return (sum1, sum2)

var = dela_iterativ("fTlH-yE((g 48aQnUdI#5eC_K§b 29äB>cRkO7-aW-0sN#i 0>nFeOrX=!_ =!sJöUkM1aP(>_Sh wOiV,lE4aR3_ pTåH_Em jLuA§kZ`aY>_ @tDuO5vGo$r1")
print(var)
