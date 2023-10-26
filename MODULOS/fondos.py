import pygame

# Tamaño de la pantalla
screen_width = 800
screen_height = 600

##### ICONO #####3
icono = pygame.image.load("parcial_juego\Imagenes\icono.png") #agregamos el icono en una variable
pygame.display.set_icon(icono) 

#### FONDOS #########
#agregamos los fondos
fondo = pygame.image.load("parcial_juego\Imagenes\intro.png")
fondo = pygame.transform.scale(fondo,(screen_width,screen_height))   

fondo_seleccion_niveles_1 = pygame.image.load("parcial_juego\Imagenes\\fondo_sel_niveles_1.png")
fondo_niveles_1 = pygame.transform.scale(fondo_seleccion_niveles_1,(screen_width,screen_height))
fondo_nivel_uno = pygame.image.load("parcial_juego\Imagenes\\fondo_nivel_uno.png")
fondo_nivel_1 = pygame.transform.scale(fondo_nivel_uno,(screen_width,screen_height))
fondo_nivel_dos = pygame.image.load("parcial_juego\Imagenes\\fondo_nivel_dos.jpg")
fondo_nivel_2 = pygame.transform.scale(fondo_nivel_dos,(screen_width,screen_height))
fondo_nivel_tres = pygame.image.load("parcial_juego\Imagenes\\fondo_nivel_tres.jpg")
fondo_nivel_3 = pygame.transform.scale(fondo_nivel_tres,(screen_width,screen_height))