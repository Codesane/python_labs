# Tidsperioder är av typen "tidsperioder" enligt ex: "('tidsperioder', [tidsperiod_1, tideperiod_2, tidsperiod_3, ..., tidsperiod_n])
# funktionen packa_ihop skapar en tupel där namnet är definierat på plats [0] och värdet (listan med tidsperioder) på plats[1]
from almanacka import *
from datatyper import *

def skapa_tidsperioder():
	""" Skapar och returnerar ett tidsperioder objekt med en tom lista som värde. """
	return packa_ihop('tidsperioder', [])

def lägg_till_tidsperioder(t_period, t_perioder):
	if not är_tidsperioder(t_perioder) or not är_tidsperiod(t_period):
		raise Exception("Argumenten är av fel datatyp, indata skall vara av typen tidsperiod och tidsperioder '(tidsperiod, tidsperioder)'!")
	tidsperioder = packa_upp(t_perioder) # ger oss värdet på tidsperioderna av typen list
	res_värde = []
	added = False
	if len(tidsperioder) == 0:
		return packa_ihop('tidsperioder', [t_period])
	for i in range(0, len(tidsperioder)):
		if är_före_klockslag(start_klockslag(t_period), start_klockslag(tidsperioder[i])):
			if not added:
				res_värde.append(t_period)
				added = True
			res_värde.append(tidsperioder[i])
		else:
			res_värde.append(tidsperioder[i])
	if not added:
		res_värde.append(t_period)
	return packa_ihop('tidsperioder', res_värde)

def är_tidsperioder(t_perioder):
	return (typ(t_perioder) == 'tidsperioder')

def print_tidsperioder(t_perioder):
	if not är_tidsperioder(t_perioder):
		raise Exception("Argumentet är inte en tidsperiod!")
	for tidsperiod in packa_upp(t_perioder):
		print(tidsperiod)



""" Testfall -- OK
t_perioder = skapa_tidsperioder()
kl1 = skapa_klockslag(skapa_timme(16), skapa_minut(0))
kl2 = skapa_klockslag(skapa_timme(18), skapa_minut(0))
tidsperiod = skapa_tidsperiod(kl1, kl2)

tidsperioder = lägg_till_tidsperioder(tidsperiod, t_perioder)

kl1 = skapa_klockslag(skapa_timme(12), skapa_minut(0))
kl2 = skapa_klockslag(skapa_timme(19), skapa_minut(0))
tidsperiod = skapa_tidsperiod(kl1, kl2)

tidsperioder = lägg_till_tidsperioder(tidsperiod, tidsperioder)

kl1 = skapa_klockslag(skapa_timme(18), skapa_minut(0))
kl2 = skapa_klockslag(skapa_timme(19), skapa_minut(0))
tidsperiod = skapa_tidsperiod(kl1, kl2)

tidsperioder = lägg_till_tidsperioder(tidsperiod, tidsperioder)

kl1 = skapa_klockslag(skapa_timme(20), skapa_minut(0))
kl2 = skapa_klockslag(skapa_timme(22), skapa_minut(0))
tidsperiod = skapa_tidsperiod(kl1, kl2)

tidsperioder = lägg_till_tidsperioder(tidsperiod, tidsperioder)

print_tidsperioder(tidsperioder)
"""

