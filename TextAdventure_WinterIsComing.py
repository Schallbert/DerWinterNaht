#import pygame
import datetime
import time
from enum import IntEnum         
 
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
in die Schublade 'Panisch und übertrieben vorsichtig' fällt...\n\
Zum Benutzen kombiniert ich den Gegenstand mit sich selbst.\n",
    14 : \
"Wahnsinn, was Hunger im Einkaufsladen anrichten kann!\n\
Eure Rucksäcke platzen fast vor Zutaten für eine wahre Picknick-Orgie.\n\
Wenn ihr das alles esst, werdet ihr wohl kaum weiterwandern wollen ;)\n\
Zum Benutzen kombiniert ich den Gegenstand mit sich selbst.\n",
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
    1313: \
"Ihr beschließt, den Verbandkasten zu benutzen, um eure Wunden\n\
und die eurer möglichen Begleiter zu versorgen. Das funktioniert prima!\n\
(Euch ist natürlich klar, dass das jetzt nur einen Effekt hatte,\n\
wenn ihr auch wirklich verletzt wart. Sonst sieht es einfach nur albern aus,\n\
in Rettungsdecke und mit Verbänden und Pflastern übersät herumzulaufen)\n",
    1414: \
"Jetzt ein Picknick! Ihr lasst euch auf der mitgebrachten Decke nieder und genießt\n\
ein fürstliches Mahl in der Natur. Auch wenn ihr jetzt wieder motivierter seid,\n\
euren Ausflug fortzusetzen, so hat euch das viele Essen doch ein Kantinenkoma beschert.\n"
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

#Defines which actions can be performed on spots  
dictSpotActions = {
    101 : Action_id.VIEW,\
    102 : Action_id.NOC,\
    103 : Action_id.GOTO,\
    104 : Action_id.GOTO,\
    105 : Action_id.VIEW\
    }

