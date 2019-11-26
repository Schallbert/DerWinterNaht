import pickle
import sys

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
        #tk.destroy() to destroy the gui
        guiRoot.destroy()
        sys.exit
        
    @classmethod
    def Save(cls):
        with open('savegame.dat', 'wb') as svGame:
             pickle.dump([cls.__listP \
                         , cls.__dictInventory \
                         , cls.__listRoomsVisited \
                         , cls.__listItemsYielded \
                         , cls.__currentRoom], svGame, protocol=2)
    
    @classmethod
    def Load(cls):
        with open('savegame.dat', 'rb') as svGame:
            cls.__listP \
            , cls.__dictInventory \
            , cls.__listRoomsVisited \
            , cls.__listItemsYielded \
            , cls.__currentRoom \
            = pickle.load(svGame)
   
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
            print("Error: No current room!")
            cls.Quit()
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
