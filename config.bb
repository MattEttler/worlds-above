Const mapSize = 75
Const screenWidth = 800
Const screenHeight = 600

; Through testing Blitz3D I have found that creating an array with the max int value crashes the program.
; Through experimentation I have found that 268435455 is a safe capacity (at least on my 64bit machine) but the true upper limit is likely higher. 
Const numberOfEntities = 268435455 
If(numberOfEntities > 268435455)
    DebugLog("WARNING: This program has not been tested with an entity capacity greater than 268435455. You may experience instability.")
End If 

Const numberOfCharacters = 10
If(numberOfCharacters > numberOfEntities)
    DebugLog("ERROR: you may not configure deep-sea to have more of an entity type (character) than there are allowed entities.")
    Stop()
    End
End If

Const numberOfBlueprints = 100