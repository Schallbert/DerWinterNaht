from tkinter import *
#import datetime
import time

#Import data structures   
from TextData_WinterIsComing import *
from Enums_WinterIsComing import *
from ScreenManager_WinterIsComing import *
from GameStatClass_WinterIsComing import GameStats
    
# Game classes
#----------------------------------------------
class Room:
    """A place, room, or scene within the game.
    It has a 3-digit number, of which the first two refer to the room
    and the last digit will be 0 as it is the spot ID."""
    def __init__(self, number):
        self.number = abs(number)
        self.name = dictRooms[self.number]
        self.description = dictTexts[self.number]
        self.__spotList = [] #contains spot keys. negative=hidden
        self.__roomList = [] #contains room keys. negative=hidden
        self.__spotObjects = {} #contains spots. keys always positive.
        self.__roomObjects = {} #contains rooms. keys always positive.

    def OnEnter(self):
        """Set up of connected spots and adjacent rooms if not already defined.
        Then refreshes the room's attributes.""" 
        if not self.__spotObjects: #no spots generated for this room
            self.__spotBuilder()
        if not self.__roomList: #list is empty
            self.__roomBuilder(self.number)
        checkLooseItem(self.number)
        
    def ReloadRoom(self):
        """This function re-writes the GUI with current room info, available spots
        and connected rooms. It additionally prints the room's description if
        players enter the room the first time."""
        gui.textScreen.Clear()
        listRoomsVisited = GameStats.GetRoomsVisited()
        if self.number not in listRoomsVisited:
            gui.textScreen.TypeWrite(self.description)
            GameStats.AddRoomsVisited()
        #location info
        gui.textScreen.TypeWrite(GameMsg.YOURE_AT[0] + str(self.number) + ": "\
                   + self.name + GameMsg.YOURE_AT[1])
        #list spots
        iterator = filter(lambda id: id>0, self.__spotList)
        for spotNr in iterator:
            gui.textScreen.LineWrite(str(spotNr) + ": " + self.__spotObjects[spotNr].name + "\n")
        #list connected rooms
        gui.textScreen.LineWrite(GameMsg.IN_REACH)
        iterator = filter(lambda id: id>0, self.__roomList)
        for roomNr in iterator:
            if roomNr in listRoomsVisited:
                #room is known
                gui.textScreen.LineWrite(str(roomNr) + ": "\
                      + self.__roomObjects[roomNr].name + "\n")
            else:
                gui.textScreen.LineWrite(str(roomNr) + GameMsg.UNKNOWN_ROOM)
        gui.textScreen.LineWrite("\n")
        
    def ModifyRooms(self, connectedRoomKey):
        """Wrapper function to call internal room builder.
        Takes a key, matches with dictConnectedRooms and then 
        calls room builder if needed."""
        if connectedRoomKey in dictConnectedRooms.keys():
            __roomBuilder(connectedRoomKey)
        else:
            pass #roomNr not in connected rooms list.
            
    def ModifySpots(self, cmdId, exchangeDir):
        """This Method exchanges a spot within the list with another
        target spot needed when a spot changes its meaning throughout
        the game"""
        if cmdId in dictSpotChange.keys(): 
            for value in dictSpotChange[cmdId]:
                if exchangeDir*value < 0: #execute hide commands
                    posVal = -1*value
                    if posVal in self.__spotList: #element is reachable (positive)
                        indx = self.__spotList.index(posVal)
                        self.__spotList[indx] = value #hide element
                else: #hide added spot
                    negVal = -1*value
                    if negVal in self.__spotList:
                        indx = self.__spotList.index(negVal)
                        self.__spotList[indx] = value #show existing element
            self.__spotList.sort() #sort list by number            
    
    def __spotBuilder(self):
        """Generates all spots of the room both as objects and as lists.
        List contains information on whether the spots are currently reachable."""
        #get valid spot numbers for room
        for spotId in range(self.number+1, self.number+11): #+1/11 to check if next room is hidden as well
            negVal = -1*spotId
            if spotId in dictSpots: #spot
                self.__spotList.append(spotId)
                self.__spotObjects[spotId] = Spot(spotId, self)
            elif negVal in dictSpots: #hidden spot
                self.__spotList.append(negVal)
                self.__spotObjects[spotId] = Spot(negVal, self)
            else:
                pass #spotId not in dict.
                
    def __roomBuilder(self, connectedRoomKey):
        """Gemerates adjacent rooms both as objects and as a list.
        List contains information on whether the rooms are currently reachable."""
        if connectedRoomKey in dictConnectedRooms:
            for roomId in dictConnectedRooms[connectedRoomKey]:
                if abs(roomId) not in self.__roomObjects.keys():
                    self.__roomList.append(roomId)
                    self.__roomObjects[abs(roomId)] = Room(roomId)
        else:
            print("Warning: key " + str(connectedRoomKey) \
                  + " not found. Could not create 'connected room' list!")
        
    def CheckInReach(self, plAction, spotRoom):
        """Checks if player requested spot input is reachable.
        Player input is positive (abs) so that only reachable
        spots/rooms can be returned."""
        if plAction in self.__spotList and spotRoom == Reach.SPOT:
            return self.__spotObjects[plAction]
        elif plAction in self.__roomList and spotRoom == Reach.ROOM:
            return self.__roomObjects[plAction]
        else:
            return False #spot/room not in reach

    def OnLeave(self):
        """Not needed (just yet). Input 'room' not used."""
        #TODO: not implemented (yet)
        pass
                
