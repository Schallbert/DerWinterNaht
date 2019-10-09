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
    listField = 0
    spotObjList = {}
    #get valid spot numbers for room
    for i in range(roomNumber, roomNumber+9):
        if i in dictSpots:
            #generate spots
            spotObjList[i] = Spot(i)
            listField = listField + 1
    return spotObjList

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
        self.spot_list = spotList(number)

    def onEnter(self):
        print(self.description + "\n")
        textReader("Ihr befindet euch " + self.name + ".\n\n")
        print("Ihr seht:")
        
        for element in self.spot_list.values():
            print(str(element.number) + ": "\
                  + element.name)
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
    10 : "Euer Smartphone. Kann so ziemlich alles und ist natürlich auch mit Taschenlampe, \
Kamera und Navigationssystem ausgestattet.\nHier draußen scheinen allerdings weder Mobilfunk\
noch Datenvervindung möglich zu sein.\nZudem ist der Akkustand niedrig und ihr habt keine Powerbank dabei.",
    11 : "Ein kaum leserliches Foto der Umgebungskare, aufgenommen mit dem Handy.\
Die Spiegelung der hellen Hauswand gegenüber links des Kastens hingegen zeigt alle Details.\n",
    12 : "Das Foto der Umgebungskarte.\nDie Karte ist scharf und detailliert zu erkennen.\n",
    13 : "Ein Standard Auto-Verbandkasten.\nNicht ganz klar, ob das jetzt bei einem Tagesausflug \
zu Fuß noch dem Credo 'Vorsicht ist die Mutter der Porzellankiste' \
entspricht\noder glattweg in die Schublade 'Panisch und übertrieben vorsichtig' fällt...\n",
    14 : "Wahnsinn, was Hunger im Einkaufsladen anrichten kann!\nEure Rucksäcke platzen fast vor \
Zutaten für eine wahre Picknick-Orgie. Wenn ihr das alles esst, werdet ihr wohl kaum weiterwandern wollen ;)\n",
    100 : "Eine Bahnstation in der tiefsten Eifel...\n",
    101 : "Eine große, ziemlich detaillierte Karte der Umgebung in einem etwas ramponiert \
aussehendem Glaskasten.\nDie Sonne spiegelt sich so sehr darin, dass man kaum etwas erkennen kann.\n\
Ihr Titel: 'Die V_____eifel: Mend__ ___ ____bung, 1:10000'\n",
    102 : "Der linke Pfosten des Glaskastens.\nEr trägt zwar Rostspuren, \
scheint aber grundsolide und tief im Boden verankert.\n",
    103 : "Die 'Adler-Apotheke' in Mendig. Kennste eine, kennste alle...\n",
    104 : "Ein REWE-Markt, ziemlich groß für diese Gegend.\n\
Der hat bestimmt alles, was man vergessen haben könnte.\n",
    105 : "Die große Karte der Umgebung ist jetzt verschattet, da eine von euch vor dem Pfosten steht.\
Man kann die Karte jetzt klar und deutlich erkennen.\n"
    }

#Defines room number and names
dictRooms = {
    100 : "Bahnhof Mendig",\
    110 : "Fußweg Maria Laach"\
    }

#Defines which rooms are in what way connected to which rooms
dictConnectedRooms = {
    100 : [110],\
    110 : [100, 120],\
    120 : [110, 130, 140],\
    130 : [120],\
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

dictInventory = {}

#Vorgeschichte!
#Room1: Train station Mendig, RB26, 1.5h from cologne     
currentRoom = Room(100)

#player1 = Player("Lukas", "red", 5,8)
#print(player1.name)
#print(player1.fitness)

currentRoom.onEnter()
activeSpot = currentRoom.spot_list[inputCheck("Was wollt ihr untersuchen? ", 3)]
activeSpot.action()



    

        
