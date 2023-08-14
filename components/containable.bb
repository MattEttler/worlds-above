Type Containable
	Field rectangle.Rectangle
	Field containable_type$
End Type

Function DeleteContainable(containable.Containable)
	Delete containable\rectangle
	Delete containable
End Function

Function DeleteAllContainables()
	For containable.Containable = Each Containable
		DeleteContainable(containable)
	Next
End Function
