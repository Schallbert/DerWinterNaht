from TextData_WinterIsComing import GameMsg
from TextData_WinterIsComing import dictTexts
from GameMechanics_WinterIsComing import RandomMod
from GameMechanics_WinterIsComing import Room
from GameMechanics_WinterIsComing import Player
from GameMechanics_WinterIsComing import Item
from GameStatClass_WinterIsComing import GameStats
from Enums_WinterIsComing import GUICONSTS


class TitleScreens:

    @classmethod
    def printTitleMenu(cls, gui):
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

    @classmethod
    def newGame(cls, gui):
        """This method initializes the game with predefined values.
            Acts like a setter for the player list."""
        startRoom = 100
        gui.audioStream.play(110)  # Main Theme

        GameStats.SetCurrentRoom(Room(startRoom))
        # Setup Player list (static Class)
        gui.textScreen.Clear()
        gui.textScreen.LineWrite("\n")
        gui.textScreen.TitleWriteCentered("Der Winter naht")
        gui.textScreen.LineWrite("\n")
        gui.textScreen.TypeWrite("Seid willkommen bei 'Der Winter naht'!\n\
Wie viele Spieler seid ihr [1-4]?")
        resp = gui.inputScreen.getNumber()
        if resp < 1:
            resp = 1
        if resp > 4:
            resp = 4
        gui.textScreen.TypeWrite("\nOk, %d Spieler.\n" % resp)
        for player in range(1, resp+1):
            gui.textScreen.Clear()
            gui.textScreen.LineWrite("\n")
            gui.textScreen.TitleWriteCentered("Der Winter naht")
            # Get player name
            gui.textScreen.TypeWrite("Spieler %d, wie lautet Dein Name? " % player)
            playerName = gui.inputScreen.getInput()
            gui.textScreen.TypeWrite(playerName)
            # Get player color
            gui.textScreen.TypeWrite(GameMsg.ASKCLR)
            gui.textScreen.ChooseColor()
            colorId = gui.inputScreen.getNumber()
            if colorId in GUICONSTS.DICTPLAYERCOLORS:
                playerColor = GUICONSTS.DICTPLAYERCOLORS[colorId]
            else:  # player didn't select a valid color
                gui.textScreen.TypeWrite(GameMsg.CLRNOTSET)
                playerColor = GUICONSTS.DICTPLAYERCOLORS[player]
            # Get player's motivation and tiredness
            gui.textScreen.TypeWrite(GameMsg.MODBEFOREGAMESTART)
            gui.textScreen.TypeWrite(GameMsg.GETMOT)
            playerMot = RandomMod.rndm_PlayerInput(gui.inputScreen.getNumber())
            gui.textScreen.TypeWrite(GameMsg.GETTIR)
            playerTir = RandomMod.rndm_PlayerInput(gui.inputScreen.getNumber())
            playerList = GameStats.GetListPlayers()
            # Modify player list
            playerList.append(Player(playerName, playerColor, [playerMot, playerTir], GameStats.GetCurrentRoom()))
            GameStats.SetListPlayers(playerList)
            gui.textScreen.Clear()

        gui.textScreen.LineWrite("\n")
        gui.textScreen.TitleWriteCentered("Der Winter naht")
        for player in GameStats.GetListPlayers():
            gui.textScreen.NameWrite(player)
            gui.textScreen.TypeWrite(", ")
        gui.textScreen.TypeWrite("\n\n\n" + dictTexts[1])
        # generate start items in inventory
        Item(10)  # first item: Smartphone
        gui.textScreen.TypeWrite(GameMsg.LOADING)

    @classmethod
    def playTutorial(cls, gui):
        mock_player = Player("Spieler", 'white', [7, 4], 0)
        gui.textScreen.Clear()
        gui.textScreen.TitleWriteCentered("Regeln und Tutorial")
        gui.textScreen.LineWrite("\n\n")
        gui.textScreen.TypeWrite(dictTexts[7][0])  # intro page 1
        gui.textScreen.TypeWrite(GameMsg.LOADING)
        Item(98)
        Item(99)
        gui.inventoryScreen.TypeWrite(dictTexts[8])  # inventory text
        gui.statsScreen.Update([mock_player])
        gui.statsScreen.TypeWrite(dictTexts[9])  # player stats text
        gui.textScreen.Clear()
        gui.textScreen.TypeWrite(dictTexts[7][1])  # intro page 2
        gui.textScreen.TypeWrite(GameMsg.LOADING)
        gui.textScreen.Clear()
        gui.textScreen.TypeWrite(dictTexts[7][2])  # intro page 3
        gui.textScreen.TypeWrite(GameMsg.LOADING)

    @classmethod
    def playCredits(cls, gui):
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
