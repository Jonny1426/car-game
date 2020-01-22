import pygame
from random import randint


pygame.init()

#Variaveis de posição
''' carro principa l'''
x = 540
y = 360
''' carro azul '''
pos_x = 330
pos_y = 800
''' carro branco '''
pos_y_a = 1200
''' carro preto '''
pos_y_c = 1600

#variaveis de velocidade
velocidade = 15
velocidade_outros = 20

#imagens
fundo = pygame.image.load('pista.png')
carro = pygame.image.load('carro_principal.png')
carro_azul = pygame.image.load('carro_azul.png')
carro_branco = pygame.image.load('carro_branco.png')
#xb = 493
carro_preto = pygame.image.load('carro_preto.png')
#xp = 640

''' Definições do cronometro '''
timer = 0
tempo_segundo = 0

font = pygame.font.SysFont('arial black', 30) 
texto = font.render("Tempo: ", True, (255,255,255), (0,0,0)) 
post_texto = texto.get_rect()
post_texto.center = (68,60) 

'''difinições da janela'''
janela = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("matematica-06-12") 
janela_aberta = True 

while janela_aberta :
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    '''definição das teclas de movimentação do carro principal'''
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if comandos[pygame.K_RIGHT] and x <= 650:
        x += velocidade
    if comandos[pygame.K_LEFT] and x >= 327:
        x -= velocidade

    ''' Configurações cronometro '''
    if (timer < 10):
        timer += 1
    else:
        tempo_segundo += 1
        texto = font.render("Tempo: "+str(tempo_segundo), True, (255,255,255), (0,0,0))
        timer = 0


    '''respawn aleatorio, determinada entre limites'''
    if (pos_y <= -200) and (pos_y_a <= -200) and (pos_y_c <= -200):
        pos_y = randint(800,1100) #azul
        pos_y_a = randint(1400,2000)#branco
        pos_y_c = randint(2300,3000)#preto

    '''tornando velocidade dos carros aleatorias'''
    pos_y -= velocidade_outros + randint(1,10)
    pos_y_a -= velocidade_outros + randint(1,10)
    pos_y_c -= velocidade_outros + randint(1,10)

    '''Jogando na tela'''
    janela.blit(fundo,(0,0)) 
    janela.blit(carro, (x,y)) #carro principal
    janela.blit(carro_azul, (pos_x, pos_y)) #carro azul
    janela.blit(carro_branco,(pos_x + 163, pos_y_a)) #carro branco
    janela.blit(carro_preto,(pos_x + 310, pos_y_c)) # carro preto
    janela.blit(texto, post_texto) 

    pygame.display.update()

pygame.quit()
