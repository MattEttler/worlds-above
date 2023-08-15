Include "config.bb"
Include "components/rectangle.bb"

Function UpdateRectangles()
        For rect.Rectangle = Each Rectangle
                xPos% = rect\x * (screenWidth/mapSize)
                yPos% = rect\y * (screenHeight/mapSize)
                drawWidth = rect\width * (screenWidth/mapSize)
                drawHeight = rect\height * (screenHeight/mapSize)
                Color(rect\red, rect\green, rect\blue)
                Rect(xPos, yPos, drawWidth, drawHeight, rect\solid)
                Color(0,0,0)
        Next
End Function