def setup():
    size(600,600)
def draw():
    background(255)
    translate(100,100)
    snowflake(400,1)
    saveFrame("image.png");
def snowflake(sz,level):
    for i in range(3):
        line(0,0,sz,0)
        translate(sz,0)
        rotate(radians(120))
