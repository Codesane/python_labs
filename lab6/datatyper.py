# =========================================================================
#  Almanackan - Laboration i kursen Programmering i Python
#
#  Modul: datatyper.py
#  Uppdaterad: 2005-09-27 av Peter Dalenius
#  Beroenden: 
#    Inga
# =========================================================================

# I början på denna modul finns de primitiva funktioner som behövs för att
# hantera de abstrakta datatyperna i almanackan, följt av flera
# "bra att ha"-funktioner.

## =========================================================================
##  1. Grundläggande funktioner för typ- och felhantering
## =========================================================================

def packa_ihop(typ, objekt):
    "almanackstyp x Python-objekt -> almanacksobjekt"
    return (typ, objekt)

def packa_upp(objekt):
    "almanacksobjekt -> Python-objekt"
    if isinstance(objekt, tuple):
        return objekt[1]

def typ(objekt):
    "almanacksobjekt -> almanackstyp" 
    if isinstance(objekt, tuple):
        return objekt[0]

def typkontroll(värde, predikat):
    assert predikat(värde), "Värdet {0} är av fel typ.".format(värde)

## =========================================================================
##  2. Enkla abstrakta datatyper
## =========================================================================

# ----- 2.1. Primitiver för datatypen timme. -----
def skapa_timme(h):
    "Python-heltal -> timme"
    typkontroll(h, lambda h: isinstance(h, int) and 0 <= h)
    return packa_ihop('timme', h)

def är_timme(objekt):
    "Python-objekt -> sanningsvärde"
    return typ(objekt) == 'timme'

# Datatypen timme har även den primitiva funktionen "heltal", definerad under
# datatypen minut.

# ----- 2.2. Primitiver för datatypen minut. -----
def skapa_minut(m):
    "Python-heltal -> minut"
    typkontroll(m, lambda m: isinstance(m, int) and 0 <= m)
    return packa_ihop('minut', m)

def är_minut(objekt):
    "Python-objekt -> sanningsvärde"
    return typ(objekt) == 'minut'

def heltal(timme_minut):
    "timme U minut -> Python-heltal"
    typkontroll(timme_minut, lambda x: är_timme(x) or är_minut(x))
    return packa_upp(timme_minut)


# ----- 2.3. Primitiver för datatypen dag. -----
def skapa_dag(d):
    "Python-heltal -> dag"
    typkontroll(d, lambda d: isinstance(d, int) and 1 <= d <= 31)
    return packa_ihop('dag', d)

def är_dag(objekt):
    "Python-objekt -> sanningsvärde"
    return typ(objekt) == 'dag'

def dagnummer(dag):
    "dag -> Python-heltal"
    typkontroll(dag, är_dag)
    return packa_upp(dag)


# ----- 2.4. Primitiver för datatypen månad. -----
MÅNADSNAMN = {'jan': 'januari',
              'feb': 'februari',
              'mar': 'mars',
              'apr': 'april',
              'maj': 'maj',
              'jun': 'juni',
              'jul': 'juli',
              'aug': 'augusti',
              'sep': 'september',
              'okt': 'oktober',
              'nov': 'november',
              'dec': 'december'}

MÅNADSDATA = {'januari': 31,
              'februari': 28,
              'mars': 31,
              'april': 30,
              'maj': 31,
              'juni': 30,
              'juli': 31,
              'augusti': 31,
              'september': 30,
              'oktober': 31,
              'november': 30,
              'december': 31}

MÅNADSNUMMER = {'januari': 1,
                'februari': 2,
                'mars': 3,
                'april': 4,
                'maj': 5,
                'juni': 6,
                'juli': 7,
                'augusti': 8,
                'september': 9,
                'oktober': 10,
                'november': 11,
                'december': 12}

