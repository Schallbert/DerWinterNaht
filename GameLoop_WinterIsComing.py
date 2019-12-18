#!/Program Files (x86)/Python python3
from GameMechanics_WinterIsComing import *
from Enums_WinterIsComing import cmd_inpt
from GameStatClass_WinterIsComing import GameStats
import time
#Vorgeschichte!
#Room1: Train station Mendig, RB26, 1.5h from cologne

resp = 3
while resp > 1:
    ctrStr = " "*23
    gui.textScreen.Clear()
    gui.textScreen.TypeWrite("\n\n\n\n")
    gui.textScreen.TypeWrite(ctrStr + "-----------Hauptmenü------------\n\n")
    gui.textScreen.LineWrite(ctrStr + "Bitte eingeben:   <Wert> <Enter>\n")
    gui.textScreen.LineWrite(ctrStr + "Spiel fortsetzen:     0\n")
    gui.textScreen.LineWrite(ctrStr + "Neues Spiel beginnen: 1\n")
    gui.textScreen.LineWrite(ctrStr + "Regeln und Tutorial:  2\n")
    gui.textScreen.LineWrite(ctrStr + "Credits:              3\n")
    gui.textScreen.LineWrite(ctrStr + "Spiel beenden:     quit\n\n")
    resp = gui.inputScreen.GetInput()
    if resp == 0: #continue game
        try:
            gui.textScreen.TypeWrite(GameMsg.LOAD)
            GameStats.Load()
            gui.inventoryScreen.Update(GameStats.GetInventory())
            gui.statsScreen.Update(GameStats.GetListPlayers())
            gui.textScreen.TypeWrite(GameMsg.SUCCESS)
        except:
            gui.textScreen.TypeWrite(GameMsg.NO_SVGAME)
            NewGame()
    elif resp == 1: #new game
        gui.textScreen.TypeWrite(GameMsg.ASKOVWR)
        gui.textScreen.TypeWrite(GameMsg.ACTIONP)
        resp = gui.inputScreen.GetInput()
        if resp == 1: #ask if savegame file shall be overwritten
            NewGame()
            gui.inventoryScreen.Update(GameStats.GetInventory())
            gui.statsScreen.Update(GameStats.GetListPlayers())
        else:
            gui.textScreen.TypeWrite(GameMsg.QUIT)
            GameStats.Quit(gui.root)
    elif resp == 2: #tutorial
        mockPlayer = Player("Spieler", 'white', [7,4], 0)
        gui.textScreen.Clear()
        gui.textScreen.TypeWrite(GameMsg.INTRO)
        gui.textScreen.TypeWrite(GameMsg.LOADING)
        Item(98)
        Item(99)
        gui.inventoryScreen.TypeWrite(GameMsg.INVSCR)
        gui.statsScreen.Update([mockPlayer])
        gui.statsScreen.TypeWrite(GameMsg.STATSCR)
        gui.textScreen.Clear()
        gui.textScreen.TypeWrite(GameMsg.NUMBERS)
        gui.textScreen.TypeWrite(GameMsg.LOADING)
        gui.textScreen.Clear()
        gui.textScreen.TypeWrite(GameMsg.COMBINATIONS)
        gui.textScreen.TypeWrite(GameMsg.LOADING)   
    elif resp == 3: #credits
        gui.textScreen.TypeWrite("\n\n\n\n" + ctrStr + "Das alles hier: Lukas P. 'Schallbert'")
        gui.textScreen.TypeWrite(GameMsg.LOADING)
    else:
        gui.textScreen.TypeWrite(GameMsg.QUIT)
        GameStats.Quit(gui)

#gui preparation
GameStats.GetCurrentRoom().OnEnter()
while True:
    CheckPlayerStats()
    newRound()
    #update currentRoom if necessary and call player's interaction function
    playerAction_Selector()
    gui.textScreen.TypeWrite(GameMsg.LOADING)
    GameStats.Save()
