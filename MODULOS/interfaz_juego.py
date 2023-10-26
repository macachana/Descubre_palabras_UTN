'''
JUEGO = DESCUBRE LAS PALABRAS 
CODIGO PRINCIPAL
ALUMNA = MACARENA CHANAMPA
1 B
'''
#APLICAR TIPOS DE DATOS AVANZADOS
'''

A PARTIR DEL CODIGO HECHO EN EL DOJO, REALICE VARIAS MODIFICACIONES PARA QUE FUNCIONE MI JUEGO
YA QUE PROBABA DE UNA FORMA U OTRA Y NO FUNCIONABA LA PARTE DE LOS BOTONES POR LO CUAL
AGREGUE VARIAS FUNCIONES QUE ME PERMITIAN REALIZAR LAS ACCIONES NECESARIAS PARA QUE PUEDA JUGAR

'''
try:
    import pygame
    from pygame import *
    import pygame.font
    import sys
    from funciones_juego import *
    from niveles_data import *
    from colores_y_fonts import *
    import os
    from fondos import *
    import csv
except IOError:
    print("No se pudo importar un modulo")
# Inicialización de Pygame
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("DESCUBRE LAS PALABRAS UTN") 

#secciones del juego inicializados en False excepto intro que es la primera seccion
intro = True
segunda_parte = False
nivel_uno = False
nivel_dos = False
nivel_tres = False
nivel_terminado = False
nivel_perdido = False
seccion_puntaje = False
como_se_juega = False

# Letras seleccionadas
letras_seleccionadas = []
palabras_encontradas_f = []
palabras_encontradas_m = []
palabras_encontradas_d = []
letras_sin_seleccionar = []
palabras_en_pantalla = []
#tiempo y puntaje
puntaje = 0
tiempo_restante = 90
partidas_perdidas = 1

# Configuración del reloj
clock = pygame.time.Clock()        
bandera_tiempo = True
FPS = 30
try:
    botones_1 = dibujar_letras(lista_let_facil)
    botones_2 = dibujar_letras(lista_let_medio)
    botones_3 = dibujar_letras(lista_let_dificil)
except NameError:
    print("alguna variable ingresada como parametro no existe o no fue definida")
except TypeError:
    print("falta ingresar parametros en las funciones")
