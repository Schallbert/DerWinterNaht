from GameMechanics_WinterIsComing import *

#Vorgeschichte!      
#Room1: Train station Mendig, RB26, 1.5h from cologne
currentRoom = Room(100)
#generate start items in inventory
Item(10)
#listPlayers Types [int currentPlayer, Player player1, Player player2, ...]
listPlayers = [Player("Lukas", "red", [5,10], currentRoom), \
               Player("Marie", "green", [7,6], currentRoom)]
currentPlayerId = 0
currentPlayer = listPlayers[currentPlayerId]
#enter a room routine
currentRoom.OnEnter()
while True:
    textReader("\n" + currentPlayer.GetName() + " ist an der Reihe.\n")
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
        
