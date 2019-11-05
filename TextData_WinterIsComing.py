from enum import IntEnum

test = "Hallo"

# Enums and data structures
#----------------------------------------------
class Action_id(IntEnum):
    VIEW = 0
    GOTO = 1
    OPEN = 2
    USE = 3
    GET = 4
    NOC_YES = 5 #NO Choice, answer is YES
    NOC_NO = 6 #NO Choice, answer is NO

class Mod_typ(IntEnum):
    EFFONE = 0 #Once usable, effect on calling player
    EFFALL = 1 #Once usable, effect on all players
    NOTUSABLE = 2 #Item that cannot be used without a combination
    PERMANENT = 3 #Item cannot be consumed, it is permanently available

#----------------------------------------------
#DICTIONARIES
#----------------------------------------------
#text ID rules:
# xx     = Item
# xxx    = Spot/room
# xxxx   = combinations of item --> new item
# xxxxx  = combination of item and spot --> action
# xxxxxx = action within a room 


actionDict = {
    0 : " genauer untersuchen?",
    1 : " betreten?",
    2 : " öffnen?",
    3 : " benutzen?",
    4 : " nehmen?"
    }

#Text Dictionary by IDs:
dictTexts = {
    10 : \
"Euer Smartphone. Kann so ziemlich alles und ist natürlich auch mit Taschenlampe,\n\
Kamera und Navigationssystem ausgestattet.\n\
Hier draußen scheinen leider weder Mobilfunk noch Datenvervindung möglich zu sein.\n\
Zudem ist der Akkustand niedrig und ihr habt keine Powerbank dabei.",
    11 : \
"Ein kaum leserliches Foto der Umgebungskare, aufgenommen mit dem Handy.\n\
Die Spiegelung der hellen Hauswand gegenüber links des Kastens hingegen zeigt alle Details.\n",
    12 : \
"Das Foto der Umgebungskarte.\n\
Die Karte ist scharf und detailliert zu erkennen.\n",
    13 : \
"Ein Standard Auto-Verbandkasten.\n\
Nicht ganz klar, ob das jetzt bei einem Tagesausflug zu Fuß noch dem Credo\n\
'Vorsicht ist die Mutter der Porzellankiste' entspricht oder glattweg\n\
in die Schublade 'Panisch und übertrieben vorsichtig' fällt...\n",
    14 : \
"Wahnsinn, was Hunger im Einkaufsladen anrichten kann!\n\
Eure Rucksäcke platzen fast vor Zutaten für eine wahre Picknick-Orgie.\n\
Wenn ihr das alles esst, werdet ihr wohl kaum weiterwandern wollen ;)\n",
    100 : \
"Eine Bahnstation in der tiefsten Eifel...\n",
    101 : \
"Eine große, ziemlich detaillierte Karte der Umgebung in einem etwas ramponiert\n\
aussehendem Glaskasten.\n\
Die Sonne spiegelt sich so sehr darin, dass man kaum etwas erkennen kann.\n\
Ihr Titel: 'Die V_____eifel: Mend__ ___ ____bung, 1:10000'\n",
    102 : \
"Der linke Pfosten des Glaskastens.\nEr trägt zwar Rostspuren,\n\
scheint aber grundsolide und tief im Boden verankert.\n",
    103 : \
"Die 'Adler-Apotheke' in Mendig. Kennste eine, kennste alle...\n",
    104 : \
"Ein REWE-Markt, ziemlich groß für diese Gegend.\n\
Der hat bestimmt alles, was man vergessen haben könnte.\n",
    105 : \
"Die große Karte der Umgebung ist jetzt verschattet, da jemand von euch\n\
vor dem Pfosten steht. Man kann die Karte jetzt klar und deutlich erkennen.\n",
    110 : \
"Der Fußweg zu eurem ersten Etappenziel Maria Laach.\n\
Ihr wolltet ungern an der Landstraße entlang gehen und habt euch für diesen\n\
zugewachsenen, schmalen Pfad entschieden,\n\
den das Wild sicher auch als Weg benutzt. Die Sonne blinzelt immer wieder\n\
durch das Blätterdach, es duftet nach Heckenrosen und ab und zu erhascht ihr\n\
einen Blick auf den Wald.\n\
Schließlich gelangt ihr an eine Weggabelung in einer kleinen Senke.\n\
Der Wegweiser wird den letzten Winter wohl nicht überlebt haben,\n\
sein mit abgebrochener Stumpf ragt ein paar Zentimeter aus dem Boden.\n",
    120: \
"Nach ein paar hundert Metern sanft bergab verläuft sich der Weg\n\
und endet in lockeren, aber leicht erhöhten, festen Grasbüscheln.\n\
Die Natur hat euch hier förmlich verschluckt.\n\
Doch - halt - was glitzert da hinten im Gras?\n",
    130: \
"Hier geht es eindeutig bergauf. Nicht, dass ihr das am Gelände sehen könnt,\n\
nein, dafür ist das Unterholz viel zu dicht, aber es ist irgendwie...\n\
anstrengend und wird eher noch anstrengender. \n\
Vorne seht ihr eine Lichtung, vielleicht gut für eine Rast?\n",
    10101: \
"Ihr nehmt ein Foto der Übersichtskarte auf, um es euch später ansehen zu können.\n\
Gute Idee!",
    10105: \
"Ihr nehmt ein Foto der Übersichtskarte auf, um es euch später ansehen zu können.\n\
Gute Idee!"
    }

