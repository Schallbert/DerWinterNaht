from GameMechanics_WinterIsComing import *
from Enums_WinterIsComing import cmd_inpt

# ------------------------------------
# HELPERS

def quitSave():
    print("Saving...")
    save()
    print("Killing game...")
    quit()

def save():
    print("IMPLEMENT SAVE!")
    print("Saved!")

#Vorgeschichte!      
#Room1: Train station Mendig, RB26, 1.5h from cologne
currentRoom = Room(100)
#generate start items in inventory
Item(10)

#Setup Player list (static Class)
ListPlayers.SetPlayers([Player("Lukas", "orange", [10,8], currentRoom), \
                        Player("Marie", "cyan", [7,6], currentRoom)])

gui.inventoryScreen.Update(dictInventory)
gui.statsScreen.Update(ListPlayers.GetList())

currentRoom.OnEnter()
while True:
    currentRoom.ReloadRoom()
    newRound()
    #update currentRoom if necessary and call player's interaction function
    currentRoom = playerAction_Selector(currentRoom)
    gui.textScreen.TypeWrite("______________________________________________________________________")
    
    # TODO: low/no stat left : End game/delay etc.
        
