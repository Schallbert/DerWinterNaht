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

class Mod_typ(IntEnum):
    EFFONE = 0 #Once usable, effect on calling player
    EFFALL = 1 #Once usable, effect on all players
    NOTUSABLE = 2 #Item that cannot be used without a combination

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
    102 : Action_id.NOC,\
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
    14 : [-2,-4],\
    104 : [0,-1]\
    }

dictModType = {
    10 : Mod_typ.NOTUSABLE,\
    11 : Mod_typ.NOTUSABLE,\
    12 : Mod_typ.NOTUSABLE,\
    13 : Mod_typ.EFFALL,\
    14 : Mod_typ.EFFALL,\
    104 : Mod_typ.EFFONE\
    }

dictModsRefused = {
    #TODO: add
    }

dictInventory = {}
listRoomsVisited = []
listItemsYielded = []
listPlayers = []

    
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
        self.spot_list = spotBuilder(self.number)
        self.room_list = roomBuilder(self.number)
        if self.number not in listRoomsVisited:
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
        listRoomsVisited.append(self.number)

class Spot:
    """A spot within a room, referred to as a 3-Digit number.
    The first two digits stand for the room in which the spot is
    and the last digit is the spot ID"""
    def __init__(self, number):
        self.number = number
        self.description = dictTexts[number]
        self.name = dictSpots[number]
        self.__action_id = dictActionType[number]
        if number in dictMods:
            self.__mod = dictMods[number]
        if number in dictModType:
            self.__modType = dictModType[number]

    def action(self):
        """Interaction with the spot depending on context VIEW, GOTO, OPEN, GET or NOCHOICE
        May modify character's properties or set flags plot changes"""
        print("\nIhr untersucht: " + self.name)
        textReader(self.description)
        if self.__action_id < Action_id.NOC:
            textReader("Möchtet ihr " + self.name + actionDict[self.__action_id] + "\n")
            resp = inputCheck("Bitte eingeben: JA: '1', NEIN: '0'. ")
            if resp == 1:
                if self.number in dictAction:
                    textReader(dictAction[self.number])
                if self.number in dictMods:
                    invokeChangeMod(self.__mod, self.__modType)
                if self.number in dictSpotItems:
                    #create items as found in list
                    for element in range(0, len(dictSpotItems[self.number])):
                        itemId = dictSpotItems[self.number][element]
                        Item(itemId)
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
        """Initiates the item and its properties. Properties are number, description,
        name, Item_type (see enum) and modificators."""
        #construct item
        self.number = number
        self.description = dictTexts[number]
        self.name = dictItems[number]
        self.__type = dictModType[number]
        if number in dictAction:
            self.__action = dictAction[number]
        if number in dictMods:
            self.__mod = dictMods[number]
        else:
            self.__mod = None
            #add to yielded items
        if number not in listItemsYielded:
            listItemsYielded.append(number)
            #add to inventory
            dictInventory[number] = self

    def DelItem(self):
        del dictInventory[self.number]

    def UseItem(self):
        """This method offers the item's description and then
        asks the player - if the item is 'usable' - whether the item shall be used.
        Items are only 'usable' if they do not need any other object for interaction
        except the player and the item itself."""
        textReader(self.description)
        textReader("Möchtet ihr " + self.name + " benutzen?\n")
        resp = inputCheck("Bitte eingeben: JA: '1', NEIN: '0'. ")
        if resp == 1:
            textReader(self.__action)
            if self.__type == Mod_typ.EFFONE or self.__type == Mod_typ.EFFALL:
                if self.__mod is not None:
                    invokeChangeMod(self.__mod, self.__type)
                #item uses up and is then deleted
                self.DelItem()
                textReader(self.name + " wurde verbraucht.\n")
            else:
                textReader(self.name + " kann nicht allein benutzt oder verbraucht werden.\n")
        else:
            textReader("Ja, manchmal ist es auch gut, von Taten abzusehen.\n")  

        

class Player:
    def __init__(self, name, color, mod):
        self.name = name
        self.color = color
        self.__mod = mod
        self.__maxMod = [10, 10]

    def GetMod(self):
        return self.__mod

    def ChangeMod(self, valueList):
        for i in range(0, len(self.__mod)):
            self.__mod[i] = self.__mod[i] + valueList[i]
            if self.__mod[i] > self.__maxMod[i]:
                self.__mod[i] = self.__maxMod[i]
            elif self.__mod[i] < 1:
                print("TODO: GAME OVER")

#----------------------------------------------
# General Helper functions
#----------------------------------------------
def textReader(text):
    for text in text:
            print(text, end="")
            time.sleep(.001) #later: 0.04
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
#----------------------------------------------
# Handlers
#----------------------------------------------
def actionHandler(generateFromNr):
    nrOfDigits = len(str(generateFromNr))
    if nrOfDigits == 2:
        itemUse(generateFromNr)
    elif nrOfDigits == 3:
        notReachable(currentRoom, playerAction)
    elif nrOfDigits == 4:
        itemItem(generateFromNr)
    elif nrOfDigits == 5:
        itemSpot(generateFromNr)
    else:
        print("Kein bekanntes Kommando.")
