#pumpkinCarving.py
#carve a jack o'lantern
#douglas mckenney

from graphics import *

def groupUndraw(objectList):
    for item in objectList:
        item.undraw()

def main():
    win = GraphWin("Carve a Jack O'Lantern!", 500, 450)

    #background setup
    win.setBackground("black")
    ground = Rectangle(Point(0,300), Point(500,450))
    ground.setFill("dark green")
    ground.draw(win)
    title = Text(Point(250, 66), "It's pumpkin carving time!")
    title.setTextColor("orange")
    title.setFace("times roman")
    title.setStyle("italic")
    title.setSize(29)
    title.draw(win)

    #pumpkin setup
    pumpkin = Oval(Point(100, 175), Point(400, 400))
    pumpkin.setFill("orange red")
    pumpkin.draw(win)
    lines1 = Oval(Point(125, 175), Point(375, 400))
    lines1.setFill("orange red")
    lines1.draw(win)
    #lines2 = Oval(Point(150, 175), Point(350, 400))
    #lines2.setFill("orange red")
    #lines2.draw(win)
    lines3 = Oval(Point(175, 175), Point(325, 400))
    lines3.setFill("orange red")
    lines3.draw(win)
    #lines4 = Oval(Point(200, 175), Point(300, 400))
    #lines4.setFill("orange red")
    #lines4.draw(win)
    lines5 = Oval(Point(225, 175), Point(275, 400))
    lines5.setFill("orange red")
    lines5.draw(win)
    stem = Polygon(Point(218, 178), Point(253, 201), Point(295, 180), Point(325, 140), Point(277, 123))
    stem.setFill("dark green")
    stem.draw(win)


    #text setup
    text = Text(Point(250, 425), "click on three points to draw the left eye")
    text.setTextColor("orange")
    text.setFace("courier")
    text.draw(win)

    #drawing left eye
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    leftEye = Polygon(p1, p2, p3)
    leftEye.setFill("black")
    leftEye.draw(win)

    text.setText("click on three points to draw the right eye")

    #drawing right eye
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    rightEye = Polygon(p1, p2, p3)
    rightEye.setFill("black")
    rightEye.draw(win)

    text.setText("click on three points to draw the nose")

    #drawing nose
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    nose = Polygon(p1, p2, p3)
    nose.setFill("black")
    nose.draw(win)

    text.setText("click on four points to draw the mouth")

    #drawing mouth
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    p4 = win.getMouse()
    p4.draw(win)

    mouth = Polygon(p1, p2, p3, p4)
    mouth.setFill("black")
    mouth.draw(win)

    text.undraw()
    title.setText("Hey, thanks for carving me!")

    #adding candle
    time.sleep(2)
    candle1 = Polygon(Point(41,325), Point(66,325), Point(70,385), Point(48,385))
    candle1.setFill("white")
    candle1.setOutline("white")
    candle1.draw(win)
    candle2 = Polygon(Point(41,325), Point(66,325), Point(56,315))
    candle2.setFill("white")
    candle2.setOutline("white")
    candle2.draw(win)
    wick1 = Line(Point(54, 319), Point(49,314))
    wick1.draw(win)
    wick2 = Line(Point(43,313), Point(49,314))
    wick2.draw(win)
    wick3 = Line(Point(43,313), Point(39,314))
    wick3.draw(win)
    wick4 = Line(Point(35, 315), Point(39,314))
    wick4.draw(win)
    match = Polygon(Point(15,368), Point(21,397), Point(24,397), Point(18,366))
    match.setFill("chocolate")
    match.setOutline("chocolate")
    match.draw(win)
    matchHead = Circle(Point(16,363), 4)
    matchHead.setFill("red")
    matchHead.setOutline("red")
    matchHead.draw(win)
    text.setText("click to put the candle inside and light it")
    text.draw(win)
    candleList = [candle1, candle2, wick1, wick2, wick3, wick4]
    matchList = [match, matchHead]

    text.setText("click to light a candle inside")

    #lighting the candle
    win.getMouse()
    leftEye.setFill("yellow")
    rightEye.setFill("yellow")
    nose.setFill("yellow")
    mouth.setFill("yellow")
    title.setText("AAAA, it burns!")
    text.undraw()
    groupUndraw(candleList)
    groupUndraw(matchList)

    #close window
    time.sleep(2.5)
    title.setText("Just kidding, ha ha!")
    time.sleep(1.5)
    title.setText("Thanks for the face!")
    time.sleep(2)
    text.setText("Click anywhere to quit.")
    text.draw(win)
    win.getMouse()
    win.close()
    

main()
