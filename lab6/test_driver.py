# =========================================================================
#  Almanackan - Laboration i kursen Programmering i Python
#
#  Modul: test_driver.py
#  Ursprunglig version: 2009-09-25 av Anders Haraldsson
#  Uppdaterad: 2008-10-07 av Peter Dalenius
# =========================================================================

# Ladda in nödvändiga funktioner från almanackssystemet.
from datatyper import *
from bokningar import *
from utskrifter import *

# Den här filen innehåller nödvändiga funktioner för att testa om funktionen
# som beräknar lediga tidsperioder mellan två klockslag i en dagalmanacka
# fungerar som den ska. I koden nedan antas funktionen heta lediga_tidsperioder
# och anropas med parametrarna dagalmanacka, startklockslag, slutklockslag (i
# den ordnignen). Troligtvis behöver du ändra i koden nedan så att din funktion
# (som möjligen har ett annat namn) anropas med rätt parameterordning. Dessutom
# behöver du fylla på med fler testfall.


# =========================================================================
#  1. Nya hjälpfunktioner
# =========================================================================

# Syftet med funktionen omvandla_tidsperioder är att på ett enkelt sätt
# kunna skapa många testfall. Indata är en lista med strängar som ska
# representera tidsperioder, t.ex. "10:15-12:30". Utdata är ett riktigt
# almanacksobjekt av typen tidsperioder. Exempel:
"""
>>> omvandla_tidsperioder(["10:15-12:00", "13:15-15:00"])
('tidsperioder',
  [('tidsperiod', (('klockslag', (('timme', 10), ('minut', 15))),
                   ('klockslag', (('timme', 12), ('minut', 0))))),
   ('tidsperiod', (('klockslag', (('timme', 13), ('minut', 15))),
                   ('klockslag', (('timme', 15), ('minut', 0)))))])
"""
def omvandla_tidsperioder(lista):
	"lista med strängar -> tidsperioder"
	if not lista:
		return skapa_tidsperioder()
	else:
		klockslagen = lista[0].split("-")
		return lägg_in_tidsperiod(
		           skapa_tidsperiod(
		               omvandla_klockslag(klockslagen[0]),
		               omvandla_klockslag(klockslagen[1])),
		           omvandla_tidsperioder(lista[1:]))

# För att kunna testa funktionen lediga_tidsperioder behöver vi dessutom
# kunna skapa dagalmanackor. Denna funktion kan skapa en dagalmanacka
# utifrån ett tidsperioder-objekt, där varje möte har en standardbeskrivning.
def tidsperioder_till_dagalmanacka(tpr):
	"tidsperioder -> dagalmanacka"
	typkontroll(tpr, är_tidsperioder)
	if är_tom_tidsperioder(tpr):
		return skapa_dagalmanacka()
	else:
		return lägg_in_möte(
		           skapa_mötestid(första_tidsperiod(tpr), skapa_möte("Test")),
		           tidsperioder_till_dagalmanacka(resten_tidsperioder(tpr)))

# Testar om två objekt av typen tidsperioder är lika.
def är_samma_tidsperioder(tpr1, tpr2):
	"tidsperioder x tidsperioder -> sanningsvärde"
	if är_tom_tidsperioder(tpr1) and är_tom_tidsperioder(tpr2):
		return True
	elif är_tom_tidsperioder(tpr1) or är_tom_tidsperioder(tpr2):
		return False
	elif är_samma_tidsperiod(första_tidsperiod(tpr1), första_tidsperiod(tpr2)):
		return är_samma_tidsperioder(
		           resten_tidsperioder(tpr1),
		           resten_tidsperioder(tpr2))
	else:
		return False

# Testar om två objekt av typen tidsperiod är lika.
def är_samma_tidsperiod(tp1, tp2):
	"tidsperiod x tidsperiod -> sanningsvärde"
	return är_samma_klockslag(start_klockslag(tp1), start_klockslag(tp2)) and\
	       är_samma_klockslag(slut_klockslag(tp1), slut_klockslag(tp2))


# =========================================================================
#  2. Funktioner för att bygga upp och köra testfall
# =========================================================================

# Den globala variabeln testfallen innehåller alla våra testfall i form
# av en dict med testfallets nummer som nyckel.
testfallen = {}

# Funktionen skapa_testfall tar emot specifikationen av ett testfall i
# extern notation och skapar ett faktiskt testfall som läggs till i den
# globala variabeln testfallen. Varje testfall har ett nummer för att man
# lättare ska förstå felrapporterna.
def skapa_testfall(test_nr, start_str, slut_str, bokningar, resultat):
	"integer x (klockslag x klockslag x tidsperioder -> tidsperioder)"
	" x sträng x sträng x lista med strängar x lista med strängar -> Lisp-kod"
	start = omvandla_klockslag(start_str)
	slut = omvandla_klockslag(slut_str)
	dagalma = tidsperioder_till_dagalmanacka(
	                          omvandla_tidsperioder(bokningar))
	resultat_tidsperioder = omvandla_tidsperioder(resultat)
	
	global testfallen
	
	testfallen[test_nr] = [start, slut, dagalma, resultat_tidsperioder]

# Denna funktionen kör igenom alla testfallen.
def kör_testfallen():
	
	alla_ok = True
	antal = 0
	
	for test_nr in testfallen:
		
		antal += 1
		
		testfall = testfallen[test_nr]
		
		start = testfall[0]
		slut = testfall[1]
		dagalma = testfall[2]
		förväntade_tidsperioder = testfall[3]
		
		if not är_samma_tidsperioder(
		        lediga_tidsperioder(dagalma, start, slut),
		        förväntade_tidsperioder):
			
			alla_ok = False
			
			print("----")
			print("Testfall nummer {0} ger felaktig utdata.".format(test_nr))
			print("Beräknade lediga tidsperioder:")
			skriv_tidsperioder(lediga_tidsperioder(dagalma, start, slut))
			print()
			print("Förväntade lediga tidsperioder:")
			skriv_tidsperioder(förväntade_tidsperioder)
			print("----")
			print()
	
	if alla_ok:
		print("Alla ({0} stycken) testfallen är OK.".format(antal))

# Skapar alla testfall och kör dem.
def testa_lediga():
	skapa_testfallen()
	kör_testfallen()


# =========================================================================
#  3. Exempel på hur man kan bygga upp testfall
# =========================================================================

# Skapar alla testfall genom att anropa skapa_testfall med olika argument.
def skapa_testfallen():
	
	global testfallen
	
	testfallen = {}
	
	skapa_testfall(
	    1,
	    "08:00",                        # Start av intervall
	    "21:00",                        # Slut av intervall
	    ["07:00-09:00", "13:00-18:00"], # Dagens mötestider
	    ["09:00-13:00", "18:00-21:00"]) # Förväntade lediga tider
	
	# Fyll på med fler testfall (som det ovan)...
	# ...här!
	
	print("Testfallen är skapade!")

# Kör testerna genom att anropa testa_lediga().