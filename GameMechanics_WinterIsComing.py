#import pygame
import subprocess
from tkinter import *
#import datetime
import time

#Import data structures   
from TextData_WinterIsComing import *
from Enums_WinterIsComing import *
from ScreenManager_WinterIsComing import *
    
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
        """Set up of connected spots and adjacent rooms.
        Then refreshes the room's attributes. Input 'room' not used."""
        self.__spot_list = self.__spotBuilder()
        self.__room_list = self.__roomBuilder()

    def ReloadRoom(self):
        """This function re-writes the GUI with current room info, available spots
        and connected rooms. It additionally prints the room's description if
        players enter the room the first time."""
        gui.textScreen.Clear()
        if self.number not in listRoomsVisited:
            gui.textScreen.TypeWrite(self.description)
        #location info
        gui.textScreen.TypeWrite(GameMsg.YOURE_AT[0] + str(self.number) + ": "\
                   + self.name + GameMsg.YOURE_AT[1])
        #list spots
        for element in self.__spot_list.values():
            gui.textScreen.LineWrite(str(element.number) + ": " + element.name + "\n")
        #list connected rooms
        gui.textScreen.LineWrite(GameMsg.IN_REACH)
        for element in self.__room_list.values():
            if element.number in listRoomsVisited:
                #room is known
                gui.textScreen.LineWrite(str(element.number) + ": "\
                      + element.name + "\n")
            else:
                gui.textScreen.LineWrite(str(element.number) + GameMsg.UNKNOWN_ROOM)
            time.sleep(.5)
        gui.textScreen.LineWrite("\n")
        listRoomsVisited.append(self.number)
        
    def __spotBuilder(self):
        """Generates a list of spots that the roon contains
        based on room number, using spot dictionary."""
        spotObjList = {}
        #get valid spot numbers for room
        for i in range(self.number, self.number+9):
            hiddenObj = False
            #only list if there's a valid spot that is not hidden
            if i in dictSpots:
                for x in dictSpotChange.values():
                    if i in x[1]:
                        hiddenObj = True
                #generate spots
                if hiddenObj == False:
                    spotObjList[i] = Spot(i, self)
        return spotObjList
        
    def __roomBuilder(self):
        roomObjList = {}
        for i in range(0, len(dictConnectedRooms[self.number])):
            #generate adjacent rooms
            roomObjList[dictConnectedRooms[self.number][i]] = Room(dictConnectedRooms[self.number][i])
        return roomObjList  

    def SpotExchange(self, fromSpotId, targetSpotId):
        """This Method exchanges a spot within the list with another
        target spot needed when a spot changes its meaning throughout
        the game"""
        if targetSpotId not in self.__spot_list:
            tgtSpot = Spot(targetSpotId, self)
            self.__spot_list[targetSpotId] = tgtSpot
            self.__spot_list.pop(fromSpotId)
        else:
            #don't switch als switch has already happened
            pass

    def GetSpotList(self):
        return self.__spot_list

    def GetRoomList(self):
        return self.__room_list

    def OnLeave(self):
        """Not needed (just yet). Input 'room' not used."""
        #TODO: not implemented (yet)
        pass
                
