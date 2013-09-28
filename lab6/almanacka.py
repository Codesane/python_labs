# =========================================================================
#  Almanackan _ Laboration i kursen Programmering i Python
#
#  Modul: almanacka.py
#  Uppdaterad: 2004-11-10 av Peter Dalenius
#  Beroenden:
#    datatyper.py
#    bokningar.py
#    utskrifter.py
# =========================================================================

# Denna huvudmodul innehåller funktioner för att hålla reda på olika
# almanackor, göra bokningar och hitta lediga tider. Den består av två
# delar. Första delen innehåller rutiner för att hantera en global dict
# med olika namngivna almanackor. Den andra delen innehåller gränssnittet,
# dvs de funktioner som slutanvändaren förväntas använda sig av.

# För att utföra sina uppgifter använder sig almanacka.py av rutiner
# i bokningar.py och utskrifter.py. Dessa två moduler använder sig i
# sin tur av berakningar.py och primitiver.py enligt nedanstående figur:

#
#                       almanacka.py
#                            |
#           +________________+______________+
#           |                |              |
#      bokningar.py    utskrifter.py    import.py
#           |                |              |
#           +________________+______________+ 
#                            |
#                       datatyper.py

# De övriga filerna laddas in och evalueras automatiskt när du 
# evaluerar denna fil.

from datatyper import *
from bokningar import *
from utskrifter import *
from timeedit_import import *
import pickle;

# =========================================================================
#  1. Lagring av almanackor
# =========================================================================
almanackor = dict();

def hämta_almanacka(namn):
    if finns_almanacka(namn):
        return almanackor[namn]
    else:
        raise Exception("Ingen årsalmanacka med namnet {0} finns.".format(namn))

def lägg_in_almanacka(namn, årsalma):
    almanackor[namn] = årsalma
    return almanackor

def finns_almanacka(namn):
    return namn in almanackor

def skapa_almanacka(namn):
    almanackor[namn] = skapa_årsalmanacka()
    return almanackor

# Sparar alla existerande almanackor i en fil. Almanackorna läggs i en lista
# ihop med strängen '*ALMANACKA*' för verifikation i funktionen
# ladda_almanacka.
def spara_almanacka(filnamn):
    "sträng ->"
    output = open(filnamn, 'wb')
    pickle.dump(['*ALMANACKA*', almanackor], output)
    output.close()

# Laddar almanckor från en fil. Om filen inte finns eller om filen ej är i
# förväntat format (som angivet i spara_almanacka) blir de gamla almanackorna
# kvar i minnet.
def ladda_almanacka(filnamn):
    "sträng -> sanningsvärde"
    try:
        pkl_file = open(filnamn, 'rb')
        lista = pickle.load(pkl_file)
        pkl_file.close()
        if isinstance(lista, list) and\
         len(lista) == 2 and\
         lista[0] == '*ALMANACKA*':
            global almanackor
            almanackor = lista[1]
            return True
        else:
            return False
    except IOError:
        return False

# =========================================================================
#  2. Användargränssnitt
# =========================================================================

def hjälp():
    "->"
    (skriv_hjälptext)

def skapa(namn):
    "sträng ->"
    if finns_almanacka(namn):
        print("Det finns redan en almanacka med namnet {0}.".format(namn))
    else:
        skapa_almanacka(namn)
        print("En ny almanacka med namnet {0} har skapats.".format(namn))

def visa_almanackor():
    "->"
    if almanackor:
        print("Följande almanackor finns:")
        for namn in almanackor:
            print(namn)
    else:
        print("Det finns inga skapade almanackor.")

def boka(namn, d, m, t1, t2, text):
    "sträng x heltal x sträng x sträng x sträng x sträng ->"
    dag = skapa_dag(d)
    mån = skapa_månad(m)
    start = omvandla_klockslag(t1)
    slut = omvandla_klockslag(t2)
    möte = skapa_möte(text)
    dagalma = dagalmanacka(dag, månadsalmanacka(mån, hämta_almanacka(namn)))
    
    skapa_datum(dag, mån) # Testa om det är ett giltigt datum.
    
    if är_före_klockslag(slut, start):
        print("Klockslagen är i fel ordning.")
    elif är_bokat(dagalma, skapa_tidsperiod(start, slut)):
        print("Tiden är redan bokad.")
    else:
        lägg_in_almanacka(namn, boka_möte(hämta_almanacka(namn),
                                          dag, mån, start, slut, möte))
        print("Mötet är bokat.")

def visa(namn, d, m):
    "sträng x heltal x sträng ->"
    dag = skapa_dag(d)
    mån = skapa_månad(m)
    dagalma = dagalmanacka(dag, månadsalmanacka(mån, hämta_almanacka(namn)))
    
    skapa_datum(dag, mån) # Testa om det är ett giltigt datum.
    
    if är_tom_dagalmanacka(dagalma):
        print("Det finns inga bokningar.\n")
    else:
        skriv_dagrubrik(dag, mån)
        skriv_dagalmanacka(dagalma)

def importera_kurs(namn, kurskod):
    "sträng x sträng ->"
    lägg_in_almanacka(namn, importera_schema_för_kurs(kurskod))
    print("Almanackan är importerad.")

def importera_lärare(namn, liu_id):
    "sträng x sträng ->"
    lägg_in_almanacka(namn, importera_schema_för_lärare(liu_id))
    print("Almanackan är importerad.")

def importera_grupp(namn, grupp):
    "sträng x sträng ->"
    lägg_in_almanacka(namn, importera_schema_för_grupp(grupp))
    print("Almanackan är importerad.")

def spara (filnamn):
    "sträng ->"
    spara_almanacka(filnamn)
    print("Almanackorna är sparade i filen {0}.".format(filnamn))

def ladda (filnamn):
    "sträng ->"
    if ladda_almanacka(filnamn):
        print("Nya almanackor har laddats.")
    else:
        print("Filen finns ej eller innehåller inga sparade almanackor.")