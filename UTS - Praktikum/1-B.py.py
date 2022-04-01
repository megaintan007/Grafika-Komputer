from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def initFun():
    glClearColor(1.0,1.0,1.0,0.0)
    glColor3f(128.0,0.0, 0.0)
    glPointSize(5.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0,640.0,0.0,480.0)
    
def AlgDDA():
    #tentukan titik awal dan akhir
    x1 = 10
    y1 = 10
    x2 = 500
    y2 = 400
    x = x1
    y = y1

    #hitung dx dan dy
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    #hitung p 
    p = 2 * dy - dx
    duady = 2 * dy
    duadydx = 2 * (dy - dx)
    
    #tentukan titik awal dan akhir
    if (x1 > x2):
        x = x2
        y = y2
        xend = x1
    else:
        x = x1
        y = y1
        xend = x2
    

    #gambar titik awal
    glBegin(GL_POINTS)
    glVertex2i(x, y)

    #perulangan untuk menggambar titik-titik 
    while (x < xend):
        x = x+1
        if (p < 0):
            p += duady
        else:
            if (y1 > y2):
                y = y-1
            else:
                y = y+1
            p += duadydx
        glVertex2i(x, y)

    glEnd()
    glFlush()

if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(640,480)
    glutCreateWindow("Grafika Komputer - UTS")
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutDisplayFunc(AlgDDA)
    initFun()