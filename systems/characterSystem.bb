Include "config.bb"
Include "components/rectangle.bb"
Include "character.bb"

Dim characters.Character(numberOfEntities)

Function BootstrapCharacters()
	For i=0 To numberOfCharacters-1
	character.Character = New Character
	character\health = 100
	character\maxHealth = 100
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
	character\rectangle\red = 0
	character\rectangle\green = 255
	character\rectangle\blue = 0
	characters(i) = character
	Next

	; designate the first character as our character.
	characters(playerControlledCharacterId)\rectangle\x = 40
	characters(playerControlledCharacterId)\rectangle\y = 40
	characters(playerControlledCharacterId)\rectangle\red = 0
	characters(playerControlledCharacterId)\rectangle\green = 0
	characters(playerControlledCharacterId)\rectangle\blue = 255
	End Function

Function UpdateCharacters(fortress.Rectangle)
	For character.Character = Each Character
			If(character\health > 0) and (Not RectsOverlap(fortress\x, fortress\y, fortress\width, fortress\height, character\rectangle\x, character\rectangle\y, character\rectangle\width, character\rectangle\height))
				character\health = character\health -1
			Else If character\health < character\maxHealth
				character\health = character\health +1
			End If
		character\rectangle\red = (255 / character\maxHealth) * (character\maxHealth - character\health)

	Next
End Function
