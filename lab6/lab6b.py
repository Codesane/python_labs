# Tidsperioder är av typen "tidsperioder" enligt ex: "('tidsperioder', [tidsperiod_1, tideperiod_2, tidsperiod_3, ..., tidsperiod_n])
# funktionen packa_ihop skapar en tupel där namnet är definierat på plats [0] och värdet (listan med tidsperioder) på plats[1]

from almanacka import *
from datatyper import *


def skapa_tidsperioder():
	""" Skapar och returnerar ett tidsperioder objekt med en tom lista som värde. """
	return packa_ihop('tidsperioder', []) # att bara ta bort packa_ihop skulle också funka, dock förstör det abstraktionsmönstret

def lägg_till_tidsperioder(t_period, t_perioder):
	if not är_tidsperioder(t_perioder) or not är_tidsperiod(t_period):
		raise Exception("Argumenten är av fel datatyp, indata skall vara av typen tidsperiod och tidsperioder '(tidsperiod, tidsperioder)'!")
	tidsperioder = packa_upp(t_perioder) # ger oss värdet på tidsperioderna av typen list
	res_värde = []
	if not t_perioder:
		return packa_ihop('tidsperioder', [t_period])
	for i in range(1, tidsperioder):
		if not är_före_klockslag(start_klockslag(t_period), start_klockslag(tidsperioder[i])):
			res_värde = tidsperioder[:i-1] + [t_period] + tidsperioder[i-1:]
	return packa_ihop('tidsperioder', res_värde)

def är_tidsperioder(t_perioder):
	return (typ(t_perioder) == 'tidsperioder')

def print_tidsperioder(t_perioder):
	if not är_tidsperioder(t_perioder):
		raise Exception("Argumentet är inte en tidsperiod!")
	for tidsperiod in packa_upp(t_perioder):
		print(tidsperiod)

t_perioder = skapa_tidsperioder()

			
			
			
	




