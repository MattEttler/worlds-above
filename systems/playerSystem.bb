Include "systems/characterSystem.bb"

Function UpdatePlayer()
    If(KeyDown(200))
        characters(playerControlledCharacterId)\rectangle\y = characters(playerControlledCharacterId)\rectangle\y - 1
    Else If(KeyDown(205))
        characters(playerControlledCharacterId)\rectangle\x = characters(playerControlledCharacterId)\rectangle\x + 1 
    Else If(KeyDown(203))
        characters(playerControlledCharacterId)\rectangle\x = characters(playerControlledCharacterId)\rectangle\x - 1 
    Else If(KeyDown(208))
        characters(playerControlledCharacterId)\rectangle\y = characters(playerControlledCharacterId)\rectangle\y + 1
    End If
End Function

Function RenderHUD()
	Color(255, 255, 255)
	Text(0, 0, "Items: " + characters(playerControlledCharacterId)\containableCount)
End Function
