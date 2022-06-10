import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

#mendefinisikan sudut-sudutnya
vertices = (
#Vertices Rotasi Tidur
(1, 0, -1), #Titik 0
(1, 0, 1),  #Titik 1
(-1, 0, 1), #Titik 2
(-1, 0, -1), #Titik 3
(0, 3, 0), #Titik 4
)

#mendefinisikan garis
edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 4),
    (1, 4),
    (3, 4),
)

#mendefinisikan warna
colors = (
    (1, 1, 1),
    (1, 0, 0),
    (1, 1, 0),
    (0, 0, 1),
    (1, 0, 1),
    (0, 1, 1),
    (1, 1, 1),
    (1, 0, 0),
    (1, 1, 0),
    (0, 0, 1),
    (1, 0, 1),
    (0, 1, 1),
    )

#mendefisikan sisi
surfaces = (
    #Diamond
    (0, 1, 4),
    (0, 3, 4),
    (2, 1, 4),
    (2, 3, 4),
)

#menggambar Limas
def Limastumpuk():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_TRIANGLES)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()

#menambahkan layar untuk menampilkan limas
def main():
    #inisialisasi pygame
    pygame.init()
    #resolusi display layar
    display = (800,600)
    #mode layar double buffering
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    #mengatur judul pada windows
    pygame.display.set_caption("Menggambar Limas - Mega")
    #mengubah perspektif, fov 45*, znear 0.1, zfar 50
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    #memindahkan objek sesuai dengan matrix translate
    glTranslatef(0.0,0.0, -7)
    #infinite looping
    while True:
        #apabila ditekan tombol x, maka program akan berhenti.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #apabila ada tombol keyboard yang ditekan, 
        #maka akan dilakukan fungsi berikut
        if event.type == pygame.KEYDOWN:
            #bila yang di tekan tombol panah kiri
            #pindahkan kubus ke kiri sebanyak 0.5
            if event.key == pygame.K_LEFT:
                glTranslatef(-0.5,0,0)
            if event.key == pygame.K_RIGHT:
                glTranslatef(0.5,0,0)

            if event.key == pygame.K_UP:
                glTranslatef(0,1,0)
            if event.key == pygame.K_DOWN:
                glTranslatef(0,-1,0)
        if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0,0,1.0)

                if event.button == 5:
                    glTranslatef(0,0,-1.0)
        #arah gerak perputaran limas
        glRotatef(1, 1, 1, 0)
        #menghapus semua kanvas/display
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Limastumpuk()
        pygame.display.flip()
        #menunggu 10ms sebelum looping lagi
        pygame.time.wait(10) 
main()