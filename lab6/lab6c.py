# lab6C.py
# @author Felix Ekdahl
# Student-ID: felno295
# Assignment 6C from: http://www.ida.liu.se/~TDDD64/python/la/la6.shtml



""" Skapar en ny dag med alla möten förutom det mötet som önskas avbokas och sätter in den nya dagen i almanackan """
def avboka(namn, dag, månad, stid):
	sd_dag = skapa_dag(dag)
	sm_månad = skapa_månad(månad)
	ok_stid = omvandla_klockslag(stid) #sträng
	dag_almanacka = dagalmanacka(sd_dag, månadsalmanacka(sm_månad, hämta_almanacka(namn)))
	avbokad_lista = []
	for m in packa_upp(dag_almanacka):
			if not start_klockslag(tidsperioddel(m)) == ok_stid:
				avbokad_lista.append(m)
	if len(avbokad_lista) == (len(packa_upp(dag_almanacka)) - 1):
		print("Mötet är avbokat.")
	
	månad = packa_upp(månadsalmanacka(skapa_månad(månad), hämta_almanacka(namn)))
	for i in range(0, len(månad)):
		månad[i] = packa_ihop(dag, packa_ihop('dagalmanacka', avbokad_lista)) if månad[i][0] == dag else månad[i][0]

skapa("Peter")
boka("Peter", 24, "dec", "12:00", "14:00", "Julmiddag")
boka("Peter", 24, "dec", "15:00", "16:00", "se på 'Dr Snuggles'")
visa("Peter", 24, "dec")

avboka("Peter", 24, "dec", "15:00")
visa("Peter", 24, "dec")
