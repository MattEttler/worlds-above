Include "config.bb"

Function UpdateRectangles()
        Cls()
        For rect.Rectangle = Each Rectangle
                xPos% = rect\x * (screenWidth/mapSize)
                yPos% = rect\y * (screenHeight/mapSize)
                drawWidth = rect\width * (screenWidth/mapSize)
                drawHeight = rect\height * (screenHeight/mapSize)
                Color(255, 250, 0)
                Rect(xPos, yPos, drawWidth, drawHeight, rect\solid)
                Color(0,0,0)
        Next
        Flip()
End Function