def skapa_månad(mån):
    "Python-symbol -> månad"
    if mån in MÅNADSDATA:
        return packa_ihop('månad', mån)
    else:
        if mån in MÅNADSNAMN:
            return packa_ihop('månad', MÅNADSNAMN[mån])
        else:
            raise Exception('\'{0}\' är ej en månad.'.format(mån))

def är_månad(objekt):
    "Python-objekt -> sanningsvärde"
    return typ(objekt) == 'månad'

def månadsnamn(mån):
    "månad -> Python-symbol"
    typkontroll(mån, är_månad)
    return packa_upp(mån)

def månadsnummer(mån):
    "månad -> heltal"
    typkontroll(mån, är_månad)
    return MÅNADSNUMMER[packa_upp(mån)]

def antal_dagar_i_månad(mån):
    "månad -> heltal"
    typkontroll(mån, är_månad)
    return MÅNADSDATA[packa_upp(mån)]


# ----- 2.5. Primitiver för datatypen möte. -----
def skapa_möte(text):
    "Python-heltal -> möte"
    typkontroll(text, lambda t: isinstance(t, str))
    return packa_ihop('möte', text)

def är_möte(objekt):
    "Python-objekt -> sanningsvärde"
    return typ(objekt) == 'möte'

def mötestext(möte):
    "möte -> Python-sträng"
    typkontroll(möte, är_möte)
    return packa_upp(möte)

## =========================================================================
##  3. Sammansatta abstrakta datatyper
## =========================================================================