class Spot:
    """A spot within a room, referred to as a 3-Digit number.
    The first two digits stand for the room in which the spot is
    and the last digit is the spot ID"""
    def __init__(self, number, room):
        self.number = abs(number)
        self.__room = room
        self.description = dictTexts[self.number]
        self.name = dictSpots[number] # as init spots may be negative...
        self.__action_id = Action_id.NOC_NO #standard action ID
        self.__mod = [0,0]
        self.__modType = Mod_typ.NOTUSABLE
        if number in dictActionType:
            self.__action_id = dictActionType[self.number]
        if number in dictMods:
            self.__mod = dictMods[self.number]
        if number in dictModType:
            self.__modType = dictModType[self.number]

    def OnEnter(self):
        """Routines that are executed when a spot is entered,
        i.e. description, trigger spot exchange, trigger actions"""
        gui.textScreen.Clear()
        gui.textScreen.TypeWrite(GameMsg.EXAMINE + self.name + "\n" + self.description + "\n")
        if self.number in dictAction:
            self.__action() #perform spot action
        checkLooseItem(self.number)
        if self.number in dictSpotChange: 
            self.__room.ModifySpots(self.number, Exchange_dir.FORWARD)

    def OnLeave(self):
        """Checks dict if there's an action to be performed on exit of a spot"""
        if self.number in dictSpotChange: #if it can be found in the keys
            listPlayers = GameStats.GetListPlayers()
            playersOnSpot = 0
            for element in listPlayers:
                if element.GetPos().number == self.number:
                    playersOnSpot += 1
            if playersOnSpot <= 1:
                self.__room.ModifySpots(self.number, Exchange_dir.REVERT)
            else:
                #as at least 1 player still is on the spot, 
                #it cannot be changed back yet.
                pass
        
                
    def __action(self):
        """Interaction with the spot depending on context VIEW, GOTO, OPEN, GET or NOCHOICE
        May modify character's properties or set flags plot changes"""
        if self.__action_id < Action_id.NOC_YES: #any action the user can choose from
            gui.textScreen.TypeWrite(GameMsg.ACTIONQ + self.name + actionDict[self.__action_id] + "\n")
            gui.textScreen.TypeWrite(GameMsg.ACTIONP)
            #Ask user for 0/1 whether to further investigate
            resp = gui.inputScreen.GetInput()
            if resp == 1:
                self.__action_id = Action_id.NOC_NO #mitigate re-enter action
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
                    invokeChangeMod(self.__mod, self.__modType)
        elif self.__action_id == Action_id.NOC_YES:
            #player has no choice whether to further investigate :D
            self.__action_id = Action_id.NOC_NO #reset to mitigate re-enter action
            if self.number in dictAction:
                gui.textScreen.TypeWrite(dictAction[self.number])
            if self.number in dictMods:
                invokeChangeMod(self.__mod, self.__modType)
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
        self.__type = Mod_typ.NOTUSABLE
        self.__mod = None
        if number in dictModType:
            self.__type = dictModType[number]
        if number in dictAction:
            self.__action = dictAction[number]
        if number in dictMods:
            self.__mod = dictMods[number]
        #add to yielded items
        gui.inventoryScreen.Update(GameStats.AddToInventory(self))

    def DelItem(self):
        """"Deletes an item by removing it from the inventory dict."""
        if self.__type == Mod_typ.PERMANENT:
            pass #item is permanent
        else:
            gui.inventoryScreen.Update(GameStats.DelFromInventory(self.number))

    def UseItem(self):
        """This method offers the item's description and then
        asks the player - if the item is 'usable' - whether the item shall be used.
        Items are only 'usable' if they do not need any other object for interaction
        except the player and the item itself."""
        gui.textScreen.TypeWrite(self.description)
        if self.__type == Mod_typ.NOTUSABLE or self.__type == Mod_typ.PERMANENT:
            gui.textScreen.TypeWrite(GameMsg.MUST_COMB)
        else:
            gui.textScreen.TypeWrite(GameMsg.ACTIONQ + self.name + actionDict[3]) #use?
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
        #show mod update
        gui.textScreen.NameWrite(self)
        gui.textScreen.TypeWrite(GameMsg.CHMOD[0] + str(valueList[0]) \
                                     + GameMsg.CHMOD[1] + str(-1*valueList[1]) + "\n")
        gui.statsScreen.Update(GameStats.GetListPlayers())
        #check for "gameover" criterium Motivation
        if self.__mod[0] <= 1: #motivation is very low
            if self.__gameOverWarn == True:
                #player has been warned and is still unmotivated: end game!
                gui.textScreen.TypeWrite(GameMsg.UNMOT_END)
                gui.textScreen.TypeWrite(GameMsg.SVQT)
                GameStats.Quit(gui.root)
            self.__gameOverWarn = True
        else:
            self.__gameOverWarn = False
        


