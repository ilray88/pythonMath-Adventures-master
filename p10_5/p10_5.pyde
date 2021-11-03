def setup():
    size(600,600)
def draw():
    background(255)
    translate(300,500)
    y(100)
    saveFrame("image.png");
def y(sz):
    line(0,0,0,-sz)
    translate(0,-sz)
    rotate(radians(30))
    line(0,0,0,-0.8*sz)
    rotate(radians(-60))
    line(0,0,0,-0.8*sz)
    rotate(radians(30))
    translate(0,sz)
