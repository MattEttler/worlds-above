Include "config.bb"
Include "character.bb"
Include "components/rectangle.bb"
Include "entityManager.bb"

; Systems
Include "systems/rectangleSystem.bb"
Include "systems/characterSystem.bb"
Include "systems/playerSystem.bb"
Include "systems/containableSystem.bb"

; Game State
Const GAMEBOOTING = 0
Const GAMERUNNING = 1
Const GAMEOVER = 2
Global GameState% = GAMEBOOTING

Local entities%[numberOfEntities]
SetBuffer(BackBuffer())

Graphics(screenWidth, screenHeight)

Local playerControlledCharacterId = 0;

logicTimer = CreateTimer(60)

local fortress.Rectangle = New Rectangle
fortress\x = (mapSize-fortress\width)/2
fortress\y = (mapSize-fortress\height)/2
fortress\width = 10
fortress\height = 10
fortress\red = 0
fortress\green = 0
fortress\blue = 255
fortress\solid = 0

While(Not KeyHit(1))
	WaitTimer(logicTimer)
	If(GameState = GAMEBOOTING)
		BootstrapCharacters()
		BootstrapContainables()
		GameState = GAMERUNNING
		Cls()
		Text(screenWidth/2, screenHeight/2, "WELCOME TO WORLDS-BELOW.", True, True)
		Delay(1000)
	Else If(GameState = GAMEOVER)
		If(KeyHit(28))
			GameState = GAMEBOOTING
		End If 
	End If

	; Update Logic
	If(GameState = GAMERUNNING)
		UpdatePlayer()
	End If
	
	; Update Rendering
	Cls()

	; TODO: Remove non-rendering update from Rendering jobs.
	UpdateRectangles()
	UpdateCharacters(fortress)
	RenderHUD()
	
	If(GameState = GAMEOVER)
		Text(screenWidth/2, screenHeight/2, "AQUANAUT DIED. Hit <Enter> to restart.", True, True)
	End If
	Flip()
Wend
