def start_klockslag(per):
	# Dålig implementation, bryter mot abstraktionslagren!  -- Fixed
	if not är_tidsperiod(per):
		raise Exception("Parametervärdet är inte en tidsperiod!")
	else:
		tid = packa_upp(per)[0]'	
		if är_klockslag(tid):
			return tid


def längd_av_tidsperiod(t_per):
	# Dålig implementation, bryter mot abstraktionen. -- Fixed
	
	t1 = m1 = heltal(timdel(start_klockslag(t_per)))
	t2 = m2 = heltal(timdel(slut_klockslag(t_per)))
	
	tim = skapa_timme(t2 - t1)
	min = skapa_minut(m2 - m1)
	
	return skapa_tidsrymd(tim, min)

def slut_klockslag(per):
	# Dålig implementation, bryter mot abstraktionslagren! -- Fixed
		if not är_tidsperiod(per):
		raise Exception("Parametervärdet är inte en tidsperiod!")
	else:
		tid = packa_upp(per)[1]
		if är_klockslag(tid):
			return tid

def överlapp(tp1, tp2):
	# Dålig implementation, bryter mot abstraktionen. -- Fixed
	""" Object (tidsperiod, (m1, m2)) """
	min1 = senaste_klockslag(start_klockslag(tp1), slut_klockslag(tp1))
	min2 = tidigaste_klockslag(slut_klockslag(tp2), slut_klockslag(tp2))
	return ('tidsperiod', (min1, min2)) # "lite" fräschare

def skapa_tidsrymd(timme, minut):
	# Dålig implementation, bryter mot abstraktionslagren! -- Fixed!
	if not är_minut(minut) or är_timme(timme):
		raise Exception("Argumenten stämmer ej med förväntat indata.")
	else:
		totMin = heltal(timme) * 60 + heltal(minut) # 60 min/timme + rest minuter (Antalet totala minuter)
		retTim = skapa_timme(totMin // 60) # Heltalsdivision med 60 ger oss antalet timmar som minuterna representerar
		retMin = skapa_minut(totMin % 60) # Antalet minuter totalmängden representerar (- timmarna)
	return ('tidsrymd', (retTim, retMin)) # Returnerar ett tidsrymd objekt, formaterat enligt kriterierna





