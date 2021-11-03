
t = 0

def tri(length):
    '''Draws an equilateral triangle
    around center of triangle'''
    triangle(0,-length,
            -length*sqrt(3)/2, length/2,
            length*sqrt(3)/2, length/2)

def setup():
    size(600,600)
    rectMode(CENTER)

def draw():
    global t
    #set background white
    background(255)
    translate(width/2,height/2)
    for i in range(12):
        pushMatrix() #save this orientation
        translate(200,0)
        rotate(radians(t))
        tri(50) #this line is changed from geometry.pyde
        popMatrix() #return to the saved orientation
        rotate(radians(360/12))
    t += 1
    saveFrame("image.png");
