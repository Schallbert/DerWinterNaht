from GameMechanics_WinterIsComing import *
from Enums_WinterIsComing import cmd_inpt

# ------------------------------------
# HELPERS


#Vorgeschichte!
#Room1: Train station Mendig, RB26, 1.5h from cologne
    
gui.textScreen.TypeWrite("Möchtet Ihr euer aktuelles Spiel fortsetzen?\n")
gui.textScreen.TypeWrite(GameMsg.ACTIONP)
resp = gui.inputScreen.GetInput()
if resp == 1:
    try:
        GameStats.Load()
        print(GameStats.GetRoomsVisited())
        print(GameStats.GetItemsYielded())
    except:
        gui.textScreen.TypeWrite(GameMsg.NO_SVGAME)
        GameStats.NewGame()
else:
    GameStats.NewGame()

gui.statsScreen.Update(GameStats.GetListPlayers())
GameStats.GetCurrentRoom().OnEnter()
while True:
    CheckPlayerStats()
    newRound()
    #update currentRoom if necessary and call player's interaction function
    playerAction_Selector()
    gui.textScreen.TypeWrite(GameMsg.LOADING)
    GameStats.Save()
    
    # TODO: low/no stat left : End game/delay etc.
        
