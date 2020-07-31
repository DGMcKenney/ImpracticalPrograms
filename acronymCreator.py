#acronymCreator.py
#creates an acronym of any phrase
#douglas mckenney


from graphics import *

#to draw more than one object at a time
def groupDraw(objectList, window):
    for item in objectList:
        item.draw(window)

#to undraw more than one object at a time
def groupUndraw(objectList):
    for item in objectList:
        item.undraw()

#to "process" information
def beepBoop(window):
    window.setBackground("black")
    beep = Text(Point(200,200), "*beep*boop*beep*")
    beep.setSize(30)
    beep.setFill("yellow")
    cir1 = Circle(Point(75,75), 30)
    cir1.setFill("red")
    cir2 = Circle(Point(325, 325), 30)
    cir2.setFill("red")
    cir3 = Circle(Point(75, 325), 30)
    cir3.setFill("blue")
    cir4 = Circle(Point(325, 75), 30)
    cir4.setFill("blue")
    display = [beep, cir1, cir2, cir3, cir4]
    groupDraw(display, window)
    time.sleep(.4)
    cir1.move(250, 0)
    cir2.move(-250, 0)
    cir3.move(250, 0)
    cir4.move(-250, 0)
    time.sleep(.4)
    cir1.move(-250, 0)
    cir2.move(250, 0)
    cir3.move(-250, 0)
    cir4.move(250, 0)
    time.sleep(.4)
    cir1.move(250, 0)
    cir2.move(-250, 0)
    cir3.move(250, 0)
    cir4.move(-250, 0)
    time.sleep(.4)
    cir1.move(-250, 0)
    cir2.move(250, 0)
    cir3.move(-250, 0)
    cir4.move(250, 0)

    time.sleep(.4)
    groupUndraw(display)
    window.setBackground("white")


#to create GUI
def createGUI():
    win = GraphWin("Acronym Creator 5000",400,400)
    win.setBackground("white")

    return win

#to set up interface
def interface(window):
    text = Text(Point(200, 100), "Please input phrase to be \nconverted to acronym: ")
    text.setSize(20)
    button = Text(Point(200,300),"Convert It")
    button.setSize(15)
    buttonEdge = Rectangle(Point(100, 250), Point(300, 350))
    interface = [text , button , buttonEdge]
    groupDraw(interface, window)

    return interface

#to set up input box
def inputBox(window):
    phraseBox = Entry(Point(200, 200), 30)
    phraseBox.setText("")
    phraseBox.draw(window)

    return phraseBox

#to set up textAcronym
def outputText(window):   
    textAcronym = Text(Point(200, 200), "")
    textAcronym.setSize(35)
    textAcronym.draw(window)

    return textAcronym

#to set up program end
def endProgram(window):
    time.sleep(2)
    close = Text(Point(200, 375), "Click anywhere to close.")
    close.draw(window)
    window.getMouse()
    window.close()

#main program
def main():    

    win = createGUI()
    display = interface(win)
    phraseBox = inputBox(win)
    textAcronym = outputText(win)
    
    #get phrase from user
    win.getMouse()
    phrase = (phraseBox.getText())

    #convert first letters to uppercase
    phraseCap = (phrase.title())

    #split string into list
    prep = phraseCap.split()
    
    #get first letters and create acronym
    acronym = ""
    for w in prep:
        initial = (w[0])
        acronym = acronym + initial

    #output
    groupUndraw(display)
    phraseBox.undraw()
    beepBoop(win)
    textAcronym.setText("Your acronym is: \n" + acronym)

    endProgram(win)


main()
