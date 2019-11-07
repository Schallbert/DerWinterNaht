from GameMechanics_WinterIsComing import *

#Vorgeschichte!      
#Room1: Train station Mendig, RB26, 1.5h from cologne
currentRoom = Room(100)
#generate start items in inventory
Item(10)
#listPlayers Types [int currentPlayer, Player player1, Player player2, ...]
listPlayers = [Player("Lukas", "blue", [10,8], currentRoom), \
               Player("Marie", "cyan", [7,6], currentRoom)]
currentPlayerId = 0
currentPlayer = listPlayers[currentPlayerId]
#get GUI up and running
gui = GameGui()
#enter a room routine
currentRoom.OnEnter()
while True:
    gui.textScreen.Clear()
    gui.textScreen.TypeWrite("\n" + currentPlayer.GetName() + " ist an der Reihe.\n")
    gui.statsScreen.Update(listPlayers)
    gui.inventoryScreen.Update(dictInventory)
    roomObjList = currentRoom.GetRoomList()
    spotObjList = currentRoom.GetSpotList()
    activeSpot = currentPlayer.GetPos()
    playerAction = inputCheck("Was wollt ihr tun?\n ")
    if playerAction in dictRooms:
        #player enters a room
        if playerAction == currentRoom.number:
            #only show description if specifically asked
            textReader(currentRoom.description)
        elif playerAction in dictConnectedRooms[currentRoom.number]:
            #players leave current spot/room
            for player in listPlayers:
                player.GetPos().OnLeave()
            #player selected another room
            currentRoom = roomObjList[playerAction]
            #players enter new room
            for player in listPlayers:
                player.SetPos(currentRoom)
            currentRoom.OnEnter()
        else:
            notReachable(currentRoom, playerAction)    
    elif playerAction in dictSpots:
        #player enters a spot
        if playerAction in spotObjList:
            #player selected a spot
            if not activeSpot.number == playerAction:
                activeSpot.OnLeave()
            currentPlayer.SetPos(spotObjList[playerAction])
            currentPlayer.GetPos().OnEnter()
        else:
            notReachable(currentRoom, playerAction)  
    else:
        #player selected an item, an item-item combination, or an item-spot combination
        actionHandler(playerAction)
    currentPlayer = listPlayers[nextPlayer(currentPlayerId)]
    
    # TODO: Update inventory/stat screen
    # TODO: low/no stat left : End game/delay etc.
        