class Spot:
    """A spot within a room, referred to as a 3-Digit number.
    The first two digits stand for the room in which the spot is
    and the last digit is the spot ID"""
    def __init__(self, number, room):
        self.number = number
        self.__room = room
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
        gui.textScreen.Clear()
        gui.textScreen.TypeWrite(GameMsg.EXAMINE + self.name + "\n" + self.description + "\n")
        self.__action() #perform spot action
        if self.number in dictSpotChange: 
            for element in range(0, len(dictSpotChange[self.number][0])):
                #exchange spots in room dictionary
                fromSpotId = dictSpotChange[self.number][0][element]
                tgtSpotId = dictSpotChange[self.number][1][element]
                self.__room.SpotExchange(fromSpotId, tgtSpotId)

    def OnLeave(self):
        """Checks dict if there's an action to be performed on exit of a spot"""
        if self.number in dictSpotChange: #if it can be found in the keys
            for element in range(0, len(dictSpotChange[self.number][1])):
                #exchange spots back in room dictionary
                fromSpotId = dictSpotChange[self.number][1][element]
                tgtSpotId = dictSpotChange[self.number][0][element]
                self.__room.SpotExchange(fromSpotId, tgtSpotId)
        
                
    def __action(self):
        """Interaction with the spot depending on context VIEW, GOTO, OPEN, GET or NOCHOICE
        May modify character's properties or set flags plot changes"""
        if self.__action_id < Action_id.NOC_YES: #any action the user can choose from
            gui.textScreen.TypeWrite(GameMsg.ACTIONQ + self.name + actionDict[self.__action_id] + "\n")
            gui.textScreen.TypeWrite(GameMsg.ACTIONP)
            #Ask user for 0/1 whether to further investigate
            resp = gui.inputScreen.GetInput()
            if resp == 1:
                self.__action_id == Action_id.NOC_NO #mitigate re-enter action
                if self.number in dictAction:
                    gui.textScreen.TypeWrite(dictAction[self.number])
                if self.number in dictMods:
                    invokeChangeMod(self.__mod, self.__modType)
                if self.number in dictSpotItems:
                    #create items as found in list
                    for element in range(0, len(dictSpotItems[self.number])):
                        itemId = dictSpotItems[self.number][element]
                        Item(itemId)
            else:
                if self.number in dictActionRefused:
                    gui.textScreen.TypeWrite(dictActionRefused[self.number])
                else:
                    gui.textScreen.TypeWrite(GameMsg.ACTIONE)
                if self.number in dictModsRefused:
                    changeMod(dictMods[self.number])
        elif self.__action_id == Action_id.NOC_YES:
            #player has no choice whether to further investigate :D
            self.__action_id = Action_id.NOC_NO #reset to mitigate re-enter action
            if self.number in dictAction:
                gui.textScreen.TypeWrite(dictAction[self.number])
            if self.number in dictMods:
                changeMod(dictMods[self.number])
        else: 
            #action_id is NOC_NO and nothing happens
            pass
                    
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
            gui.inventoryScreen.Update(dictInventory)

    def DelItem(self):
        del dictInventory[self.number]
        gui.inventoryScreen.Update(dictInventory)

    def UseItem(self):
        """This method offers the item's description and then
        asks the player - if the item is 'usable' - whether the item shall be used.
        Items are only 'usable' if they do not need any other object for interaction
        except the player and the item itself."""
        gui.textScreen.TypeWrite(self.description)
        if self.__type == Mod_typ.NOTUSABLE or self.__type == Mod_typ.PERMANENT:
            gui.textScreen.TypeWrite(GameMsg.MUST_COMB)
        else:
            gui.textScreen.TypeWrite(GameMsg.ACIONQ + self.name + actionDict[3]) #use?
            gui.textScreen.TypeWrite(GameMsg.ACTIONP) #y/n?
            resp = gui.inputScreen.GetInput()
            if resp == 1:
                gui.textScreen.TypeWrite(self.__action)
                if self.__type == Mod_typ.EFFONE or self.__type == Mod_typ.EFFALL:
                    if self.__mod is not None:
                        invokeChangeMod(self.__mod, self.__type)
                    #item uses up and is then deleted
                    self.DelItem()
                    gui.textScreen.TypeWrite(self.name + GameMsg.USED)
                else:
                    gui.textScreen.TypeWrite(self.name + GameMsg.CANT_USE)
            else:
                gui.textScreen.TypeWrite(GameMsg.ACTIONE)

    def GetType(self):
        return self.__type             