nivel = 0
# Bucle principal del juego
while True:
    while intro:
        try:
            screen.blit(fondo,(0,0))
        except FileNotFoundError:
            print("el archivo no existe")
        for i in pygame.event.get():          
            if i.type == pygame.QUIT: 
                sys.exit()
            if i.type == MOUSEBUTTONDOWN and i.button==1:
                if Rect(270,300,250,80).collidepoint(mouse.get_pos()):
                    intro = False
                    nivel_uno = True
                if Rect(100,400,600,100).collidepoint(mouse.get_pos()):
                    intro = False
                    como_se_juega = True

        fondo_animado(screen,MORADO,font_itali,palabras,palabras_en_pantalla)

        
        boton_cuadrado(screen,Rect(90,150,620,100),"ADIVINA LA PALABRA",font_2,MORADO)
        pintar_boton_cuadrado(screen,Rect(270,300,250,80),"PLAY",font,MORADO)
        pintar_boton_cuadrado(screen,Rect(100,400,600,100),"¿COMO SE JUEGA?",font,MORADO)

        pygame.display.flip()
    
    while segunda_parte:
        lista_eventos = pygame.event.get()
        for i in lista_eventos:
            if i.type == pygame.QUIT:
                sys.exit()
            elif i.type == MOUSEBUTTONDOWN and i.button==1:
                if boton_nivel_facil.collidepoint(mouse.get_pos()):
                    tiempo_restante = 90
                    bandera_tiempo = True
                    letras_seleccionadas = []
                    lista_let_facil += letras_seleccionadas
                    palabras_encontradas_f = []                    
                    botones_1 = dibujar_letras(lista_let_facil)                  
                    segunda_parte = False
                    nivel_uno = True

                if boton_nivel_medio.collidepoint(mouse.get_pos()):
                    tiempo_restante = 90
                    bandera_tiempo = True
                    letras_seleccionadas = []
                    lista_let_medio += letras_seleccionadas
                    palabras_encontradas_m = []
                    botones_2 = dibujar_letras(lista_let_medio) 
                    segunda_parte = False
                    nivel_dos = True

                if boton_nivel_dificil.collidepoint(mouse.get_pos()):
                    tiempo_restante = 90
                    bandera_tiempo = True
                    letras_seleccionadas = []
                    lista_let_dificil += letras_seleccionadas
                    palabras_encontradas_d = []
                    botones_3 = dibujar_letras(lista_let_dificil)   
                    segunda_parte = False
                    nivel_tres = True
        try:
            screen.blit(fondo_niveles_1,(0,0))
        except FileNotFoundError:
            print("El archivo no existe o no se encuentra")

        boton_cuadrado(screen,Rect(80,30,650,100),"ELIJA EL NIVEL QUE DESEA JUGAR",font,BLANCO)

        #armamos los botones para nivel facil, nivel medio y nivel dificil
        boton_nivel_facil = Rect(250,150,250,100)
        boton_nivel_medio = Rect(250,280,250,100)
        boton_nivel_dificil = Rect(250,410,250,100)
        pintar_boton_cuadrado(screen,boton_nivel_facil,"NIVEL FACIL",font)
        pintar_boton_cuadrado(screen,boton_nivel_medio,"NIVEL MEDIO",font)
        pintar_boton_cuadrado(screen,boton_nivel_dificil,"NIVEL DIFICIL",font)

        pygame.display.update()

    while nivel_uno:
        clock.tick(2) 
        timer = pygame.time.get_ticks()
        try:
            screen.blit(fondo_nivel_1,(0,0))
        except FileNotFoundError:
            print("El archivo no existe o no se encuentra")
        dibujar_barra_de_letra(screen,BLANCO)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for letra, boton_rect in botones_1:
                    if boton_rect.collidepoint(x, y) and letra in lista_let_facil:
                        letras_seleccionadas.append(letra)
                        lista_let_facil.remove(letra)  # Elimina la letra seleccionada
                        botones_1.remove((letra, boton_rect))  # Elimina el botón correspondiente
                    
                    #BOTON CLEAR
                if Rect(310,330,200,60).collidepoint(mouse.get_pos()): 
                    #Restablece las letras seleccionadas y recupera los botones y letras disponibles
                    lista_let_facil += letras_seleccionadas
                    letras_seleccionadas = []
                    botones_1 = dibujar_letras(lista_let_facil) 

                    # Vuelve a llenar la lista de botones
                    for letra, boton_rect in botones_1:
                        if boton_rect.collidepoint(x, y) and letra in lista_let_facil:
                            letras_seleccionadas.append(letra)
                            lista_let_facil.remove(letra)  # Elimina la letra seleccionada
                            botones_1.remove((letra, boton_rect))  # Elimina el botón correspondiente

                    #BOTON SHUFFLE
                if Rect(90,330,200,60).collidepoint(mouse.get_pos()):    
                    shuffle = random.shuffle(lista_let_facil)
                    botones_1 = dibujar_letras(lista_let_facil)
                    # Vuelve a llenar la lista de botones
                    for letra, boton_rect in botones_1:
                        if boton_rect.collidepoint(x, y) and letra in lista_let_facil:
                            letras_seleccionadas.append(letra)
                            lista_let_facil.remove(letra)  # Elimina la letra seleccionada
                            botones_1.remove((letra, boton_rect))  # Elimina el botón correspondiente


                    #BOTON SUBMIT
                if Rect(530,330,200,60).collidepoint(mouse.get_pos()):
                    #cuando se aprete el boton se analizara la palabra ingresada
                    palabra = str("".join(letras_seleccionadas)) #unimos todas las letras ingresadas
                    palabra_min = palabra.lower() #como la palabra ingresada es en letras mayusculas, cambiamos las letras a minusculas
                    if palabra_min in combinaciones_nivel_facil:
                        if palabra not in palabras_encontradas_f:
                            if len(palabras_encontradas_f) < 9:
                                puntaje += len(palabra)
                                palabras_encontradas_f.append(palabra)
                            else:
                                if tiempo_restante > 0:
                                    nivel_uno = False
                                    nivel_terminado = True

                    #Restablece las letras seleccionadas y recupera los botones y letras disponibles
                    lista_let_facil += letras_seleccionadas
                    letras_seleccionadas = []                    
                    botones_1 = dibujar_letras(lista_let_facil) 

                    # Vuelve a llenar la lista de botones
                    for letra, boton_rect in botones_1:
                        if boton_rect.collidepoint(x, y) and letra in lista_let_facil:
                            letras_seleccionadas.append(letra)
                            lista_let_facil.remove(letra)  # Elimina la letra seleccionada
                            botones_1.remove((letra, boton_rect))  # Elimina el botón correspondiente

        # Muestra las letras seleccionadas
        letras_seleccionadas_texto = '   '.join(letras_seleccionadas)
        mostrar_texto2(screen,letras_seleccionadas_texto, 180, 240, (0, 0, 0),font_2)
        # Dibuja los botones con las letras disponibles
        for letra, boton_rect in botones_1:
            pygame.draw.rect(screen,(255,255,255), boton_rect)  # Color del botón
            mostrar_texto2(screen,letra, boton_rect.centerx - 12, boton_rect.centery - 12, (0, 0, 0),font)  # Muestra la letra en el botón

        palabras_convertidas = capitalize_lista(palabras_encontradas_f)

        dibujar_palabras_correctas(screen,palabras_convertidas,font_itali,screen_height,CELESTE) 

        boton_cuadrado(screen,Rect(20,8,500,50),f"TIEMPO RESTANTE : {tiempo_restante}",font,CELESTE)

        crear_botones_de_niveles(screen,font)

        if bandera_tiempo:
            # Restar tiempo
            tiempo_restante -= 1

        if tiempo_restante == 0:
            if partidas_perdidas < 3:    
                partidas_perdidas +=1
                nivel_uno = False
                nivel_perdido = True
                bandera_tiempo = False
            else:
                nivel_uno = False
                seccion_puntaje = True
                bandera_tiempo = False

        pygame.display.flip()

    while nivel_dos:
        clock.tick(2)
        timer = pygame.time.get_ticks()
        try:
            screen.blit(fondo_nivel_dos,(0,0))
        except FileNotFoundError:
            print("El archivo no existe o no se encuentra")        
        dibujar_barra_de_letra(screen,BLANCO)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for letra, boton_rect in botones_2:
                    if boton_rect.collidepoint(x, y) and letra in lista_let_medio:
                        letras_seleccionadas.append(letra)
                        lista_let_medio.remove(letra)  # Elimina la letra seleccionada
                        botones_2.remove((letra, boton_rect))  # Elimina el botón correspondiente
                    #BOTON CLEAR
                if Rect(310,330,200,60).collidepoint(mouse.get_pos()): 
                    #Restablece las letras seleccionadas y recupera los botones y letras disponibles
                    lista_let_medio += letras_seleccionadas
                    letras_seleccionadas = []
                    botones_2 = dibujar_letras(lista_let_medio) 

                    # Vuelve a llenar la lista de botones
                    for letra, boton_rect in botones_2:
                        if boton_rect.collidepoint(x, y) and letra in lista_let_medio:
                            letras_seleccionadas.append(letra)
                            lista_let_medio.remove(letra)  # Elimina la letra seleccionada
                            botones_2.remove((letra, boton_rect))  # Elimina el botón correspondiente

                    #BOTON SHUFFLE
                if Rect(90,330,200,60).collidepoint(mouse.get_pos()):    
                    shuffle = random.shuffle(lista_let_medio)
                    botones_2 = dibujar_letras(lista_let_medio)
                    # Vuelve a llenar la lista de botones
                    for letra, boton_rect in botones_2:
                        if boton_rect.collidepoint(x, y) and letra in lista_let_medio:
                            letras_seleccionadas.append(letra)
                            lista_let_medio.remove(letra)  # Elimina la letra seleccionada
                            botones_2.remove((letra, boton_rect))  # Elimina el botón correspondiente


                    #BOTON SUBMIT
                if Rect(530,330,200,60).collidepoint(mouse.get_pos()):
                    #cuando se aprete el boton se analizara la palabra ingresada
                    palabra = str("".join(letras_seleccionadas)) #unimos todas las letras ingresadas
                    palabra_min = palabra.lower() #como la palabra ingresada es en letras mayusculas, cambiamos las letras a minusculas
                    if palabra_min in combinaciones_nivel_medio:
                        if palabra not in palabras_encontradas_m:
                            if len(palabras_encontradas_m) < 9:
                                puntaje += len(palabra)
                                palabras_encontradas_m.append(palabra)
                            else:
                                if tiempo_restante > 0:
                                    nivel_dos = False
                                    nivel_terminado = True

                    #Restablece las letras seleccionadas y recupera los botones y letras disponibles
                    lista_let_medio += letras_seleccionadas
                    letras_seleccionadas = []                    
                    botones_2 = dibujar_letras(lista_let_medio) 

                    # Vuelve a llenar la lista de botones
                    for letra, boton_rect in botones_2:
                        if boton_rect.collidepoint(x, y) and letra in lista_let_medio:
                            letras_seleccionadas.append(letra)
                            lista_let_medio.remove(letra)  # Elimina la letra seleccionada
                            botones_2.remove((letra, boton_rect))  # Elimina el botón correspondiente

        
        # Muestra las letras seleccionadas
        letras_seleccionadas_texto = '   '.join(letras_seleccionadas)
        mostrar_texto2(screen,letras_seleccionadas_texto, 180, 240, (0, 0, 0),font_2)
        # Dibuja los botones con las letras disponibles
        for letra, boton_rect in botones_2:
            pygame.draw.rect(screen, (255,255,255), boton_rect)  # Color del botón
            mostrar_texto2(screen,letra, boton_rect.centerx - 12, boton_rect.centery - 12, (0, 0, 0),font)  # Muestra la letra en el botón
        
        #CONVERTIMOS LAS PALABRAS DE LA LISTA DE "PALABRAS_ENCONTRADAS" A CAPITALIZE()
        palabras_convertidas = capitalize_lista(palabras_encontradas_m)
        dibujar_palabras_correctas(screen,palabras_convertidas,font_itali,screen_height,AMARILLO) 

        boton_cuadrado(screen,Rect(30,8,500,50),f"TIEMPO RESTANTE : {tiempo_restante}",font,AMARILLO)

        crear_botones_de_niveles(screen,font)

        if bandera_tiempo:
            # Restar tiempo
            tiempo_restante -= 1

        if tiempo_restante == 0:
            if partidas_perdidas < 3:
                partidas_perdidas +=1
                nivel_dos = False
                nivel_perdido = True
                bandera_tiempo = False

            else:
                nivel_dos = False
                seccion_puntaje = True
                bandera_tiempo = False
                
        pygame.display.flip()

    while nivel_tres:   
        clock.tick(2)  

        try:
            screen.blit(fondo_nivel_tres,(0,0))
        except FileNotFoundError:
            print("El archivo no existe o no se encuentra")

        #creamos la barra en donde estaran los botones
        draw.rect(screen,BLANCO,(60,60,700,120),0,10)

        #creamos la barra en donde estaran las letras
        draw.rect(screen,BLANCO,(110,220,600,80),0,10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for letra, boton_rect in botones_3:
                    if boton_rect.collidepoint(x, y) and letra in lista_let_dificil:
                        letras_seleccionadas.append(letra)
                        lista_let_dificil.remove(letra)  # Elimina la letra seleccionada
                        botones_3.remove((letra, boton_rect))  # Elimina el botón correspondiente
                    
                    #BOTON CLEAR
                if Rect(310,330,200,60).collidepoint(mouse.get_pos()): 
                    #Restablece las letras seleccionadas y recupera los botones y letras disponibles
                    lista_let_dificil += letras_seleccionadas
                    letras_seleccionadas = []
                    botones_3 = dibujar_letras(lista_let_dificil) 

                    # Vuelve a llenar la lista de botones
                    for letra, boton_rect in botones_3:
                        if boton_rect.collidepoint(x, y) and letra in lista_let_dificil:
                            letras_seleccionadas.append(letra)
                            lista_let_dificil.remove(letra)  # Elimina la letra seleccionada
                            botones_3.remove((letra, boton_rect))  # Elimina el botón correspondiente

                    #BOTON SHUFFLE
                if Rect(90,330,200,60).collidepoint(mouse.get_pos()):    
                    shuffle = random.shuffle(lista_let_dificil)
                    botones_3 = dibujar_letras(lista_let_dificil)
                    # Vuelve a llenar la lista de botones
                    for letra, boton_rect in botones_3:
                        if boton_rect.collidepoint(x, y) and letra in lista_let_dificil:
                            letras_seleccionadas.append(letra)
                            lista_let_dificil.remove(letra)  # Elimina la letra seleccionada
                            botones_3.remove((letra, boton_rect))  # Elimina el botón correspondiente


                    #BOTON SUBMIT
                if Rect(530,330,200,60).collidepoint(mouse.get_pos()):
                    #cuando se aprete el boton se analizara la palabra ingresada
                    palabra = str("".join(letras_seleccionadas)) #unimos todas las letras ingresadas
                    palabra_min = palabra.lower() #como la palabra ingresada es en letras mayusculas, cambiamos las letras a minusculas
                    if palabra_min in combinaciones_nivel_dificil:
                        if palabra not in palabras_encontradas_d:
                            if len(palabras_encontradas_d) < 9:
                                puntaje += len(palabra)
                                palabras_encontradas_d.append(palabra)
                            else:
                                if tiempo_restante > 0:
                                    nivel_tres = False
                                    nivel_terminado = True


                    #Restablece las letras seleccionadas y recupera los botones y letras disponibles
                    lista_let_dificil += letras_seleccionadas
                    letras_seleccionadas = []                    
                    botones_3 = dibujar_letras(lista_let_dificil) 

                    # Vuelve a llenar la lista de botones
                    for letra, boton_rect in botones_3:
                        if boton_rect.collidepoint(x, y) and letra in lista_let_dificil:
                            letras_seleccionadas.append(letra)
                            lista_let_dificil.remove(letra)  # Elimina la letra seleccionada
                            botones_3.remove((letra, boton_rect))  # Elimina el botón correspondiente

        
        # Muestra las letras seleccionadas
        letras_seleccionadas_texto = '   '.join(letras_seleccionadas)
        mostrar_texto2(screen,letras_seleccionadas_texto, 180, 240, (0, 0, 0),font_2)

        # Dibuja los botones con las letras disponibles
        for letra, boton_rect in botones_3:
            pygame.draw.rect(screen, (255,255,255), boton_rect)  # Color del botón
            mostrar_texto2(screen,letra, boton_rect.centerx - 12, boton_rect.centery - 12, (0, 0, 0),font)  # Muestra la letra en el botón
        
        #CONVIERTO LAS PALABRAS CON EL METODO CAPITALIZE()
        palabras_convertidas = capitalize_lista(palabras_encontradas_d)

        dibujar_palabras_correctas(screen,palabras_convertidas,font_itali,screen_height,ROJO_OSCURO)

        boton_cuadrado(screen,Rect(30,8,500,50),f"TIEMPO RESTANTE : {tiempo_restante}",font,ROJO_OSCURO)

        crear_botones_de_niveles(screen,font)

        if bandera_tiempo:
            # Restar tiempo
            tiempo_restante -= 1

        if tiempo_restante == 0:
            if partidas_perdidas < 3:
                partidas_perdidas +=1
                nivel_tres = False
                nivel_perdido = True
                bandera_tiempo = False

            else:
                nivel_tres = False
                seccion_puntaje = True
                bandera_tiempo = False

        pygame.display.flip()
 
    while nivel_terminado:
        screen.fill(VERDE_PASTEL)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()      
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if Rect(200,250,410,80).collidepoint(mouse.get_pos()):
                    nivel_terminado = False
                    segunda_parte = True
                if Rect(200,400,400,80).collidepoint(mouse.get_pos()):
                    nivel_terminado = False
                    seccion_puntaje = True
                if Rect(250,500,300,100).collidepoint(mouse.get_pos()):
                    exit()
        mostrar_texto2(screen,"FELICIDADES",300,15,NEGRO,font)
        mostrar_texto2(screen,"¡¡¡ HA COMPLETADO EL NIVEL !!!",100,50,NEGRO,font)
        mostrar_texto2(screen,"ESPERO QUE SE HAYA DIVERTIDO",105,100,NEGRO,font)
        mostrar_texto2(screen,"PUEDE SEGUIR AUMENTANDO PUNTOS",90,150,NEGRO,font)
        mostrar_texto2(screen,"LLENDO AL MENU DE NIVELES",130,200,NEGRO,font)
        pintar_boton_cuadrado(screen,Rect(200,250,410,80),"IR AL MENÚ DE NIVELES",font,VERDE_PASTEL)
        mostrar_texto2(screen,"O PUEDE VER SU PUNTAJE FINAL",105,350,NEGRO,font)
        pintar_boton_cuadrado(screen,Rect(200,400,400,80),"PUNTAJE FINAL",font,VERDE_PASTEL)
        pintar_boton_cuadrado(screen,Rect(250,480,310,100),"SALIR",font,VERDE_PASTEL)
        
        pygame.display.update()

    while nivel_perdido:
        screen.fill(ROJO_PASTEL)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()    
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if Rect(150,460,220,50).collidepoint(mouse.get_pos()):
                    exit()

                if Rect(50,400,220,50).collidepoint(mouse.get_pos()):  
                    tiempo_restante = 90
                    bandera_tiempo = True
                    letras_seleccionadas = []
                    lista_let_facil += letras_seleccionadas
                    palabras_encontradas_f = []                  
                    botones_1 = dibujar_letras(lista_let_facil)
                    nivel_perdido = False
                    nivel_uno = True

                if Rect(280,400,220,50).collidepoint(mouse.get_pos()):
                    tiempo_restante = 90
                    bandera_tiempo = True
                    letras_seleccionadas = []
                    lista_let_medio += letras_seleccionadas
                    palabras_encontradas_m = []
                    botones_2 = dibujar_letras(lista_let_medio) 
                    nivel_perdido = False
                    nivel_dos = True

                if Rect(520,400,240,50).collidepoint(mouse.get_pos()):
                    tiempo_restante = 90
                    bandera_tiempo = True
                    letras_seleccionadas = []
                    lista_let_dificil += letras_seleccionadas
                    palabras_encontradas_d = []
                    botones_3 = dibujar_letras(lista_let_dificil)                     
                    nivel_perdido = False
                    nivel_tres = True
                
        pantalla_para_mensaje = Rect(10,5,780,580)
        try:
            texto = leer_archivo("parcial_juego\mensaje_perdio.txt")
        except IOError:
            print("Parece que el archivo no existe o no se puede acceder a el")

        boton_cuadrado(screen,Rect(10,10,780,510),texto,font_3,ROJO_CLARITO)

        crear_botones_de_perdio(screen,font)

        pygame.display.update()
    
    while seccion_puntaje:
        screen.fill(ROJO_PASTEL)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()    
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if boton_salir.collidepoint(mouse.get_pos()):
                    exit()
        mostrar_texto2(screen,f"SU PUNTAJE ES: {puntaje}",160,200,NEGRO,font_2)
        boton_salir = Rect(250,400,300,80)
        pintar_boton_cuadrado(screen,boton_salir,"SALIR",font_2,VERDE_PASTEL)

        pygame.display.update()
    
    while como_se_juega:
        try:
            screen.blit(fondo,(0,0))
        except FileNotFoundError:
            print("El archivo no existe o no se encuentra")  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()     
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if boton_back.collidepoint(mouse.get_pos()):
                    como_se_juega = False
                    intro = True
        fondo_animado(screen,MORADO,font_itali,palabras,palabras_en_pantalla)
        
        texto_como_se_juega(screen,font,BLANCO,font_4) 

        #creamos el boton back para que una vez en la seccion de informacion se pueda volver al inicio
        boton_back = Rect(10,30,100,35)
        pintar_boton_cuadrado(screen,boton_back,"BACK",font,MORADO)
        pygame.display.update()

    clock.tick(FPS)  