# ----- 3.1. Primitiver för datatypen tidsrymd. -----
# Funktionen "skapa_tidsrymd" ska omimplementeras i Uppgift 6A.
def skapa_tidsrymd(timme, minut):
	# Dålig implementation, bryter mot abstraktionslagren! -- Fixed!
	if not är_minut(minut) or är_timme(timme):
		raise Exception("Argumenten stämmer ej med förväntat indata.")
	else:
		totMin = heltal(timme) * 60 + heltal(minut) # 60 min/timme + rest minuter (Antalet totala minuter)
		retTim = skapa_timme(totMin // 60) # Heltalsdivision med 60 ger oss antalet timmar som minuterna representerar
		retMin = skapa_minut(totMin % 60) # Antalet minuter totalmängden representerar (- timmarna)
	return ('tidsrymd', (retTim, retMin)) # Returnerar ett tidsrymd objekt, formaterat enligt kriterierna

def är_tidsrymd(objekt):
    "Python-objekt -> sanningsvärde"
    return typ(objekt) == 'tidsrymd'

def timdel(tidsrymd_klockslag):
    "tidsrymd U klockslag -> timme"
    if är_tidsrymd(tidsrymd_klockslag):
        return packa_upp(tidsrymd_klockslag)[0]
    elif är_klockslag(tidsrymd_klockslag):
        return packa_upp(tidsrymd_klockslag)[0]
    else:
        raise Exception('Argumentet ska vara tidsrymd eller klockslag.')

def minutdel(tidsrymd_klockslag):
    "tidsrymd U klockslag -> minut"
    if är_tidsrymd(tidsrymd_klockslag):
        return packa_upp(tidsrymd_klockslag)[1]
    elif är_klockslag(tidsrymd_klockslag):
        return packa_upp(tidsrymd_klockslag)[1]
    else:
        raise Exception('Argumentet ska vara tidsrymd eller klockslag.')


# ----- 3.2. Primitiver för datatypen klockslag. -----
def skapa_klockslag(timme, minut):
    "timme x minut -> klockslag"
    typkontroll(timme, är_timme)
    typkontroll(minut, är_minut)
    if heltal(timme) > 23:
        raise Exception('Timmen {0} är ej giltig.'.format(timme))
    elif heltal(minut) > 59:
        raise Exception('Minuten {0} är ej giltig.'.format(minut))
    else:
        return packa_ihop('klockslag', (timme, minut))

def är_klockslag(objekt):
    "Python-objekt -> sanningsvärde"
    return typ(objekt) == 'klockslag'


# ----- 3.3. Primitiver för datatypen tidsperiod. -----
def skapa_tidsperiod(kl1, kl2):
    "klockslag x klockslag -> tidsperiod"
    typkontroll(kl1, är_klockslag)
    typkontroll(kl2, är_klockslag)
    if är_samma_klockslag(kl1, kl2):
        raise Exception('Klockslagen är samma, {0}, {1}.'.format(kl1, kl2))
    elif not är_före_klockslag(kl1, kl2):
        raise Exception('Klockslagen i fel ordning: {0}, {1}.'.format(kl1, kl2))
    else:
        return packa_ihop('tidsperiod', (kl1, kl2))

def är_tidsperiod(objekt):
    "Python-objekt -> sanningsvärde"
    return typ(objekt) == 'tidsperiod'

# Funktionen start_klockslag ska omimplementeras i Uppgift 6A.
def start_klockslag(per):
	# Dålig implementation, bryter mot abstraktionslagren!  -- Fixed
	if not är_tidsperiod(per):
		raise Exception("Parametervärdet är inte en tidsperiod!")
	else:
		tid = packa_upp(per)[0]'	
		if är_klockslag(tid):
			return tid

# Funktionen slut_klockslag ska omimplementeras i Uppgift 6A.
def slut_klockslag(per):
	# Dålig implementation, bryter mot abstraktionslagren! -- Fixed
		if not är_tidsperiod(per):
		raise Exception("Parametervärdet är inte en tidsperiod!")
	else:
		tid = packa_upp(per)[1]
		if är_klockslag(tid):
			return tid


#----- 3.4. Primitiver för datatypen datum. -----
def skapa_datum(dag, mån):
    "dag x månad -> datum"
    typkontroll(dag, är_dag)
    typkontroll(mån, är_månad)
    if dagnummer(dag) > antal_dagar_i_månad(mån):
        raise Exception('Felaktigt datum: {0}, {1}.'.format(dag, mån))

    else:
        return packa_ihop('datum', (mån, dag))

def är_datum(objekt):
    "Python-objekt -> sanningsvärde"
    return typ(objekt) == 'datum'

def månadsdel(datum):
    "datum -> månad"
    typkontroll(datum, är_datum)
    return packa_upp(datum)[0]

def dagdel(datum):
    "datum -> dag"
    typkontroll(datum, är_datum)
    return packa_upp(datum)[1]


# ----- 3.5. Primitiver för datatypen mötestid. -----
def skapa_mötestid(per, möte):
    "tidsperiod x möte -> mötestid"
    typkontroll(per, är_tidsperiod)
    typkontroll(möte, är_möte)
    return packa_ihop('mötestid', (per, möte))

def är_mötestid(objekt):
    "Python-objekt -> sanningsvärde"
    return typ(objekt) == 'mötestid'

def tidsperioddel(mtid):
    "mötestid -> tidsperiod"
    typkontroll(mtid, är_mötestid)
    return packa_upp(mtid)[0]

def mötesdel(mtid):
    "mötestid -> möte"
    typkontroll(mtid, är_mötestid)
    return packa_upp(mtid)[1]


# ----- 3.6. Primitiver för datatypen dagalmanacka. -----
def skapa_dagalmanacka():
    " -> dagalmanacka"
    return packa_ihop('dagalmanacka', [])

def är_dagalmanacka(objekt):
    "Python-objekt -> sanningsvärde"
    return typ(objekt) == 'dagalmanacka'

def är_tom_dagalmanacka(dagalma):
    "dagalmanacka -> sanningsvärde"
    typkontroll(dagalma, är_dagalmanacka)
    return not packa_upp(dagalma)

def lägg_in_möte(mtid, dagalma):
    "mötestid x dagalmanacka -> dagalmanacka"
    
    def sortera_in_möte(ml):
        if not ml or är_före_klockslag(start_klockslag(tidsperioddel(mtid)),
                                       start_klockslag(tidsperioddel(ml[0]))):
            return [mtid] + ml
        else:
            return [ml[0]] + sortera_in_möte(ml[1:])
    
    typkontroll(mtid, är_mötestid)
    typkontroll(dagalma, är_dagalmanacka)
    
    return packa_ihop('dagalmanacka', sortera_in_möte(packa_upp(dagalma)))

def första_mötestid(dagalma):
    "dagalmanacka -> mötestid"
    typkontroll(dagalma, är_dagalmanacka)
    if är_tom_dagalmanacka(dagalma):
        raise Exception('Dagalmanackan är tom.')
    else:
        return packa_upp(dagalma)[0]

def resten_dagalmanacka(dagalma):
    "dagalmanacka -> dagalmanacka"
    typkontroll(dagalma, är_dagalmanacka)
    if är_tom_dagalmanacka(dagalma):
        return dagalma
    else:
        return packa_ihop('dagalmanacka', packa_upp(dagalma)[1:])


# ----- 3.7. Primitiver för datatypen månadsalmanacka. -----
def skapa_månadsalmanacka():
    "-> månadsalmanacka"
    return packa_ihop('månadsalmanacka', [])

def är_månadsalmanacka(objekt):
    "Python-objekt -> sanningsvärde"
    return typ(objekt) == 'månadsalmanacka'

def är_tom_månadsalmanacka(månalma):
    "månadsalmanacka -> sanningsvärde"
    typkontroll(månalma, är_månadsalmanacka)
    return not packa_upp(månalma)

def lägg_in_dagalmanacka(dag, dagalma, månalma):
    "dag x dagalmanacka x månadsalmanacka -> månadsalmanacka"
    
    def uppdatera(dl):
        if not dl or dagnummer(dag) < dagnummer(skapa_dag(dl[0][0])):
            return [(packa_upp(dag), dagalma)] + dl
        elif dagnummer(dag) == dagnummer(skapa_dag(dl[0][0])):
            return [(packa_upp(dag), dagalma)] + dl[1:]
        else:
            return [dl[0]] + uppdatera(dl[1:])
    
    typkontroll(dag, är_dag)
    typkontroll(dagalma, är_dagalmanacka)
    typkontroll(månalma, är_månadsalmanacka)
    
    return packa_ihop('månadsalmanacka', uppdatera(packa_upp(månalma)))

def dagalmanacka(dag, månalma):
    "dag x månadsalmanacka -> dagalmanacka"
    typkontroll(dag, är_dag)
    typkontroll(månalma, är_månadsalmanacka)
    dag_kontroll = [i for i, x in enumerate(packa_upp(månalma))\
                               if x[0] == dagnummer(dag)]
    if not dag_kontroll:
        return skapa_dagalmanacka()
    else:
        return packa_upp(månalma)[dag_kontroll[0]][1]

def sista_dagnummer(månalma):
    "månadsalmanacka -> heltal"
    typkontroll(månalma, är_månadsalmanacka)
    if är_tom_månadsalmanacka(månalma):
        return 0
    else:
        return packa_upp(månalma)[-1][0]


# ----- 3.8. Primitiver för datatypen årsalmanacka. -----
def skapa_årsalmanacka():
    "-> årsalmanacka"
    return packa_ihop('årsalmanacka', [])

def är_årsalmanacka(objekt):
    "Python-objekt -> sanningsvärde"
    return typ(objekt) == 'årsalmanacka'

def är_tom_årsalmanacka(årsalma):
    "årsalmanacka -> sanningsvärde"
    typkontroll(årsalma, är_årsalmanacka)
    return not packa_upp(årsalma)

def lägg_in_månadsalmanacka(mån, månalma, årsalma):
    "månad x månadsalmanacka x årsalmanacka -> årsalmanacka"
    
    def uppdatera(ml):
        if not ml or månadsnummer(mån) < månadsnummer(skapa_månad(ml[0][0])):
            return [(packa_upp(mån), månalma)] + ml
        elif månadsnummer(mån) == månadsnummer(skapa_månad(ml[0][0])):
            return [(packa_upp(mån), månalma)] + ml[1:]
        else:
            return [ml[0]] + uppdatera(ml[1:])
    
    typkontroll(mån, är_månad)
    typkontroll(månalma, är_månadsalmanacka)
    typkontroll(årsalma, är_årsalmanacka)
    
    if är_tom_månadsalmanacka(månalma):
        return årsalma
    elif sista_dagnummer(månalma) > antal_dagar_i_månad(mån):
        raise Exception('För få dagar i {0}.'.format(månadsnamn(mån)))
    else:
        return packa_ihop('årsalmanacka', uppdatera(packa_upp(årsalma)))

def månadsalmanacka(mån, årsalma):
    "månad x årsalmanacka -> månadsalmanacka"
    
    typkontroll(mån, är_månad)
    typkontroll(årsalma, är_årsalmanacka)
    
    mån_kontroll = [i for i, x in enumerate(packa_upp(årsalma))\
                               if x[0] == månadsnamn(mån)]
    if not mån_kontroll:
        return skapa_månadsalmanacka()
    else:
        return packa_upp(årsalma)[mån_kontroll[0]][1]



# =========================================================================
#  A. Beräkningar och kontroller
# =========================================================================

# Undersöker om ett klockslag kommer före ett annat klockslag.
def är_före_klockslag(kl1, kl2):
    "klockslag x klockslag -> sanningsvärde"
    h1 = heltal(timdel(kl1))
    m1 = heltal(minutdel(kl1))
    h2 = heltal(timdel(kl2))
    m2 = heltal(minutdel(kl2))
    return h1 < h2 or (h1 == h2 and m1 < m2)

# Undersöker om två klockslag är lika.
def är_samma_klockslag(kl1, kl2):
    "klockslag x klockslag -> sanningsvärde"
    return heltal(timdel(kl1)) == heltal(timdel(kl2)) and\
           heltal(minutdel(kl1)) == heltal(minutdel(kl2))

# Undersöker om ett klockslag kommer före ett annat eller om de är lika.
def är_före_eller_samma_klockslag(kl1, kl2):
    "klockslag x klockslag -> sanningsvärde"
    return är_före_klockslag(kl1, kl2) or är_samma_klockslag(kl1, kl2)

# Returnerar det senaste av två klockslag.
def senaste_klockslag(kl1, kl2):
    "klockslag x klockslag -> klockslag"
    if är_före_klockslag(kl1, kl2):
        return kl2
    else:
        return kl1

# Returnerar det tidigaste av två klockslag.
def tidigaste_klockslag(kl1, kl2):
    "klockslag x klockslag -> klockslag"
    if är_före_klockslag(kl1, kl2):
        return kl1
    else:
        return kl2

# Undersöker om en tidsrymd är längre än eller lika lång som en annan.
def är_tidsrymd_längre_än_eller_lika(tr1, tr2):
    "tidsrymd x tidsrymd -> sanningsvärde"
    h1 = heltal(timdel(tr1))
    m1 = heltal(minutdel(tr1))
    h2 = heltal(timdel(tr2))
    m2 = heltal(minutdel(tr2))
    
    return h1 > h2 or (h1 == h2 and m1 >= m2)

# Undersöker om två tidsperioder överlappar.
def är_överlappande(tp1, tp2):
    "tidsperiod x tidsperiod -> sanningsvärde"
    return är_före_klockslag(start_klockslag(tp1), slut_klockslag(tp2)) and\
           är_före_klockslag(start_klockslag(tp2), slut_klockslag(tp1))

# Beräknar den överlappande tidsperioden mellan två tidsperioder.
# Funktionen överlapp ska omimplementeras i Uppgift 6A.
def överlapp(tp1, tp2):
	# Dålig implementation, bryter mot abstraktionen. -- Fixed
	""" Object (tidsperiod, (m1, m2)) """
	min1 = senaste_klockslag(start_klockslag(tp1), slut_klockslag(tp1))
	min2 = tidigaste_klockslag(slut_klockslag(tp2), slut_klockslag(tp2))
	return ('tidsperiod', (min1, min2)) # "lite" fräschare



# =========================================================================
#  B. Omvandlingar
# =========================================================================

# Returnerar längden av en tidsperiod, dvs omvandlar en tidsperiod
# till en tidsrymd.
# Funktionen längd_av_tidsperiod ska omimplementeras i Uppgift 6A.
def längd_av_tidsperiod(t_per):
	# Dålig implementation, bryter mot abstraktionen. -- Fixed
	
	t1 = m1 = heltal(timdel(start_klockslag(t_per)))
	t2 = m2 = heltal(timdel(slut_klockslag(t_per)))
	
	tim = skapa_timme(t2 - t1)
	min = skapa_minut(m2 - m1)
	
	return skapa_tidsrymd(tim, min)

# Omvandlar en sträng "HH:MM" till ett klockslag.
def omvandla_klockslag(s):
    "sträng -> klockslag"
    return skapa_klockslag(skapa_timme(int(s[0:2])), skapa_minut(int(s[3:5])))

# Omvandlar en sträng "HH:MM" till en tidsrymd. Timangivelsen kan bestå
# av ett godtyckligt antal tecken.
def omvandla_tidsrymd(s):
    "sträng -> tidsrymd"
    i = s.find(':')
    return skapa_tidsrymd(skapa_timme(int(s[0:i])), skapa_minut(int(s[i+1:])))

# =========================================================================
#  C. Iteratorfunktioner
# =========================================================================

# Detta avsnitt innehåller funktioner som kan utföra en operation
# på varje delelement i en sammansatt datastruktur, t.ex. varje dag
# i en månadsalmanacka. 
def för_varje_månad(årsalma, månadsfunktion):
    "årsalmanacka x (månadsalmanacka ->) ->"
    map(lambda m: månadsfunktion(månadsalmanacka(m, årsalma)), månader)

def för_varje_dag(månalma, mån, dagfunktion):
    "månadsalmanacka x (dagalmanacka ->) ->"
    map(lambda d: dagfunktion(dagalmanacka(skapa_dag(d), månalma)),
        list(range(1, antal_dagar_i_månad(mån)+1)))

def för_varje_möte(dagalma, mötesfunktion):
    "dagalmanacka x (mötestid ->) ->"
    if not är_tom_dagalmanacka(dagalma):
        mötesfunktion(första_mötestid(dagalma))
        för_varje_möte(resten_dagalmanacka(dagalma), mötesfunktion)

# Undersöker om det finns något möte i den givna dagalmanackan som
# uppfyller den givna predikatsfunktionen.
def kontrollera_varje_möte(dagalma, mötesfunktion):
    "dagalmanacka x (mötestid -> sanningsvärde) -> sanningsvärde"
    if är_tom_dagalmanacka(dagalma):
        return False
    elif mötesfunktion(första_mötestid(dagalma)):
        return True
    else:
        return kontrollera_varje_möte(resten_dagalmanacka(dagalma),
                                      mötesfunktion)

# Sorterar bort de tidsperioder som inte uppfyller ett givet predikat.
def tidsperiodsfilter(tpr, filter):
    "tidsperioder x (tidsperiod -> sanningsvärde) -> tidsperioder"
    if är_tom_tidsperioder(tpr):
        return skapa_tidsperioder()
    elif filter(första_tidsperiod(tpr)):
        return lägg_in_tidsperiod(första_tidsperiod(tpr),
                                  tidsperiodsfilter(resten_tidsperioder(tpr),
                                                    filter))
    else:
        return tidsperiodsfilter(resten_tidsperioder(tpr))