class ListPlayers:
    """This is a static class that does not need any instance. 
    Saves state for playerList and current player for whole game"""
    __listP = []
    __currentPlayerId = 0
    
    @classmethod
    def SetPlayers(cls, listPlayers):
        """Setter for player list"""
        cls.__listP = listPlayers
    
    @classmethod    
    def NextPlayer(cls):
        """Selects and returns the next player from the list"""
        if cls.__currentPlayerId < (len(cls.__listP) - 1):
            #next player 
            cls.__currentPlayerId += 1
        else:
            #start again with first player
            cls.__currentPlayerId =  0
            
    @classmethod    
    def GetCurrent(cls):
        return cls.__listP[cls.__currentPlayerId]
        
    @classmethod
    def GetNext(cls):
        cPlayer = cls.GetCurrent()
        cls.NextPlayer()
        retPl = cls.GetCurrent()
        while not cPlayer == cls.GetCurrent():
            #skip players to go back to currentPlayer
            cls.NextPlayer()
        return  retPl
        
    @classmethod
    def GetList(cls):
        return cls.__listP

class Player:
    def __init__(self, name, color, mod, position):
        self.__position = position
        self.__name = name
        self.__color = color
        self.__mod = mod
        self.__gameOverWarn = False

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
            elif self.__mod[i] <= 1:
                self.__mod[i] = 1
                if self.__gameOverWarn == True:
                    #player has been warned and is still unmotivated: end game!
                    gui.textScreen.TypeWrite(GameMsg.UNMOT_END)
                    quitSave()
                self.__gameOverWarn = True
            else:
                self.__gameOverWarn = False
        #show mod update
        gui.statsScreen.Update(ListPlayers.GetList())
        gui.textScreen.NameWrite(self)
        gui.textScreen.TypeWrite(GameMsg.CHMOD[0] + str(self.__mod[0]) \
                                 + GameMsg.CHMOD[1] + str(self.__mod[1]) + "\n")

#----------------------------------------------
# General Helper functions
#----------------------------------------------

def quitSave():
    gui.textScreen.LineWrite("Speichern...")
    save()
    gui.textScreen.LineWrite("Spiel wird beendet.")
    quit()

def save():
    gui.textScreen.LineWrite("IMPLEMENT SAVE!")
    gui.textScreen.LineWrite("Gespeichert!")
           
#----------------------------------------------
# Handlers
#----------------------------------------------
def actionHandler(generateFromNr, room):
    nrOfDigits = len(str(generateFromNr))
    if nrOfDigits == 2:
        itemUse(generateFromNr)
    elif nrOfDigits == 4:
        itemItem(generateFromNr)
    elif nrOfDigits == 5:
        itemSpot(generateFromNr, room)
    else:
        gui.textScreen.TypeWrite(GameMsg.UNKNOWN_CMD)
#----------------------------------------------
def itemUse(generateFromNr):
    """Generates the item connected to the spot, if any"""
    #2-digit
    if generateFromNr in dictInventory:
        dictInventory[generateFromNr].UseItem()
    else:
        gui.textScreen.TypeWrite(GameMsg.NOT_INV)      
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
            gui.textScreen.TypeWrite(GameMsg.SUCCESS_GET + str(generateFromNr) \
                       + ": " + dictInventory[generateFromNr].name + "\n")     
        else:
            gui.textScreen.TypeWrite(GameMsg.CNT_CMB)
    else:
        gui.textScreen.TypeWrite(GameMsg.NOT_INV)
#----------------------------------------------
def itemSpot(generateFromNr, room):
    #5-digit
    item = int(generateFromNr/1000)
    spot = generateFromNr%1000
    spotList = room.GetSpotList()
    if spot in spotList:
        if item in dictInventory:
            if generateFromNr in dictSpotItems:
                #generate item
                for element in range(0, len(dictSpotItems[generateFromNr])):
                    newItemNr = dictSpotItems[generateFromNr][element]
                    newItem = Item(newItemNr)
                    gui.textScreen.TypeWrite(GameMsg.SUCCESS_GET + \
                           str(newItem.number) + \
                               ": " + newItem.name + "\n")             
                #delete old item
                if not dictInventory[item].GetType() == Mod_typ.PERMANENT:
                    print(dictInventory[item].GetType())
                    dictInventory[item].DelItem()
            else:
                #generate game progress only
                if generateFromNr in dictTexts:
                    gui.textScreen.TypeWrite(dictTexts[generateFromNr])
                else:
                    gui.textScreen.TypeWrite(GameMsg.CANT_CMB)
        else:      
            gui.textScreen.TypeWrite(GameMsg.NOT_INV)
    else:
        gui.textScreen.TypeWrite(GameMsg.NOT_IN_REACH)
