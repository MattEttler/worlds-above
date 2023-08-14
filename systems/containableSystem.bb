Include "config.bb"
Include "components/containable.bb"

Const maxContainables = 10

Function BootstrapContainables()
	DeleteAllContainables()
	For i = 0 To maxContainables
		containable.Containable = New Containable
		containable\rectangle = New Rectangle
		containable\rectangle\x = Rand(0, mapSize)
		containable\rectangle\y = Rand(0, mapSize)
		containable\rectangle\width = 1
		containable\rectangle\height = 1
		containable\rectangle\red = 255
		containable\rectangle\green = 0
		containable\rectangle\blue = 0
		containable\rectangle\solid = 0
	Next
End Function

