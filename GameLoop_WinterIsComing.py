#!/Program Files (x86)/Python python3
from GameMechanics_WinterIsComing import *
from GameStatClass_WinterIsComing import GameStats
from Enums_WinterIsComing import GUICONSTS
import time

def playTutorial():
    mockPlayer = Player("Spieler", 'white', [7,4], 0)
    gui.textScreen.Clear()
    gui.textScreen.TitleWriteCentered("Regeln und Tutorial")
    gui.textScreen.LineWrite("\n\n")
    gui.textScreen.TypeWrite(dictTexts[7][0]) #intro page 1
    gui.textScreen.TypeWrite(GameMsg.LOADING)
    Item(98)
    Item(99)
    gui.inventoryScreen.TypeWrite(dictTexts[8]) #inventory text
    gui.statsScreen.Update([mockPlayer])
    gui.statsScreen.TypeWrite(dictTexts[9]) #player stats text
    gui.textScreen.Clear()
    gui.textScreen.TypeWrite(dictTexts[7][1]) #intro page 2
    gui.textScreen.TypeWrite(GameMsg.LOADING)
    gui.textScreen.Clear()
    gui.textScreen.TypeWrite(dictTexts[7][2]) #intro page 3
    gui.textScreen.TypeWrite(GameMsg.LOADING)   
        
def playCredits():
    gui.textScreen.Clear()
    gui.textScreen.TitleWriteCentered("Credits")
    gui.textScreen.LineWrite("\n\n\n\n")
    gui.textScreen.TypeWrite(GUICONSTS.CTRSTR + "Konzept und Idee: Lukas Preußer\n")
    gui.textScreen.TypeWrite(GUICONSTS.CTRSTR + "Spielmechanik:    Lukas Preußer\n")
    gui.textScreen.TypeWrite(GUICONSTS.CTRSTR + "Plot & Texte:     Lukas Preußer\n")
    gui.textScreen.TypeWrite(GUICONSTS.CTRSTR + "Videos:           Lukas Preußer\n")
    gui.textScreen.TypeWrite(GUICONSTS.CTRSTR + "Soundtrack:       Markus Hagen & Lukas Preußer\n")
    gui.textScreen.TypeWrite(GUICONSTS.CTRSTR + "Test-Spieler:     noch keine ;)\n")
    gui.textScreen.TypeWrite(GameMsg.LOADING)
    
def printTitleMenu():
    gui.textScreen.Clear()
    gui.textScreen.TypeWrite("\n\n\n")
    gui.textScreen.TitleWriteCentered("Der Winter naht")
    gui.textScreen.TypeWrite(GUICONSTS.CTRSTR + "      - Ein Textabenteuer -\n\n\n\n")
    gui.textScreen.TypeWrite(GUICONSTS.CTRSTR + "----------- Hauptmenü -----------\n\n")
    gui.textScreen.LineWrite(GUICONSTS.CTRSTR + "Bitte eingeben:   <Wert> <Enter>\n")
    gui.textScreen.LineWrite(GUICONSTS.CTRSTR + "Spiel fortsetzen:     0\n")
    gui.textScreen.LineWrite(GUICONSTS.CTRSTR + "Neues Spiel beginnen: 1\n")
    gui.textScreen.LineWrite(GUICONSTS.CTRSTR + "Regeln und Tutorial:  2\n")
    gui.textScreen.LineWrite(GUICONSTS.CTRSTR + "Credits:              3\n")
    gui.textScreen.LineWrite(GUICONSTS.CTRSTR + "Spiel beenden:     quit\n\n")
    resp = gui.inputScreen.GetInput()


resp = 3
while resp > 1:
    printTitleMenu()
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
            GameStats.Quit(gui)
    elif resp == 2: #tutorial
        playTutorial()
    elif resp == 3: #credits
        playCredits()
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
