In matrices.pyde, in the draw function, multiply the f-matrix by a, b and c. Here�s the whole code:
#set the range of x-values
xmin=-10
xmax=10

#range of y-values
ymin = -10
ymax = 10

#calculate the range
rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    global xscl, yscl
    size(600,600)
    #the scale factors for drawing on the grid:
    xscl= width / rangex
    yscl= -height / rangey

def draw():
    global xscl, yscl
    background(255) #white
    translate(width/2,height/2)
    grid(xscl, yscl)
    #multiply fmatrix by chosen transformation matrix
    newmatrix = multmatrix(fmatrix,a)
    noFill()
    strokeWeight(1) #thinner line
    stroke(0) #black
    graphPoints(fmatrix)
    strokeWeight(2) #thicker line
    stroke(255,0,0) #red
    graphPoints(newmatrix)

fmatrix = [[0,0],[1,0],[1,2],[2,2],[2,3],[1,3],[1,4],
         [3,4],[3,5],[0,5]]

transformation_matrix = [[0,-1],[1,1]]
a = [[1,0],[0,-1]]
b = [[0,-1],[-1,0]]
c = [[-1,1],[1,1]]

def graphPoints(matrix):
    #draw line segments between consecutive points
    beginShape()
    for pt in matrix:
        vertex(pt[0]*xscl,pt[1]*yscl)
    endShape(CLOSE)

def multmatrix(a,b):
    #Returns the product of two matrices
    #b is a 2x2
    newmatrix = []
    for i in range(len(a)):
        newmatrix.append([])
        for j in range(2):
            newmatrix[i].append(a[i][0]*b[0][j]+a[i][1]*b[1][j])
    return newmatrix


def graphPoints(matrix):
    strokeWeight(2) #thicker line
    #stroke(255,0,0) #red
    #draw line segments between consecutive points
    for i,pt in enumerate(matrix):
        if i < len(matrix) - 1:
            line(pt[0]*xscl,pt[1]*yscl,
                matrix[i+1][0]*xscl,matrix[i+1][1]*yscl)
        else: #connect first and last point
            line(matrix[0][0]*xscl,matrix[0][1]*yscl,
                 matrix[-1][0]*xscl,matrix[-1][1]*yscl)

def grid(xscl, yscl):
    '''Draws a grid for graphing'''
    #cyan lines
    strokeWeight(1)
    stroke(0,255,255)
    for i in range(xmin, xmax + 1):
        line(i*xscl, ymin*yscl, i*xscl, ymax*yscl)
    for i in range(ymin,ymax+1):
        line(xmin*xscl, i*yscl, xmax*xscl, i*yscl)
    stroke(0) #black axes
    line(0,ymin*yscl,0,ymax*yscl)
    line(xmin*xscl,0, xmax*xscl,0)

Here�s what the transformations look like:
