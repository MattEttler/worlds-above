Include "components/rectangle.bb" 
Include "boundingBox.bb"

Type Character
Field health%, maxHealth%
Field containableCount%
Field x%
Field y%
Field rectangle.Rectangle 
Field boundingBox.BoundingBox
End Type

Function DeleteCharacter(character.Character)
	Delete character\rectangle
	Delete character\boundingBox
	Delete character
End Function

Function DeleteAllCharacters()
	For character.Character = Each Character
		DeleteCharacter(character)
	Next
End Function
