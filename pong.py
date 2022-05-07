from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.collision import *
from PPlay.keyboard import *

#Janela:
janela = Window(1280,720)

#Fundo:
fundo = GameImage("fundo.jpg")

#Teclado:
teclado = Window.get_keyboard()

#Sprites:
#Bola:
bola = Sprite("bola.png",1) #1 = número de imagens
bola.x = janela.width/2 - bola.width/2
bola.y = janela.height/2 - bola.height/2

#Pad
pad1 = Sprite("pad1.png",1)
pad2 = Sprite("pad2.png",1)
pad1.y = janela.height/2 - pad1.height/2
pad1.x = +55

pad2.y= janela.height/2 - pad2.height/2
pad2.x= janela.width - pad2.width/2 - 80

velocidadeBola_x = 800
velocidadeBola_y = 800
velocidadePad1_y = 500
velocidadePad2_y = 500
contadorEsquerdo = 0
contadorDireito = 0

#Game Loop
while(True):
    bola.x += velocidadeBola_x * janela.delta_time()
    bola.y += velocidadeBola_y * janela.delta_time()

    if (bola.collided(pad1) or bola.collided(pad2)):
        if not pad_collision_in_progress:
            pad_collision_in_progress = True
            velocidadeBola_x *= -1
    else:
        pad_collision_in_progress = False

    if (bola.y < 0) or (bola.y + bola.height > janela.height):
        if not wall_collision_in_progress:
            wall_collision_in_progress = True
            velocidadeBola_y *= -1
    else:
        wall_collision_in_progress = False

    if (bola.x < 0):
        bola.x = janela.width/2 - bola.width/2
        bola.y = janela.height/2 - bola.height/2
        contadorEsquerdo += 1
    if (bola.x + bola.width > janela.width):
        bola.x = janela.width/2 - bola.width/2
        bola.y = janela.height/2 - bola.height/2
        contadorDireito += 1
    if(teclado.key_pressed("UP")) and (pad2.y > 0):
        pad2.y += velocidadePad2_y * -janela.delta_time()
    if (teclado.key_pressed("DOWN")) and (pad2.y <= janela.height-pad2.height):
        pad2.y += velocidadePad2_y * janela.delta_time()
    if (teclado.key_pressed("w")) and (pad1.y > 0):
        pad1.y += velocidadePad1_y * -janela.delta_time()
    if (teclado.key_pressed("s")) and (pad1.y <= janela.height -pad1.height):
        pad1.y += velocidadePad1_y * janela.delta_time()
    if contadorDireito > 10 or contadorEsquerdo > 10:
        janela.delta_time()

    #desenho
    janela.set_background_color([0,0,100])
    fundo.draw()
    bola.draw()
    pad1.draw()
    pad2.draw()

    #Placar
    janela.draw_text(str(contadorDireito), (janela.width/2) - 6, 60, size = 40, font_name = "Arial", bold = True, color = [255, 255, 255])
    janela.draw_text(str(contadorEsquerdo), (janela.width/2) + 60, 60, size = 40, font_name = "Arial", bold = True, color = [255, 255, 255])
    janela.update()