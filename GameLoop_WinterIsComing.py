from GameMechanics_WinterIsComing import *
from Enums_WinterIsComing import cmd_inpt
from GameStatClass_WinterIsComing import GameStats

#Vorgeschichte!
#Room1: Train station Mendig, RB26, 1.5h from cologne
    
gui.textScreen.TypeWrite(GameMsg.ASKCONT) #continue game?
gui.textScreen.TypeWrite(GameMsg.ACTIONP)
resp = gui.inputScreen.GetInput()
if resp == 1:
    try:
        gui.textScreen.TypeWrite(GameMsg.LOAD)
        GameStats.Load()
        gui.inventoryScreen.Update(GameStats.GetInventory())
        gui.statsScreen.Update(GameStats.GetListPlayers())
        gui.textScreen.TypeWrite(GameMsg.SUCCESS)
    except:
        gui.textScreen.TypeWrite(GameMsg.NO_SVGAME)
        NewGame()
else:
    #ask if savegame file shall be overwritten
    gui.textScreen.TypeWrite(GameMsg.ASKOVWR)
    gui.textScreen.TypeWrite(GameMsg.ACTIONP)
    resp = gui.inputScreen.GetInput()
    if resp == 1: 
        NewGame()
    else:
        GameStats.Quit(gui.root)

#gui preparation
gui.inventoryScreen.Update(GameStats.GetInventory())
gui.statsScreen.Update(GameStats.GetListPlayers())
GameStats.GetCurrentRoom().OnEnter()
while True:
    CheckPlayerStats()
    newRound()
    #update currentRoom if necessary and call player's interaction function
    playerAction_Selector()
    gui.textScreen.TypeWrite(GameMsg.LOADING)
    GameStats.Save()
