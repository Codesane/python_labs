
from almanacka import *
from datatyper import *
from lab6b     import *

def ledigt(namn, dag, månad, kl1, kl2):
	dag = skapa_dag(dag)
	månad = skapa_månad(månad)
	tidsperiod = skapa_tidsperiod(omvandla_klockslag(kl1), omvandla_klockslag(kl2))
	tidsperioder = skapa_tidsperioder()
	dag_alm = dagalmanacka(dag, månadsalmanacka(månad, hämta_almanacka(namn)))
	möten = skapa_tidsperioder_från_dagalm(dag_alm)

	start_tid = omvandla_klockslag(kl1)

	tper = skapa_tidsperioder()
	for m in packa_upp(möten):
		start_möte = start_klockslag(m)
		if är_före_klockslag(start_tid, start_möte):
			tper = lägg_till_tidsperioder(skapa_tidsperiod(start_tid, start_möte), tper)
		start_tid = slut_klockslag(m)
	if är_före_klockslag(slut_klockslag(packa_upp(möten)[len(packa_upp(möten))-1]), omvandla_klockslag(kl2)):
		ny_tidsperiod = skapa_tidsperiod(slut_klockslag(packa_upp(möten)[len(packa_upp(möten))-1]), omvandla_klockslag(kl2))
		tper = lägg_till_tidsperioder(ny_tidsperiod, tper)
	print_tidsperioder(tper)

def skapa_tidsperioder_från_dagalm(dagalmanacka):
	""" Skapar tidsperioder av ett dagsalmanacka objekt """
	tp = skapa_tidsperioder()
	for möte in packa_upp(dagalmanacka):
		tp = lägg_till_tidsperioder(tidsperioddel(möte), tp)
	return tp


skapa("Peter")
boka("Peter", 14, "sep", "08:00", "10:00", "Lisp Fö P42")
boka("Peter", 14, "sep", "10:00", "12:00", "Lisp La SU00")
boka("Peter", 14, "sep", "13:00", "15:00", "Kaffepaus")
ledigt("Peter", 14, "sep", "09:00", "17:00")

	
