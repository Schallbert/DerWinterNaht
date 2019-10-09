#import pygame
import datetime
import time
from enum import IntEnum

# General Helper functions
#----------------------------------------------
def textReader(text):
    for text in text:
            print(text, end="")
            time.sleep(.04)
            #add blip-like sound on output?

def quitSave():
    print("Speichern...")
    save()
    print("Spiel wird beendet.")
    quit()

def save():
    print("IMPLEMENT SAVE!")
    print("Gespeichert!")

def inputCheck(text, expNumOfDigits):
    number = 1000000
    inptLoop = True
    while inptLoop:
        resp = input(text)
        try :
            number = int(resp)
        except :
            if resp.lower() == "quit":
                quitSave()
            else:
                print("Bitte eine Zahl eingeben oder das Spiel mittels 'quit' beenden.")
        resp = len(resp)  
        if resp == expNumOfDigits:
            inptLoop = False
            return number
        else:
            print("Bitte eine Ganzzahl mit " + str(expNumOfDigits) + " Stellen eingeben.")              

#----------------------------------------------

# Data structure helper functions
#----------------------------------------------
def spotList(roomNumber):
    """Generates a list of spots that the roon contains
    based on room number, using spot dictionary."""
    spotObjList = {}
    #get valid spot numbers for room
    for i in range(roomNumber, roomNumber+9):
        if i in dictSpots:
            #generate spots
            spotObjList[i] = Spot(i)
    return spotObjList

def roomList(roomNumber):
    roomObjList = {}
    for i in range(0, len(dictConnectedRooms[roomNumber])):
        #generate adjacent rooms
        roomObjList[dictConnectedRooms[roomNumber][i]] = Room(dictConnectedRooms[roomNumber][i])
    return roomObjList
    
#----------------------------------------------
def itemBuilder(generateFromNr):
    """Generates the item connected to the spot, if any"""
    #check if called via spot (3-digit) number
    if len(str(generateFromNr)) == 3:
        if generateFromNr in dictItems:
            if (not generateFromNr in dictInventory):
                dictInventory[dictSpotItems[generateFromNr]]= Item(dictSpotItems[generateFromNr])
                print("Der Gegenstand " + dictItems[dictSpotitems[generateFromNr]] + " wurde dem Inventar hinzugefügt.")      
            else:
                print("Das ist bereits im Inventar...")
        else:
            print("Der Gegenstand existiert nicht...?")
    #check if called via item-item combination (4-digit) number
    elif len(str(generateFromNr)) == 4:
        item1 = int(generateFromNr)/100
        item2 = generateFromNr%100
        if (item1 in dictInventory) & (item2 in dictInventory):
            #only add items if both are available in inventory
            if generateFromNr in dictItems:
                dictInventory[dictSpotItems[generateFromNr]]= Item(dictSpotItems[generateFromNr])
            else:
                print("Das lässt sich nicht kombinieren!")
        else:
            print("Nette Idee, allerdings habt ihr die Gegenstände " + str(item1) + \
                  " und " + str(item2) + " nicht beide im Inventar...")
    #check if called via item-spot combination
    elif len(str(generateFromNr)) == 5:
        item = int(generateFromNr)/1000
        spot = generateFromNr%1000
        if generateFromNr in dictUseItems:
            print("TODO: Allow combine items with surrounding.")
            
        
 
# Enums and data structures
#----------------------------------------------
class Action_id(IntEnum):
    VIEW = 0
    GOTO = 1
    OPEN = 2
    USE = 3
    GET = 4
    NOC = 5

actionDict = {
    0 : " genauer untersuchen?",
    1 : " betreten?",
    2 : " öffnen?",
    3 : " benutzen?",
    4 : " nehmen?"
    }
#----------------------------------------------
    
# Game classes
#----------------------------------------------
class Room:
    """A place, room, or scene within the game.
    It has a 3-digit number, of which the first two refer to the room
    and the last digit will be 0 as it is the spot ID."""
    def __init__(self, number):
        self.number = number
        self.name = dictRooms[number]
        self.description = dictTexts[number]

    def onEnter(self):
        dictRoomsInventory.append(self.number)
        self.spot_list = spotList(self.number)
        self.room_list = roomList(self.number)
        textReader(self.description)
        textReader("Ihr befindet euch bei " + str(self.number) + ": "\
                   + self.name + ".\n\n")
        print("Ihr seht:")
        for element in self.spot_list.values():
            print(str(element.number) + ": "\
                  + element.name)
            time.sleep(.5)
        print("\nVon hier aus sind folgende Orte erreichbar:")
        for element in self.room_list.values():
            if element.number < self.number:
                #room is known
                print(str(element.number) + ": "\
                      + element.name)
            else:
                print(str(element.number) + ": ???")
            time.sleep(.5)