#Defines what happens on closer investigation or usage of an item
dictAction = {
    101 : \
"Der Kartenausschnitt scheint perfekt zu eurer geplanten Tour zu passen,\n\
nur leider könnt ihr wegen der Spiegelung im Glas nichts Genaues erkennen.\n",
    102 : \
"Du stehst am Pfosten des Kartenkastens.\n\
An dieser Position schattest du den Kartenkasten ab,\n\
sodass die Karte einwandfrei lesbar ist.\n",
    103 : \
"Ihr betretet die Apotheke. Warum, das ist euch selbst noch nicht klargeworden,\n\
als euch schon ein freundlicher Herr hohen Alters mit Haarkranz,\n\
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

#Defines how spots are connected to items   
dictSpotItems = {
    101 : [11],\
    102 : [None],\
    103 : [13],\
    104 : [14],\
    105 : [12]\
    }

#Defines item number and names
dictItems = {
    10 : "Ein Smartphone",\
    11 : "Ein Foto der Umgebungskarte",\
    12 : "Ein Foto der Umgebungskarte",\
    13 : "Ein Verbandkasten",\
    14 : "Eine ordentliche Mahlzeit für mehrere Personen",\
    1313 : "Der Verbandkasten ist verbraucht.",\
    1414 : "Die Überreste eurer Mahlzeit in Form von Müll."\
    }

#Defines item modifiers
# [0] = fitness, [1] = motivation
dictMods = {
    10 : [0,0],\
    11 : [0,-1],\
    12 : [0,1],\
    1313 : [5,1],\
    1414 : [-2,3],\
    104 : [0,-1]\
    }

dictModsRefused = {
    #TODO: add
    }

dictInventory = {}
listRoomsVisited= []
listItemsYielded = []

    
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
        listRoomsVisited.append(self.number)
        self.spot_list = spotBuilder(self.number)
        self.room_list = roomBuilder(self.number)
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
            if element.number in listRoomsVisited:
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

    def action(self):
        """Interaction with the spot depending on context VIEW, GOTO, OPEN, GET or NOCHOICE
        May modify character's properties or set flags plot changes"""
        print("\nIhr untersucht: " + self.name)
        textReader(self.description)
        if self.action_id < Action_id.NOC:
            textReader("Möchtet ihr " + self.name + actionDict[self.action_id] + "\n")
            resp = inputCheck("Bitte eingeben: JA: '1', NEIN: '0'. ")           
            if resp == 1: 
                if self.number in dictAction:
                    textReader(dictAction[self.number])
                if self.number in dictMods:
                    changeMod(dictMods[self.number])
            else:
                if self.number in dictActionRefused:
                    textReader(dictActionRefused[self.number])
                else:
                    textReader("Ja, manchmal ist es auch gut, Dinge NICHT zu tun.\n")
                if self.number in dictModsRefused:
                    changeMod(dictMods[self.number])
        else:
            if self.number in dictAction:
                textReader(dictAction[self.number])
            if self.number in dictMods:
                changeMod(dictMods[self.number])
            

class Item:
    """An item is possibly combineable with other items or with a spot within
    a room. It carries a two-digit item ID. It may permanently or temporarily
    modify the obtaining character's properties."""
    def __init__(self, number):
        self.number = number
        self.name = dictItems[number]
        self.description = dictTexts[number]
        self.mod = dictMods[number]
        #allow different kinds of item:
        # -self-using directly
        # -self-using over time
        # -can be used once
        # -permanent

class Player:
    maxMod = [10, 10]
    def __init__(self, number, name, color, *mod):
        self.number = number
        self.name = name
        self.color = color
        self.mod = mod

    def GetMod(self):
        return self.mod

    def ChangeMod(self, *valueList):
        for i in self.mod:
            self.mod[i] = self.mod[i] + valueList[i]
            if self.mod[i] > maxMot:
                self.motd[i] = maxMot
            elif self.mod[i] < 1:
                print("TODO: GAME OVER")

#----------------------------------------------
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

def inputCheck(text):
    number = 1000000
    inptLoop = True
    while inptLoop:
        resp = input(text)
        try :
            number = int(resp)
            inptLoop = False
            return number
        except :
            if resp.lower() == "quit":
                quitSave()
            else:
                print("Bitte eine Zahl eingeben oder das Spiel mittels 'quit' beenden.")              
#----------------------------------------------
#----------------------------------------------
# Object builder functions
#----------------------------------------------
def spotBuilder(roomNumber):
    """Generates a list of spots that the roon contains
    based on room number, using spot dictionary."""
    spotObjList = {}
    #get valid spot numbers for room
    for i in range(roomNumber, roomNumber+9):
        if i in dictSpots:
            #generate spots
            spotObjList[i] = Spot(i)
    return spotObjList
#----------------------------------------------
def roomBuilder(roomNumber):
    roomObjList = {}
    for i in range(0, len(dictConnectedRooms[roomNumber])):
        #generate adjacent rooms
        roomObjList[dictConnectedRooms[roomNumber][i]] = Room(dictConnectedRooms[roomNumber][i])
    return roomObjList
#----------------------------------------------
def itemBuilder(itemNumber):
    """This function generates the item object in the inventory
    and adds its  number to the list of items the players received already"""
    dictInventory[itemNumber] = Item(itemNumber)
    listItemsYielded.append(itemNumber)
#----------------------------------------------
def itemList(spotNumber):
    itemObjList = {}
    for i in range(0, len(dictSpotItems[spotNumber])):
        #generate adjacent rooms
        itemHandler(spotNumber)
#----------------------------------------------
#----------------------------------------------
# Handlers
#----------------------------------------------
def itemHandler(generateFromNr):
    nrOfDigits = len(str(generateFromNr))
    if nrOfDigits == 2:
        itemInfo(generateFromNr)
    elif nrOfDigits == 3:
        itemFromSpot(generateFromNr)
    elif nrOfDigits == 4:
        itemItem(generateFromNr)
    elif nrOfDigits == 5:
        itemSpot(generateFromNr)
    else:
        print("Kein bekanntes Kommando.")
#----------------------------------------------
def itemInfo(generateFromNr):
    """Generates the item connected to the spot, if any"""
    #check if it is just an item (2-digit) number
    if generateFromNr in dictItems:
        if generateFromNr in dictInventory:
            #show item information 
            obj = dictInventory[generateFromNr]
            textReader("Information zum Gegenstand " + str(obj.number)\
                        + ": " + obj.name\
                        + "\n" + obj.description)
        else:
            print("Leider hast du diesen Gegenstand nicht im Inventar...")      
    else:
        print("Dieses Objekt existiert nicht...?")
#----------------------------------------------        
def itemFromSpot(generateFromNr):
    if generateFromNr in dictItems:
        if (not generateFromNr in listItemsYielded):
            objRef = dictSpotItems[generateFromNr]
            itemBuilder(objRef) #generate item
            textReader("Der Gegenstand " + dictInventory[objRef].number + ": "\
                  + dictInventory[objRef].name + " wurde dem Inventar hinzugefügt.")      
        else:
            print("Das ist bereits im Inventar oder wurde verbraucht...")
    else:
        print("Dieses Objekt existiert nicht...?")
#----------------------------------------------        
def itemItem(generateFromNr):
    item1 = int(generateFromNr)/100
    item2 = generateFromNr%100
    if (item1 in dictInventory) & (item2 in dictInventory):
        #only add items if both are available in inventory
        if generateFromNr in dictItems:
            dictInventory[dictSpotItems[generateFromNr]]= Item(dictSpotItems[generateFromNr])
            if item1 == item2: #items used on player
                del dictInbentory[item1]
            else: #original items deleted on combination
                del dictInbentory[item1]
                del dictInbentory[item2]
        else:
            print("Das lässt sich nicht kombinieren!")
    else:
        print("Nette Idee, allerdings habt ihr die Gegenstände " + str(item1) + \
              " und " + str(item2) + " nicht beide im Inventar...")
#----------------------------------------------
def itemSpot(generateFromNr):
    item = int(generateFromNr)/1000
    spot = generateFromNr%1000
    if generateFromNr in dictUseItems:
        print("TODO: Allow combine items with surrounding.")
#----------------------------------------------
def changeMod(modifierList):
    currentPlayer.ChangeMod(modifierList)
    if modifierList[0] > 0:
        textReader("Cool, deine Motivation erhöht sich auf: " + \
                   currentPlayer.GetMod)
    elif modifierList[0] < 0:
        textReader("Schade, deine Motivation lässt nach: " + \
                   currentPlayer.GetMod)
    if modifierList[1] > 0:
        textReader("Cool, deine Fitness erhöht sich auf: " + \
                   currentPlayer.GetMod)
    elif modifierList[1] < 0:
        textReader("Schade, deine Fitness lässt nach: " + \
                   currentPlayer.GetMod)
    # TODO: low/no stat left : End game/delay etc.
#----------------------------------------------    
#----------------------------------------------

playerList = [Player(1, "Lukas", "red", [5,10]), Player(2, "Marie", "green", [7,6])]

#Vorgeschichte!      
#Room1: Train station Mendig, RB26, 1.5h from cologne
currentPlayer = playerList[0]
currentRoom = Room(100)

#generate inventory
itemBuilder(10)
#enter a room routine
currentRoom.onEnter()
while True:
    textReader(currentPlayer.name + " ist an der Reihe.\n")
    playerAction = inputCheck("Was wollt ihr tun? ")
    print("\n")
    if playerAction in dictRooms:
        #player selected a room
        currentRoom = currentRoom.room_list[playerAction]
        currentRoom.onEnter()
    elif playerAction in dictSpots:
        #player selected a spot
        activeSpot = currentRoom.spot_list[playerAction]
        activeSpot.action()
    else:
        #player selected an item, an item-item combination, or an item-spot combination
        itemHandler(playerAction)
    if currentPlayer.number == 1:
        currentPlayer = playerList[1]
    else:
        currentPlayer = playerList[0]

        
