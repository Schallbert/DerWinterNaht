#import pygame
import subprocess
from tkinter import *
#import datetime
import time

#Import data structures   
from TextData_WinterIsComing import *
from Enums_WinterIsComing import *
from ScreenManager_WinterIsComing import *

#Data structures

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

    def OnEnter(self):
        self.__spot_list = spotBuilder(self.number)
        self.__room_list = roomBuilder(self.number)
        self.__ReloadRoom()

    def __ReloadRoom(self):
        print("")
        if self.number not in listRoomsVisited:
            textReader(self.description)
        textReader("Ihr befindet euch bei " + str(self.number) + ": "\
                   + self.name + ".\n\n")
        print("Ihr seht:")
        for element in self.__spot_list.values():
            print(str(element.number) + ": " + element.name + "\n")
            time.sleep(.5)
        print("\nVon hier aus sind folgende Orte erreichbar:")
        for element in self.__room_list.values():
            if element.number in listRoomsVisited:
                #room is known
                print(str(element.number) + ": "\
                      + element.name)
            else:
                print(str(element.number) + ": ???")
            time.sleep(.5)
        listRoomsVisited.append(self.number)

    def SpotExchange(self, fromSpotId, targetSpotId):
        """This Method exchanges a spot within the list with another
        target spot needed when a spot changes its meaning throughout
        the game"""
        if targetSpotId not in self.__spot_list:
            tgtSpot = Spot(targetSpotId)
            self.__spot_list[targetSpotId] = tgtSpot
            self.__spot_list.pop(fromSpotId)
            self.__ReloadRoom()
        else:
            #don't switch als switch has already happened
            pass

    def GetSpotList(self):
        return self.__spot_list

    def GetRoomList(self):
        return self.__room_list

    def OnLeave(self):
        #not implemented (yet)
        pass
                
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

    def OnEnter(self):
        """Routines that are executed when a spot is entered,
        i.e. description, trigger spot exchange, trigger actions"""
        textReader("\nIhr untersucht: " + self.name + "\n" + self.description)
        self.__action() #perform spot action
        if self.number in dictSpotChange: 
            for element in range(0, len(dictSpotChange[self.number][0])):
                #exchange spots in room dictionary
                fromSpotId = dictSpotChange[self.number][0][element]
                tgtSpotId = dictSpotChange[self.number][1][element]
                currentRoom.SpotExchange(fromSpotId, tgtSpotId)

    def OnLeave(self):
        if self.number in dictSpotChange: #if it can be found in the keys
            for element in range(0, len(dictSpotChange[self.number][1])):
                #exchange spots back in room dictionary
                fromSpotId = dictSpotChange[self.number][1][element]
                tgtSpotId = dictSpotChange[self.number][0][element]
                currentRoom.SpotExchange(fromSpotId, tgtSpotId)
        
                
    def __action(self):
        """Interaction with the spot depending on context VIEW, GOTO, OPEN, GET or NOCHOICE
        May modify character's properties or set flags plot changes"""
        print("")
        if self.__action_id < Action_id.NOC_YES:
            textReader("Möchtet ihr " + self.name + actionDict[self.__action_id] + "\n")
            resp = inputCheck("Bitte eingeben: JA: '1', NEIN: '0'. ")
            if resp == 1:
                self.__action_id == Action_id.NOC_NO #mitigate re-enter action
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
        elif self.__action_id == Action_id.NOC_YES:
            self.__action_id == Action_id.NOC_NO #mitigate re-enter action
            if self.number in dictAction:
                textReader(dictAction[self.number])
            if self.number in dictMods:
                changeMod(dictMods[self.number])
       #else: action_id is NOC_NO and nothing happens
                    
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
        if self.__type == Mod_typ.NOTUSABLE \
           or self.__type == Mod_typ.PERMANENT:
            print("Dieser Gegenstand kann nicht ohne Kombination benutzt werden.")
        else:
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

    def GetType(self):
        return self.__type             

class Player:
    def __init__(self, name, color, mod, position):
        self.__position = position
        self.__name = name
        self.__color = color
        self.__mod = mod

    def GetName(self):
        return self.__name

    def SetPos(self, position):
        self.__position = position

    def GetPos(self):
        return self.__position

    def GetMod(self):
        return self.__mod

    def GetColor(self):
        return self.__color

    def ChangeMod(self, valueList):
        maxMod = [10, 10]
        for i in range(0, len(self.__mod)):
            self.__mod[i] = self.__mod[i] + valueList[i]
            if self.__mod[i] > maxMod[i]:
                self.__mod[i] = maxMod[i]
            elif self.__mod[i] < 1:
                #exchange motivation/tiredness 2:1
                #If that is not possible, --> minigame or --> quit game for time x
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
        hiddenObj = False
        #only list if there's a valid spot that is not hidden
        if i in dictSpots:
            for x in dictSpotChange.values():
                if i in x[1]:
                    hiddenObj = True
            #generate spots
            if hiddenObj == False:
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
    spotList = currentRoom.GetSpotList()
    if spot in spotList:
        if item in dictInventory:
            if generateFromNr in dictSpotItems:
                #generate item
                for element in range(0, len(dictSpotItems[generateFromNr])):
                    newItemNr = dictSpotItems[generateFromNr][element]
                    newItem = Item(newItemNr)
                    textReader("Das war erfolgreich! Ihr erhaltet " + \
                           str(newItem.number) + \
                               ": " + newItem.name)
                #delete old item
                if not dictInventory[item].GetType == Mod_typ.PERMANENT:
                    dictInventory[item].DelItem()
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
def nextPlayer(currentPlayerId):
    if currentPlayerId < (len(listPlayers) - 1):
        #next player
        currentPlayerId += 1
    else:
        #start again with first player
        currentPlayerId =  0
    return currentPlayerId
#----------------------------------------------    
#----------------------------------------------