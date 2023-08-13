Include "config.bb"
Include "character.bb"
Include "components/rectangle.bb"
Include "entityManager.bb"

; Systems
Include "systems/rectangleSystem.bb"
Include "systems/characterSystem.bb"
Include "systems/playerSystem.bb"

Local entities%[numberOfEntities]
SetBuffer(BackBuffer())

Graphics(screenWidth, screenHeight)

Text(0, 0, "Welcome to Deep-Sea!")

BootstrapCharacters()
Local playerControlledCharacterId = 0;

logicTimer = CreateTimer(30)

local fortress.Rectangle = New Rectangle
fortress\width = 10
fortress\height = 10
fortress\x = (mapSize-fortress\width)/2
fortress\y = (mapSize-fortress\height)/2
fortress\red = 0
fortress\green = 0
fortress\ blue = 255
fortress\solid = 0

While Not KeyHit(1)
	; Update Logic
	WaitTimer(logicTimer)
	UpdatePlayer()


	; Update Rendering
	Cls()

	UpdateRectangles()
	UpdateCharacters(fortress)
	
	Flip()
Wend
