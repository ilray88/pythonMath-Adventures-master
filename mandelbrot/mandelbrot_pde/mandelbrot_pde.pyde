#range of x-values
xmin = -2
xmax = 2
#range of y-values
ymin = -2
ymax = 2

#calculate the range
rangex = xmax - xmin
rangey = ymax - ymin

def cAdd(a,b):
    '''adds two complex numbers'''
    return [a[0]+b[0],a[1]+b[1]]

def cMult(u,v):
    '''Returns the product of two complex numbers'''
    return [u[0]*v[0]-u[1]*v[1],u[1]*v[0]+u[0]*v[1]]

def magnitude(z):
    return sqrt(z[0]**2 + z[1]**2)

def mandelbrot(z,num):
    '''runs the process num times
    and returns the diverge count'''
    count = 0
    #define z1 as z
    z1 = z
    #iterate num times
    while count <= num:
        #check for divergence
        if magnitude(z1) > 2.0:
            #return the step it diverged on
            return count
        #iterate z
        z1 = cAdd(cMult(z1,z1),z)
        count += 1
    return num

def setup():
    global xscl, yscl
    size(600,600)
    noStroke()
    xscl = float(rangex)/width
    yscl = float(rangey)/height

def draw():
    for x in range(width):
        for y in range(height):
            z=[(xmin+x*xsecl),
               (ymin+y*yscl)]
            col=mandelbrot(z,100)
            if col==100:
                fill(0)
            else:
                fill(255)
            rect(x,y,1,1)
    saveFrame("image.png");
 