class Spot:
    """A spot within a room, referred to as a 3-Digit number.
    The first two digits stand for the room in which the spot is
    and the last digit is the spot ID"""
    def __init__(self, number):
        self.number = number
        self.name = dictSpots[number]
        self.description = dictTexts[number]
        self.action_id = dictSpotActions[number]
        self.item_id = dictSpotItems[number]

    def action(self):
        """Interaction with the spot depending on context VIEW, GOTO, OPEN, GET or NOCHOICE
        May modify character's properties or set flags plot changes"""
        print("\nIhr untersucht " + self.name + ":")
        textReader(self.description)
        if self.action_id < Action_id.NOC:
            print("Möchtet ihr " + self.name + actionDict[self.action_id])
            resp = input("Bitte eingeben: JA: '1', NEIN: '0'. ")
            
            if resp == "1": 
                print("HAT GEKLAPPT JAJAJAJAAA")
            else:
                print("FEIGLING!")
        else:
            print("KEINE WAHL MUAHAHAH")
            

class Item:
    """An item is possibly combineable with other items or with a spot within
    a room. It carries a two-digit item ID. It may permanently or temporarily
    modify the obtaining character's properties."""
    def __init__(self, number, name, mod_fit, mod_mot):
        self.number = number
        self.name = name
        self.description = dictTexts[number]
        self.mod_fit = mod_fit
        self.mod_mot = mod_mot

class Player:
    def __init__(self, name, color, fitness, motivation):
        self.name = name
        self.color = color
        self.fitness = fitness
        self.motivation = motivation

    def ChangeMotivation(by_value):
        self.motivation = self.motivaiton + by_value

    def ChangeFitness(by_value):
        self.fitness = self.fitness + by_value

#----------------------------------------------

#DICTIONARIES
#----------------------------------------------
#text ID rules:
# xx     = Item
# xxx    = Spot/room
# xxxx   = combinations of item --> new item
# xxxxx  = combination of item and spot --> action
# xxxxxx = action within a room 

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
zugewachsenen, schmalen Weg entschieden,\n\
den das Wild sicher auch als Straße benutzt. Die Sonne blinzelt immer wieder\n\
durch das Blätterdach, es duftet nach Heckenrosen und ab und zu erhascht ihr\n\
einen Blick auf den Wald.\n\
Schließlich gelangt ihr an eine Weggabelung in einer kleinen Senke.\n\
Der Wegweiser wird den letzten Winter wohl nicht überlebt haben,\n\
sein mit zackigen Holzsplittern versehener Stumpf ragt\n\
ein paar Zentimeter aus dem Boden.\n",
    120: \
"Nach ein paar hundert Metern sanft bergab verläuft sich der Weg\n\
und endet in lockeren, aber leicht erhöhten, festen Grasbüscheln.\n\
Die Natur hat euch hier förmlich verschluckt.\n\
Doch - halt - was glitzert da hinten im Gras?\n",
    130:
"Hier geht es eindeutig bergauf. Nicht, dass ihr das am Gelände sehen könnt,\n\
nein, dafür ist das Unterholz viel zu dicht, aber es ist irgendwie...\n\
anstrengend und wird eher noch anstrengender. \n\
Vorne seht ihr eine Lichtung, vielleicht gut für eine Rast?\n"
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
    105 : "die Übersichtskarte, verschattet"
    }

#Defines item number and names
dictItems = {
    10 : "Ein Smartphone",\
    11 : "Ein Foto der Umgebungskarte",\
    12 : "Ein Foto der Umgebungskarte",\
    13 : "Ein Verbandkasten",\
    14 : "Eine ordentliche Mahlzeit für mehrere Personen"\
    }

#Defines how spots are connected to items   
dictSpotItems = {
    101 : 11,\
    102 : None,\
    103 : 13,\
    104 : 14,\
    105 : 12\
    }

#Defines item modifiers
dictMods = {
    10 : [0,0],\
    11 : [0,-1],\
    12 : [0,1],\
    13 : [5,1],\
    14 : [3,-2]\
    }

#Defines which actions can be performed on spots  
dictSpotActions = {
    101 : Action_id.VIEW,\
    102 : Action_id.NOC,\
    103 : Action_id.GOTO,\
    104 : Action_id.GOTO,\
    105 : Action_id.VIEW\
    }

dictItemsInventory = []
dictRoomsInventory= []

#Vorgeschichte!
#Room1: Train station Mendig, RB26, 1.5h from cologne     
currentRoom = Room(100)

#player1 = Player("Lukas", "red", 5,8)
#print(player1.name)
#print(player1.fitness)

#enter a room routine
currentRoom.onEnter()
playerAction = inputCheck("Was wollt ihr untersuchen? ", 3)
print("\n")
if playerAction in dictRooms:
    #player selected a room
    currentRoom = currentRoom.room_list[playerAction]
    currentRoom.onEnter()
elif playerAction in dictSpots:
    #player selected a spot
    activeSpot = currentRoom.spot_list[playerAction]
else:
    #player selected an item, an item-item combination, or an item-spot combination
    print("TODO: as per comment above")



    

        
