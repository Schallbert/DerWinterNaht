from GameMechanics_WinterIsComing import *
from Enums_WinterIsComing import cmd_inpt

# ------------------------------------
# HELPERS

def checkStats():
    """Checks tiredness and motivation of current player. If the player is
    very tired, this will affect his/her motivation. When the player's motivation
    is extremely low, the game offers to share motivation between players, while 1
    point is going to be lost. Should this not be successful, game will quit."""
    currPl = ListPlayers.GetCurrent()
    currMod = currPl.GetMod()
    if currMod[0] == 1:#low mod is motivation
        if len(ListPlayers.GetList()) == 1:
            #just one player, sharing not possible
            gui.textScreen.TypeWrite(GameMsg.UNMOT[0]) #Pause?
        else:
            nextPl = ListPlayers.GetNext()
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

#Vorgeschichte!
#Room1: Train station Mendig, RB26, 1.5h from cologne
    
gui.textScreen.TypeWrite("Möchtet Ihr euer aktuelles Spiel fortsetzen?\n")
gui.textScreen.TypeWrite(GameMsg.ACTIONP)
resp = gui.inputScreen.GetInput()
if resp == 1:
    try:
        load()
    except:
        gui.textScreen.TypeWrite(GameMsg.NO_SVGAME)
        newGame()
else:
    newGame()

gui.inventoryScreen.Update(dictInventory)
gui.statsScreen.Update(ListPlayers.GetList())

currentRoom.OnEnter()
while True:
    checkStats()
    currentRoom.ReloadRoom()
    newRound()
    #update currentRoom if necessary and call player's interaction function
    playerAction_Selector()
    gui.textScreen.TypeWrite(GameMsg.LOADING)
    save()
    
    # TODO: low/no stat left : End game/delay etc.
        