#----------------------------------------------
# Handlers
#----------------------------------------------
def actionHandler(generateFromNr):
    """Arbitrator, deciding which handling function to be called."""
    nrOfDigits = len(str(generateFromNr))
    if nrOfDigits == 2:
        itemUse(generateFromNr)
    elif nrOfDigits == 3:
        spotRoom(generateFromNr)
    elif nrOfDigits == 4:
        itemItem(generateFromNr)
    elif nrOfDigits == 5:
        # CHEAT    CHEAT    CHEAT    CHEAT    CHEAT
        if generateFromNr == 32167: #Dev cheat to get all items in game
            print("Cheat active: Get All Items")
            inv = GameStats.GetInventory()
            for element in dictItems:
                if element not in inv:
                    Item(element)
        elif generateFromNr // 1000 == 28: #Dev cheat to get to any room in game
            print("Cheat active: Go To Any Room")
            listPlayers = GameStats.GetListPlayers()
            for player in listPlayers: #players leave current spot/currentRoom
                player.GetPos().OnLeave()
            GameStats.SetCurrentRoom(Room(generateFromNr%1000)) #player selected another room, set and update
            currentRoom = GameStats.GetCurrentRoom()
            for player in listPlayers: #players enter new currentRoom
                player.SetPos(currentRoom)
            currentRoom.OnEnter()
        # CHEAT    CHEAT    CHEAT    CHEAT    CHEAT
        else:
            itemSpot(generateFromNr)
    else:
        gui.textScreen.TypeWrite(GameMsg.UNKNOWN_CMD)
#----------------------------------------------
def itemUse(generateFromNr):
    """Generates the item connected to the spot, if any"""
    #2-digit
    dictInventory = GameStats.GetInventory()
    if generateFromNr in dictInventory:
        dictInventory[generateFromNr].UseItem()
    else:
        gui.textScreen.TypeWrite(GameMsg.NOT_INV)      
