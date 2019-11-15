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
ListPlayers.SetPlayers([Player("Lukas", "orange", [2,2], currentRoom), \
                        Player("Marie", "cyan", [7,4], currentRoom)])

gui.inventoryScreen.Update(dictInventory)
gui.statsScreen.Update(ListPlayers.GetList())

currentRoom.OnEnter()
while True:
    currPl = ListPlayers.GetCurrent()
    currMod = currPl.GetMod()
    if currMod[0] == 1: #low mod is motivation
        nextPl = ListPlayers.GetNext()
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
    currentRoom.ReloadRoom()
    newRound()
    #update currentRoom if necessary and call player's interaction function
    currentRoom = playerAction_Selector(currentRoom)
    gui.textScreen.TypeWrite(GameMsg.LOADING)
    
    # TODO: low/no stat left : End game/delay etc.
        
