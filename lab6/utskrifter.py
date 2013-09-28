# =========================================================================
#  Almanackan - Laboration i kursen Programmering i Python
#
#  Modul: utskrifter.py
#  Uppdaterad: 2004-07-30 av Peter Dalenius
#  Beroenden:
#    datatyper.py
# =========================================================================

from datatyper import *

## =========================================================================
##  1. Utskrift av enkla abstrakta datatyper
## =========================================================================
def skriv_timme(h):
    "timme ->"
    print(heltal(h), end='')

def skriv_minut(m):
    "minut ->"
    print(heltal(m), end='')

def skriv_dag(d):
    "dag ->"
    print(dagnummer(d), end='')

def skriv_månad(m):
    "månad ->"
    print(månadsnamn(m), end='')

def skriv_möte(m):
    "möte ->"
    print(mötestext(m), end='')


## =========================================================================
##  2. Utskrift av sammansatta abstrakta datatyper
## =========================================================================
def skriv_tidsrymd(tr):
    "tidsrymd ->"
    print('{0} tim, {1} min'.format(heltal(timdel(tr)), heltal(minutdel(tr))))

def skriv_klockslag(kl):
    "klockslag ->"
    print('{0}:{1}'.format(str(heltal(timdel(kl))).zfill(2),
                           str(heltal(minutdel(kl))).zfill(2)), end='')

def skriv_tidsperiod(tp):
    "tidsperiod ->"
    skriv_klockslag(start_klockslag(tp))
    print('-', end='')
    skriv_klockslag(slut_klockslag(tp))

def skriv_datum(d):
    "datum ->"
    skriv_dag(dagdel(d))
    print(' ', end='')
    skriv_månad(månadsdel(d))

def skriv_mötestid(mt):
    "mötestid ->"
    skriv_tidsperiod(tidsperioddel(mt))
    print(' ', end='')
    skriv_möte(mötesdel(mt))

def skriv_dagalmanacka(dagalma):
    "dagalmanacka ->"
    
    def skriv_dagalma_intern(mt):
        skriv_mötestid(mt)
        print()
    
    för_varje_möte(dagalma, skriv_dagalma_intern)


## =========================================================================
##  3. Övriga utskriftsfunktioner
## =========================================================================
def skriv_dagrubrik(d, m):
    "dag x månad ->"
    s = '{0} {1}'.format(dagnummer(d), månadsnamn(m))
    print(s)
    print('='*len(s))

def skriv_hjälptext():
    print('Följande kommandon finns i almanackans användargränssnitt:')
    print('    skapa(NAMN)')
    print('    almanackor()')
    print('    boka(NAMN, DAG, MÅNAD, START, SLUT, TEXT)')
    print('    avboka(NAMN, DAG, MÅNAD, START)')
    print('    visa(NAMN, DAG, MÅNAD)')
    print('    ledigt(NAMN, DAG, MÅNAD, START, SLUT)')
    print('    jämför(NAMN, NAMN, DAG, MÅNAD, START, SLUT, LÄNGD)')
    print('    importera_kurs(NAMN, KURS)')
    print('    importera_namn(NAMN, GRUPP)')
    print('    spara(FILNAMN)')
    print('    ladda(FILNAMN)')
    print()
    print('Så här anges parametrarna:')
    print('    DAG = ett heltal')
    print('    MÅNAD = en sträng (t.ex. \'januari\')')
    print('    START, SLUT, LÄNGD = en sträng (t.ex. \'10:30\')')
    print('    NAMN = en sträng betecknande användarens namn')