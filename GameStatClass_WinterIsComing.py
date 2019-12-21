#import modules
import pickle #for savegame
import sys
import datetime #for savegame timestamp

class GameStats:
    """This is a static class that does not need any instance. 
    Saves state for players, inventory, rooms, items player for the whole game"""
    __listP = []
    __currentPlayerId = 0
    __currentRoom = None #holds the current room
    __dictInventory = {} #holds inventory objects sorted by number
    __listRoomsVisited = [] #holds room numbers
    __listItemsYielded = [] #holds item numbers
    #----------------------------------------------
    # Gameplay related methods
    #----------------------------------------------
    @classmethod
    def Quit(cls, guiRoot):
        try:
            guiRoot.audioStream.end() #if existing, end audio stream (experimental)
        except:
            pass
        guiRoot.quit() #First end the gui's bindings
        guiRoot.destroy() #Then close gui
        sys.exit() #finally, exit program.
        
    @classmethod
    def Save(cls):
        saveTime = datetime.datetime.now()
        with open('savegame.dat', 'wb') as svGame:
             pickle.dump([cls.__listP \
                         , cls.__dictInventory \
                         , cls.__listRoomsVisited \
                         , cls.__listItemsYielded \
                         , cls.__currentRoom \
                         , saveTime], svGame, protocol=2)
    
    @classmethod
    def Load(cls):
        loadTime = datetime.datetime.now()
        with open('savegame.dat', 'rb') as svGame:
            cls.__listP \
            , cls.__dictInventory \
            , cls.__listRoomsVisited \
            , cls.__listItemsYielded \
            , cls.__currentRoom \
            , saveTime \
            = pickle.load(svGame)
        return (loadTime - saveTime) #time difference between loading and saving
   
    #----------------------------------------------
    # Player related methods
    #----------------------------------------------    
    @classmethod    
    def NextPlayer(cls):
        """Selects and returns the next player from the list"""
        if cls.__currentPlayerId < (len(cls.__listP)-1):
            #next player 
            cls.__currentPlayerId += 1
        else:
            #start again with first player
            cls.__currentPlayerId =  0
            
    @classmethod    
    def GetCurrentPlayer(cls):
        return cls.__listP[cls.__currentPlayerId]
        
    @classmethod
    def GetNextPlayer(cls):
        cPlayer = cls.GetCurrentPlayer()
        cls.NextPlayer()
        retPl = cls.GetCurrentPlayer()
        while not cPlayer == cls.GetCurrentPlayer():
            #skip players to go back to currentPlayer
            cls.NextPlayer()
        return  retPl
        
    @classmethod
    def GetListPlayers(cls):
        return cls.__listP
        
    @classmethod
    def SetListPlayers(cls, listP):
        cls.__listP = listP
    #----------------------------------------------
    # Room and place related methods
    #----------------------------------------------
    @classmethod
    def GetCurrentRoom(cls):
        if cls.__currentRoom == None:
            raise Exception("No room object available. Ending game.")
        else:
            return cls.__currentRoom
               
    @classmethod
    def SetCurrentRoom(cls, room):
        cls.__currentRoom = room
            
    @classmethod 
    def GetRoomsVisited(cls):
        return cls.__listRoomsVisited
        
    @classmethod
    def AddRoomsVisited(cls):
        cls.__listRoomsVisited.append(cls.__currentRoom.number)
    #----------------------------------------------
    # Item and inventory related methods
    #----------------------------------------------
    @classmethod
    def AddToInventory(cls, item):
        if item.number not in cls.__listItemsYielded:
            cls.__listItemsYielded.append(item.number)
            #add to inventory
            cls.__dictInventory[item.number] = item
        return cls.__dictInventory
        
    @classmethod
    def GetInventory(cls):
        return cls.__dictInventory
            
    @classmethod
    def GetItemsYielded(cls):
        return cls.__listItemsYielded
    
    @classmethod
    def DelFromInventory(cls, itemNumber):
        del cls.__dictInventory[itemNumber]
        return cls.__dictInventory
