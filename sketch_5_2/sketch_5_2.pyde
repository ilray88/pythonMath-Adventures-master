def setup():
    size(600,600)
    rectMode(CENTER)
    colorMode(HSB) #for the rainbow colors
    strokeWeight(2) #a little thicker line

t = 0

def draw():
    global t
    background(255)#white
    translate(width/2,height/2)
    for i in range(90):
        #space the triangles evenly
        #around the circle
        rotate(radians(360/90))
        pushMatrix() #save this orientation
        #go to circumference of circle
        translate(200,0)
        #add color to each triangle
        stroke(2*i,255,255)
        #spin each triangle
        rotate(radians(t+2*i*360/90))
        #draw the triangle
        tri(100)
        #return to saved orientation
        popMatrix()
    t += 0.5
    saveFrame("image.png");
def tri(length):
    noFill() #makes the triangle transparent
    triangle(0,-length,
             -length*sqrt(3)/2, length/2,
             length*sqrt(3)/2, length/2)
add_library('pdf')
