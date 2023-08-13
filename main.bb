Include "config.bb"
Include "character.bb"
Include "components/rectangle.bb"
Include "entityManager.bb"

; Systems
Include "systems/rectangleSystem.bb"

Local entities.Character[numberOfEntities]
SetBuffer(BackBuffer())

Graphics(screenWidth, screenHeight)

Text(0, 0, "Welcome to Deep-Sea!")

Local characters.Character[numberOfCharacters]

For i=0 To numberOfCharacters-1
    character.Character = New Character
    character\health = 100
    character\x = Rand(0, 100)
    character\y = Rand(0, 100)
    character\boundingBox = New BoundingBox
    character\boundingBox\height = 1
    character\boundingBox\width = 1
    character\rectangle = New Rectangle
    character\rectangle\height = character\boundingBox\height
    character\rectangle\width = character\boundingBox\width
    character\rectangle\x = character\x
    character\rectangle\y = character\y
    character\rectangle\solid = 1
    characters[i] = character
Next

While Not KeyHit(1)
    Cls()
    UpdateRectangles()
    ; Draw Underwater Fortress
    fortressHeight = 80
    fortressWidth = 80
    Color(0, 0, 255)
    Rect((screenWidth-fortressWidth)/2,(screenHeight-fortressHeight)/2,fortressWidth,fortressHeight,0)
    Color(255, 255, 255)
    For i=0 To numberOfCharacters-1
        character = characters[i]
    Next
    Flip()
Wend