#----------------------------------------------
def invokeChangeMod(mod, modType):
    listPlayers = ListPlayers.GetList()
    if modType == Mod_typ.EFFONE:
            ListPlayers.GetCurrent().ChangeMod(mod)
    elif modType == Mod_typ.EFFALL:
        listP = ListPlayers.GetList()
        for element in range(1, len(listPlayers)):
            listP[element].ChangeMod(mod)
#----------------------------------------------
def notReachable(room, tgt):
    gui.textScreen.TypeWrite(str(tgt) + GameMsg.NOT_IN_REACH[0] \
+ str(room.number) + ": " + room.name + GameMsg.NOT_IN_REACH[1])
#---------------------------------------------- 
def playerAction_Selector(room):
    """This function checks the player's wish and, if valid,
    tries to match it to an existing object."""
    roomObjList = room.GetRoomList()
    spotObjList = room.GetSpotList()
    activeSpot = ListPlayers.GetCurrent().GetPos()
    plAction = gui.inputScreen.GetInput()
    gui.textScreen.TypeWrite(str(plAction) + "\n")
    if plAction == cmd_inpt.UNKNOWN:
            gui.textScreen.TypeWrite(GameMsg.NAN)
    elif plAction == cmd_inpt.QUIT:
            gui.textScreen.TypeWrite(GameMsg.SVQT)
            quitSave()
    elif plAction in dictRooms:
        #player enters a room
        if plAction == room.number:
            #only show description if specifically asked
            gui.textScreen.TypeWrite(room.description)
        elif plAction in dictConnectedRooms[room.number]:
            #players leave current spot/room
            for player in ListPlayers.GetList():
                player.GetPos().OnLeave()
            #player selected another room
            room = roomObjList[plAction]
            #players enter new room
            for player in ListPlayers.GetList():
                player.SetPos(room)
            room.OnEnter()
        else:
            notReachable(room, plAction)    
    elif plAction in dictSpots:
        #player enters a spot
        if plAction in spotObjList:
            #player selected a spot
            if not activeSpot.number == plAction:
                activeSpot.OnLeave()
            if plAction in spotObjList: #possibilty that player leaves a trigger spot, thus hiding target
                ListPlayers.GetCurrent().SetPos(spotObjList[plAction])
                ListPlayers.GetCurrent().GetPos().OnEnter()
            else:
                #fallback to room
                gui.textScreen.TypeWrite(str(plAction) \
                                         + GameMsg.NOT_IN_REACH[0] \
                                         + ListPlayers.GetCurrent().GetPos().name \
                                         + GameMsg.NOT_IN_REACH[1])
                ListPlayers.GetCurrent().SetPos(room)
                ListPlayers.GetCurrent().GetPos().OnEnter()
        else:
            notReachable(room, plAction)
    else:
        #player selected an item, an item-item combination, or an item-spot combination
        if len(str(plAction)) == 3: 
            #player selected a spot/room that is not within reach
            notReachable(room, plAction)
        else: 
            actionHandler(plAction, room)
    #returns currentRooom (might be updated in case room is changed)
    return room
        
 #----------------------------------------------  
def newRound():
     ListPlayers.NextPlayer()
     gui.textScreen.NameWrite(ListPlayers.GetCurrent())
     gui.textScreen.TypeWrite(GameMsg.TURN[0] \
                              + str(ListPlayers.GetCurrent().GetPos().number) \
                              + GameMsg.TURN[1])
#----------------------------------------------
#Data structures
#---------------------------------------------- 
dictInventory = {} #holds inventory objects sorted by number
listRoomsVisited = [] #holds room numbers
listItemsYielded = [] #holds item numbers
gui = GameGui() #constructor for GUI.