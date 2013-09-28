# =========================================================================
#  Almanackan - Laboration i kursen Programmering i Python
#
#  Modul: bokningar.py
#  Uppdaterad: 2004-07-30 av Peter Dalenius
#  Beroenden:
#    datatyper.py
# =========================================================================

# I denna modul finns själva almanackslogiken. Dessa funktioner tar hand
# om att utföra bokningar i almanackor, hitta lediga tider och kontrollera
# om bokningar finns. För att göra detta använder de sig av de primitiva
# funktionerna och de hjälpfunktioner som finns i modulen datatyper.py.

from datatyper import *

# =========================================================================
#  1. Kontroller av almanackan
# =========================================================================
# Undersöker om det finns något möte i den givna dagalmanackan som
# krockar med den givna tidsperioden.
def är_bokat(dagalma, tp):
    "dagalmanacka x tidsperiod -> sanningsvärde"
    return kontrollera_varje_möte(
        dagalma,
        lambda möte: är_överlappande(tp, tidsperioddel(möte))) 

# Undersöker om det finns något möte i den givna dagalmanackan som
# börjar vid det givna klockslaget.
def är_bokat_från(dagalma, kl):
    "dagalmanacka x klockslag -> sanningsvärde"
    return kontrollera_varje_möte(
       dagalma,
       lambda möte: är_samma_klockslag(kl,
                                       start_klockslag(tidsperioddel(möte))))

# =========================================================================
#  2. Bokningar och avbokningar
# =========================================================================
# Lägger in ett nytt möte genom att plocka ut dagalmanackan ur
# månadsalmanackan ur årsalmanackan och därefter sätta ihop dem igen.
def boka_möte(årsalma, dag, mån, start, slut, info):
    "årsalmanacka x dag x månad x klockslag x klockslag x möte -> årsalmanacka"
    dagalma = dagalmanacka(dag, månadsalmanacka(mån, årsalma))
    möte = skapa_mötestid(skapa_tidsperiod(start, slut), info)
    return lägg_in_månadsalmanacka(
               mån,
               lägg_in_dagalmanacka(
                   dag,
                   lägg_in_möte(möte, dagalma),
                   månadsalmanacka(mån, årsalma)),
               årsalma)