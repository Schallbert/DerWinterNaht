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
#listPlayers Types [int currentPlayer, Player player1, Player player2, ...]
listPlayers = [Player("Lukas", "orange", [10,8], currentRoom), \
               Player("Marie", "cyan", [7,6], currentRoom)]
currentPlayerId = 0
currentPlayer = listPlayers[currentPlayerId]
#get GUI up and running
#gui = GameGui()
#enter a room routine
currentRoom.OnEnter()
while True:
    
    #gui.textScreen.Clear() #new round
    #gui.textScreen.TypeWrite(currentPlayer.GetName() + " ist an der Reihe.\n")
    gui.statsScreen.Update(listPlayers) #only update on change?
    gui.inventoryScreen.Update(dictInventory) #only update on change?
    #gui.textScreen.TypeWrite("Was wollt ihr tun?\n")
    #playerAction = gui.inputScreen.GetInput()
    playerAction_Selector(currentRoom, currentPlayer)
    newRound(currentPlayer)
    currentPlayer = listPlayers[nextPlayer(currentPlayerId)]
    
    # TODO: Update inventory/stat screen
    # TODO: low/no stat left : End game/delay etc.
        