#----------------------------------------------    
def spotRoom(plAction):
    """Player has entered a 3-digit number which could be a spot/room.
    function checks for rooms, whether reachable, and if so transfers 
    players to this room, executing its OnEnter() method.
    Same goes for spots."""
    #init variables
    currentRoom = GameStats.GetCurrentRoom()
    currentPlayer = GameStats.GetCurrentPlayer()
    listPlayers = GameStats.GetListPlayers()
    activeSpot = currentPlayer.GetPos()
    spotObj = currentRoom.CheckInReach(plAction, Reach.SPOT)
    roomObj = currentRoom.CheckInReach(plAction, Reach.ROOM)
    #Logic 
    if plAction == currentRoom.number:
        gui.textScreen.TypeWrite(currentRoom.description) #only show description if specifically asked
    elif spotObj: #player enters a valid spot
        if not activeSpot.number == plAction:
            activeSpot.OnLeave()   
            if currentRoom.CheckInReach(plAction, Reach.SPOT): #check again whether targeted spot is still in list
                currentPlayer.SetPos(spotObj)
                currentPlayer.GetPos().OnEnter()
            else:
                notReachable(activeSpot, plAction)
                activeSpot.OnEnter() #fallback to current spot
    elif roomObj: #player enters a valid room
        GameStats.SetCurrentRoom(roomObj) #player selected another room, set and update
        for player in listPlayers: #players leave current spot/currentRoom
            player.GetPos().OnLeave()
            player.SetPos(roomObj)
        roomObj.OnEnter()
    else:
        #player selected a spot/currentRoom that is not within reach
        notReachable(currentRoom, plAction)
#----------------------------------------------                
def itemItem(generateFromNr):
    """Combine two items to one. The original items are
    deleted when complete."""
    #4-digit
    #init variables
    dictInventory = GameStats.GetInventory()
    item1 = int(generateFromNr/100)
    item2 = generateFromNr%100
    #Logic
    if (item1 in dictInventory) & (item2 in dictInventory):
        #only add items if both are available in inventory
        if generateFromNr in dictSpotItems:
            for element in dictSpotItems[generateFromNr]:
                Item(element)
                gui.textScreen.TypeWrite(GameMsg.SUCCESS_GET + str(element) \
                       + ": " + dictInventory[element].name + "\n")   
            #original items deleted on combination
            dictInventory[item1].DelItem()
            dictInventory[item2].DelItem()  
        else:
            gui.textScreen.TypeWrite(GameMsg.CANT_CMB)
    else:
        gui.textScreen.TypeWrite(GameMsg.NOT_INV)
#----------------------------------------------
def itemSpot(generateFromNr):
    """Item has been combined with a spot. Function checks if
    any item yield or action can be found in the corresponding dicts
    and performs the actions therein. The cases are mostly to catch
    undefined behavior."""
    #5-digit
    #init variables
    item = int(generateFromNr/1000)
    spot = generateFromNr%1000
    dictInventory = GameStats.GetInventory()
    currentRoom = GameStats.GetCurrentRoom()
    spotObj = currentRoom.CheckInReach(spot, Reach.SPOT)
    #Logic
    if spotObj:
        if item in dictInventory:
            if generateFromNr in dictSpotItems:
                #generate item
                for element in range(0, len(dictSpotItems[generateFromNr])):
                    newItemNr = dictSpotItems[generateFromNr][element]
                    newItem = Item(newItemNr)
                    gui.textScreen.TypeWrite(GameMsg.SUCCESS_GET + \
                           str(newItem.number) + \
                               ": " + newItem.name + "\n")             
                dictInventory[item].DelItem() #delete old item
            elif generateFromNr in dictAction:
                gui.textScreen.TypeWrite(dictAction[generateFromNr])
                if generateFromNr in dictSpotChange:
                    currentRoom.ModifySpots(generateFromNr, Exchange_dir.FORWARD)
                if generateFromNr in dictMods:
                    GameStats.GetCurrentPlayer().ChangeMod(dictMods[generateFromNr])
                dictInventory[item].DelItem()
            else:
                #generate game progress only
                if generateFromNr in dictTexts:
                    gui.textScreen.TypeWrite(dictTexts[generateFromNr])
                    dictInventory[item].DelItem() #delete old item
                else:
                    gui.textScreen.TypeWrite(GameMsg.CANT_CMB)
        else:      
            gui.textScreen.TypeWrite(GameMsg.NOT_INV)
    else:
        gui.textScreen.TypeWrite(GameMsg.NOT_IN_REACH)
#----------------------------------------------
def invokeChangeMod(mod, modType):
    listPlayers = GameStats.GetListPlayers()
    if modType == Mod_typ.EFFONE:
            GameStats.GetCurrentPlayer().ChangeMod(mod)
    elif modType == Mod_typ.EFFALL:
        for element in range(0, len(listPlayers)):
            listPlayers[element].ChangeMod(mod)