#Defines what happens on closer investigation or usage of an item
dictAction = {
    13: \
"Ihr beschließt, den Verbandkasten zu benutzen, um eure Wunden\n\
und die eurer möglichen Begleiter zu versorgen. Das funktioniert prima!\n\
(Euch ist natürlich klar, dass das jetzt nur einen Effekt hatte,\n\
wenn ihr auch wirklich verletzt wart. Sonst sieht es einfach nur albern aus,\n\
in Rettungsdecke und mit Verbänden und Pflastern übersät herumzulaufen)\n",
    14: \
"Jetzt ein Picknick! Ihr lasst euch auf der mitgebrachten Decke nieder und genießt\n\
ein fürstliches Mahl in der Natur. Auch wenn ihr jetzt wieder motivierter seid,\n\
euren Ausflug fortzusetzen, so hat euch das viele Essen doch ein Kantinenkoma beschert.\n",
    101 : \
"Der Kartenausschnitt scheint perfekt zu eurer geplanten Tour zu passen,\n\
nur leider könnt ihr wegen der Spiegelung im Glas nichts Genaues erkennen.\n",
    102 : \
"Du stehst am Pfosten des Kartenkastens.\n\
An dieser Position schattest du den Kartenkasten ab,\n\
sodass die Karte einwandfrei lesbar ist.\n",
    103 : \
"Ihr betretet die Apotheke. Warum, das ist euch selbst noch nicht ganz\n\
klar geworden, als euch schon ein freundlicher Herr hohen Alters mit Haarkranz,\n\
goldener Brille und weißem Kittel - ganz nach dem Klischee - anspricht.\n\
Aus Verlegenheit kauft ihr einen Verbandkasten.\n\
Tja, dieses sperrige Stück muss nun den ganzen Weg mitgeschleppt werden.\n",
    104 : \
"Hach, ganz wie zu Hause! So eine Zugfahrt macht echt hungrig, und so\n\
kauft ihr, obwohl ihr euch natürlich ein paar Brote geschmiert habt, einen\n\
ganzen Haufen Lebensmittel zusammen. Wohl bekomm's!\n\
Nur leider ist so ein Einkauf auch immer etwas anstrengend...\n",
    105 : \
"Die Übersichtskarte ist jetzt perfekt lesbar.\n"
    }

#Defines what happens if a closer investigation of spot is refused
dictActionRefused = {
    # TODO
    }

#Action type of the spot when visited
dictActionType = {
    101 : Action_id.VIEW,\
    102 : Action_id.NOC_YES,\
    103 : Action_id.GOTO,\
    104 : Action_id.GOTO,\
    105 : Action_id.VIEW\
    }
    
#Defines room number and names
dictRooms = {
    100 : "Bahnhof Mendig",\
    110 : "Fußweg Maria Laach",\
    120 : "Sumpf im Wald",\
    130 : "Fuß des Hügels vor dem Bergkamm",\
    140 : "Wiese auf dem Bergkamm"\
    }

#Defines which rooms are in what way connected to which rooms
dictConnectedRooms = {
    100 : [110],\
    110 : [100, 120, 130],\
    120 : [110],\
    130 : [110, 140],\
    #...
    }

#Defines spot number and names
dictSpots = {
    101 : "die Übersichtskarte",\
    102 : "der Pfosten eines Kartenkastens",\
    103 : "die Apotheke am Bahnhof",\
    104 : "der REWE-Markt",\
    105 : "die Übersichtskarte, verschattet"\
    }

#Defines how spots are connected to items   
dictSpotItems = {
    10101 : [11],\
    103 : [13],\
    104 : [14],\
    10105 : [12]\
    }

#Defines which spots can change through interaction
#with spot or item combination
# Trigger : [[Exchange targets], [Exchange spots]]
dictSpotChange = {
    102: [[101], [105]]
    }

#Defines item number and names
dictItems = {
    10 : "Ein Smartphone",\
    11 : "Ein Foto der Umgebungskarte",\
    12 : "Ein Foto der Umgebungskarte",\
    13 : "Ein Verbandkasten",\
    14 : "Eine ordentliche Mahlzeit für mehrere Personen"\
    }

#Defines item modifiers
# [0] = motivation, [1] = tiredness
dictMods = {
    11 : [0,1],\
    12 : [1,-1],\
    13 : [5,-1],\
    14 : [-2,-5],\
    104 : [0,-1]\
    }

dictModType = {
    10 : Mod_typ.PERMANENT,\
    11 : Mod_typ.NOTUSABLE,\
    12 : Mod_typ.PERMANENT,\
    13 : Mod_typ.EFFALL,\
    14 : Mod_typ.EFFALL,\
    104 : Mod_typ.EFFONE\
    }

dictModsRefused = {
    #TODO: add
    }