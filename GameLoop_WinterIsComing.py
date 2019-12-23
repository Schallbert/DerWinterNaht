#!/Program Files (x86)/Python python3
from StartPage_WinterIsComing import TitleScreens
from GameMechanics_WinterIsComing import *
from GameStatClass_WinterIsComing import GameStats


def main():
    resp = 3
    while resp > 1:
        TitleScreens.printTitleMenu(gui)
        resp = gui.inputScreen.getNumber()
        if resp == 0:  # continue game
            try:
                gui.textScreen.TypeWrite(GameMsg.LOAD)
                timeDiff = GameStats.Load()
                gui.inventoryScreen.Update(GameStats.GetInventory())
                gui.statsScreen.Update(GameStats.GetListPlayers())
                gui.textScreen.TypeWrite(GameMsg.SUCCESS)
                motBuff = RandomMod.rndm_BufRestart(timeDiff)
                invokeChangeMod([motBuff, 0], MOD.EFFALL)
            except:
                gui.textScreen.TypeWrite(GameMsg.NO_SVGAME)
                TitleScreens.newGame(gui)
        elif resp == 1:  # new game
            gui.textScreen.TypeWrite(GameMsg.ASKOVWR)
            gui.textScreen.TypeWrite(GameMsg.ACTIONP)
            resp = gui.inputScreen.getNumber()
            if resp == 1:  # ask if savegame file shall be overwritten
                TitleScreens.newGame(gui)
                gui.inventoryScreen.Update(GameStats.GetInventory())
                gui.statsScreen.Update(GameStats.GetListPlayers())
            else:
                gui.textScreen.TypeWrite(GameMsg.NOTOVWR)
                resp = 3  # to automatically resume game.
        elif resp == 2:  # tutorial
            TitleScreens.playTutorial(gui)
        elif resp == 3:  # credits
            TitleScreens.playCredits(gui)
        else:
            gui.textScreen.TypeWrite(GameMsg.QUIT)
            GameStats.Quit(gui)

    # gui preparation
    GameStats.GetCurrentRoom().OnEnter()
    while True:
        CheckPlayerStats()
        newRound()
        # update currentRoom if necessary and call player's interaction function
        playerAction_Selector()
        gui.textScreen.TypeWrite(GameMsg.LOADING)
        GameStats.Save()


if __name__ == "__main__":
    main()