#----------------------------------------------
def notReachable(room, tgt):
    """Just prints to players that current room or spot is not in reach."""
    gui.textScreen.TypeWrite(str(tgt) + GameMsg.NOT_IN_REACH[0] \
+ str(room.number) + ": " + room.name + GameMsg.NOT_IN_REACH[1])
#----------------------------------------------
def checkLooseItem(triggerNumber):
    """Checks whether a spot, room or other trigger that has an
    'OnEnter()' method makes players loose items from their inventory.
    Takes the trigger's number, checks the corresponding dict and then
    deletes items listed"""
    if triggerNumber in dictItemDelete:
            listDeleteItems = dictItemDelete[triggerNumber]
            dictInventory = GameStats.GetInventory()
            for item in listDeleteItems:
                if item in dictInventory:
                    itemToDel = dictInventory[item]
                    gui.textScreen.TypeWrite(GameMsg.LOOSE + str(itemToDel.number) \
                                             + ": " + itemToDel.name + "\n")
                    itemToDel.DelItem()         
#---------------------------------------------- 
def playerAction_Selector():
    """This function checks the player's wish and, if valid,
    tries to match it to an existing object."""
    plAction = gui.inputScreen.GetInput()
    gui.textScreen.TypeWrite(str(plAction) + "\n")
    if plAction == cmd_inpt.UNKNOWN:
        #unknown command
        gui.textScreen.TypeWrite(GameMsg.NAN)
    elif plAction == cmd_inpt.QUIT:
        #player wants to quit
        gui.textScreen.TypeWrite(GameMsg.SVQT)
        GameStats.Quit(gui.root)
    else: 
        actionHandler(plAction)

def CheckPlayerStats():
    """Checks tiredness and motivation of current player. If the player is
    very tired, this will affect his/her motivation. When the player's motivation
    is extremely low, the game offers to share motivation between players, while 1
    point is going to be lost. Should this not be successful, game will quit."""
    currPl = GameStats.GetCurrentPlayer()
    currMod = currPl.GetMod()
    if currMod[0] == 1:#low mod is motivation
        if len(GameStats.GetListPlayers()) == 1:
            #just one player, sharing not possible
            gui.textScreen.TypeWrite(GameMsg.UNMOT[0]) #Pause?
        else:
            nextPl = GameStats.GetNextPlayer()
            gui.textScreen.NameWrite(currPl)
            gui.textScreen.TypeWrite(GameMsg.UNMOT[0]) #Pause?
            gui.textScreen.NameWrite(nextPl)
            gui.textScreen.TypeWrite(GameMsg.UNMOT[1])
            gui.textScreen.NameWrite(currPl)
            gui.textScreen.TypeWrite(GameMsg.UNMOT[2])
            gui.textScreen.NameWrite(currPl)
            gui.textScreen.TypeWrite(GameMsg.UNMOT[3] + GameMsg.ACTIONP) #Share Mot?
            resp = gui.inputScreen.GetInput()
            if resp == 1:
                # shares motivation with UNMOT player.
                nextPlMot = int(nextPl.GetMod()[0]/2)
                nextPl.ChangeMod([-nextPlMot, 0])
                currPl.ChangeMod([nextPlMot-1, 0])
            else:
                pass
    elif currMod[1] == 1: #low mod is tiredness
        gui.textScreen.NameWrite(currPl)
        gui.textScreen.TypeWrite(GameMsg.TIRED)
        currPl.ChangeMod([-1, 0]) #reduce motivation by 1 each round
    else:
        pass
 #----------------------------------------------  
def newRound():
    GameStats.GetCurrentRoom().ReloadRoom()
    GameStats.NextPlayer()
    currentPlayer = GameStats.GetCurrentPlayer()
    gui.textScreen.NameWrite(currentPlayer)
    gui.textScreen.TypeWrite(GameMsg.TURN[0] \
                              + str(currentPlayer.GetPos().number) \
                              + GameMsg.TURN[1])
#-------------------------------------------- 
def NewGame():
        """This method initializes the game with predefined values.
        Acts like a setter for the player list."""
        GameStats.SetCurrentRoom(Room(100))
        #generate start items in inventory
        Item(10)
        #Setup Player list (static Class)
        GameStats.SetListPlayers([Player("Lukas", "orange", [8,7], GameStats.GetCurrentRoom()), \
                                  Player("Marie", "cyan", [6,9], GameStats.GetCurrentRoom())]) 

gui = GameGui() #constructor for GUI.