#----------------------------------------------
def itemUse(generateFromNr):
    """Generates the item connected to the spot, if any"""
    #2-digit
    if generateFromNr in dictInventory:
        dictInventory[generateFromNr].UseItem()
    else:
        print("Leider hast du diesen Gegenstand nicht im Inventar...")      
#----------------------------------------------        
def itemItem(generateFromNr):
    #4-digit
    item1 = int(generateFromNr/100)
    item2 = generateFromNr%100
    if (item1 in dictInventory) & (item2 in dictInventory):
        #only add items if both are available in inventory
        if generateFromNr in dictItems:
            Item(generateFromNr) 
            #original items deleted on combination
            dictInventory[item1].DelItem
            dictInventory[item2].DelItem
            textReader("Du erhältst " + str(generateFromNr) \
                       + ": " + dictInventory[generateFromNr].name)
        else:
            print("Das lässt sich nicht kombinieren!")
    else:
        print("Nette Idee, allerdings habt ihr die Gegenstände " + str(item1) \
              + " und " + str(item2) + " nicht beide im Inventar...")
#----------------------------------------------
def itemSpot(generateFromNr):
    item = int(generateFromNr/1000)
    spot = generateFromNr%1000
    if spot in currentRoom.spot_list:
        if item in dictInventory:
            if generateFromNr in dictSpotItems:
                #generate item
                newItemNr = dictSpotItems[generateFromNr]
                newItem = Item(newItemNr)
                #delete old item
                dictInventory[item].DelItem()
                textReader("Das war erfolgreich! Ihr erhaltet " + \
                           str(newItem.number) + \
                               ": " + newItem.name)
            else:
                #generate game progress only
                textReader(dictTexts[generateFromNr])
        else:      
            print("Ihr besitzt den angegebenen Gegenstand doch gar nicht!")
    else:
        print("Diesen Ort gibt es hier leider nicht.")
#----------------------------------------------
def invokeChangeMod(mod, modType):
    if modType == Mod_typ.EFFONE:
            currentPlayer.ChangeMod(mod)
            textReader(currentPlayer.name + ", dein Wohlbefinden ändert sich um:\n\
Motivation: " + str(mod[0]) + "\n"\
"Müdigkeit: " + str(mod[1]) + "\n")
    elif modType == Mod_typ.EFFALL:
        for element in range(1, len(listPlayers)):
            listPlayers[element].ChangeMod(mod)
            textReader(listPlayers[element].name + ", dein Wohlbefindern ändert sich um:\n\
Motivation: " + str(mod[0]) + "\n"\
"Müdigkeit: " + str(mod[1]) + "\n")
#----------------------------------------------
def notReachable(room, tgt):
    textReader("Der Raum bzw. die Aktion " + str(tgt) + " ist von hier aus\n" \
+ str(room.number) + ": " + room.name + " leider nicht erreichbar...\n")
#----------------------------------------------
def nextPlayer():
    if listPlayers[0] < (len(listPlayers) - 1):
        #next player
        listPlayers[0] = listPlayers[0] + 1
    else:
        #start again with first player
        listPlayers[0] =  1
    return listPlayers[0]
#----------------------------------------------    
#----------------------------------------------

#listPlayers Types [int currentPlayer, Player player1, Player player2, ...]
listPlayers = [1, Player("Lukas", "red", [5,10]), Player("Marie", "green", [7,6])]

#Vorgeschichte!      
#Room1: Train station Mendig, RB26, 1.5h from cologne
currentPlayer = listPlayers[listPlayers[0]]
currentRoom = Room(100)

#generate start items in inventory
Item(10)
#enter a room routine
currentRoom.onEnter()
while True:
    textReader("\n" + currentPlayer.name + " ist an der Reihe.\n")
    playerAction = inputCheck("Was wollt ihr tun? ")
    print("\n")
    if playerAction in dictRooms:
        if playerAction == currentRoom.number:
            #only show description if specifically asked
            textReader(currentRoom.description)
        elif playerAction in dictConnectedRooms[currentRoom.number]:
            #player selected a room
            currentRoom = currentRoom.room_list[playerAction]
            currentRoom.onEnter()
        else:
            notReachable(currentRoom, playerAction)    
    elif playerAction in dictSpots:
        if playerAction in currentRoom.spot_list:
            #player selected a spot
            activeSpot = currentRoom.spot_list[playerAction]
            activeSpot.action()
        else:
            notReachable(currentRoom, playerAction)  
    else:
        #player selected an item, an item-item combination, or an item-spot combination
        actionHandler(playerAction)
    currentPlayer = listPlayers[nextPlayer()]
    
    # TODO: Update inventory/stat screen
    # TODO: low/no stat left : End game/delay etc.
        
