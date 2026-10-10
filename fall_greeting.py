# Created by: Sara
# Purpose: HW3 , practicing using graphics and time library
# Created at: 9/29/25, 12:20am
# Last modified: 9/29/25, 5:26pm

#import the graphic and time library
from graphics import *
from time import *

def fall_greeting():

    #create the window
    WIDTH = 600
    HEIGHT = 800
    #name of the window and size
    win = GraphWin("Cat Pumpkin", WIDTH, HEIGHT)
    win.setBackground("black")

    #create the greeting text at the top
    greeting = Text(Point(300, 100),"Happy Fall!")
    #set color of text
    greeting.setFill("dark orange")
    #set size of text
    greeting.setSize(60)
    greeting.draw(win)



    ##draw pumpkin w/ multiple circles, background circles go first
    #far left side of pumpkin
    pumpkin_far_left = Circle(Point(190,450),160)
    pumpkin_far_left.draw(win)
    #set to orange w/ dark orange outlines
    pumpkin_far_left.setFill("orange")
    pumpkin_far_left.setOutline("dark orange")

    #left side of pumpkin
    pumpkin_left = Circle(Point(240,450),160)
    pumpkin_left.draw(win)
    #set to orange w/ dark orange outlines
    pumpkin_left.setFill("dark orange")
    pumpkin_left.setOutline("dark orange")

    #right side of pumpkin
    pumpkin_far_right = Circle(Point(410,450),160)
    pumpkin_far_right.draw(win)
    #set to orange w/ dark orange outlines
    pumpkin_far_right.setFill("orange")
    pumpkin_far_right.setOutline("dark orange")

    #right side of pumpkin
    pumpkin_right = Circle(Point(360,450),160)
    pumpkin_right.draw(win)
    #set to orange w/ dark orange outlines
    pumpkin_right.setFill("dark orange")
    pumpkin_right.setOutline("dark orange")

    #middle of pumpkin last so it's on top of other sides
    pumpkin = Circle(Point(300,450),160)
    pumpkin.draw(win)
    #set to orange w/ dark orange outlines
    pumpkin.setFill("orange")
    pumpkin.setOutline("dark orange")

    #create left ear + keep it orange and centered
    left_ear = Polygon(Point(160, 300), Point(210,230), Point(260, 300))
    left_ear.setFill("dark orange")
    left_ear.setOutline("dark orange")
    left_ear.draw(win)

    #create right ear + keep it orange and centered
    right_ear = Polygon(Point(340, 300), Point(390,230), Point(440, 300))
    right_ear.setFill("dark orange")
    right_ear.setOutline("dark orange")
    right_ear.draw(win)


    
    #dont set color to these; set color in loop
    #create left eye under left ear
    #set all outlines to dark orange to match the pumpkin
    left_eye = Circle(Point(210,390),40)
    left_eye.setOutline("dark orange")
    left_eye.draw(win)

    #create right eye under right ear
    right_eye = Circle(Point(390,390),40)
    right_eye.setOutline("dark orange")
    right_eye.draw(win)

    #create nose ; align w/ center of middle circle for symmetry
    nose = Polygon(Point(250, 450), Point(300,480), Point(350, 450))
    nose.setOutline("dark orange")
    nose.draw(win)

    #create mouth of cat pumpkin using polygon for the teeth and the mouth;easier to make 1 shape
    mouth = Polygon(Point(160, 500), Point(210,570), Point(260, 507),Point(340, 507), Point(390,570), Point(440, 500))
    mouth.setOutline("dark orange")
    mouth.draw(win)


    
    #create loop here for flickering
    #set to 30 for amt of times looped
    for i in range(30):
        #fill all black objects to yellow
        left_eye.setFill("yellow")
        right_eye.setFill("yellow")
        nose.setFill("yellow")
        mouth.setFill("yellow")
  
        #sleep for 0.1 before changing colors
        sleep(0.1)
        #fill all objects to dark orange to go from yellow -> dark orange
        left_eye.setFill("dark orange")
        right_eye.setFill("dark orange")
        nose.setFill("dark orange")
        mouth.setFill("dark orange")
     
        #sleep for 0.1 before changing colors
        sleep(0.1)
        #fill to black to give flickering effect of light off and on
        left_eye.setFill("black")
        right_eye.setFill("black")
        nose.setFill("black")
        mouth.setFill("black")

        #sleep for 0.1 before changing colors
        sleep(0.1)
    


    #create the ending text at the bottom telling user to click to close
    closing = Text(Point(300, 700),"Click Anywhere to Close!")
    #set color of text
    closing.setFill("dark orange")
    #set size of text; smaller than title text
    closing.setSize(30)
    closing.draw(win)

    #get mouse to let user close by clicking
    win.getMouse()



#use main to call function
def main():
    fall_greeting()

main()
