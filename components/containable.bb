Type Containable
	Field rectangle.Rectangle
	Field containable_type$
End Type

Function DestroyContainable(containable.Containable)
	Delete containable\rectangle
	Delete containable
End Function
