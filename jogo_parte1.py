import pygame
pygame.init()

X=400
Y=300
pos_x=240
pos_y=300
velocidade = 10
velocidade_outros = 20
fundo = pygame.image.load('tela.jpg')#baixar PNG
carro = pygame.image.load('carro.png')
policia = pygame.image.load('policia.png')
ambulancia = pygame.image.load('ambulancia.png')
caminhonete = pygame.image.load('caminhonete.png')

janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption(" Meu jogo em python Elias Madrid")

janela_aberta = True
while janela_aberta :
    pygame.time.delay(50)
      
         for event in pygame.event.get() :
           if event.type == pygame.QUIT:
                janela_aberta = False

         comandos P pygame.key.get_pressed()
         if comandos[pygame.K_UP] : 
          Y -= velocidade  
          if comandos[pygame.K_DOWN] : 
          Y += velocidade
          if comandos[pygame.K_RIGHT] : 
          X += velocidade
          if comandos[pygame.K_LEFT] : 
          X -= velocidade 

          if(pos_y <= -200):
             pos_y = 600
          pos_y -= velocidade_outros

         # janela.fill((0,0,0))
          #pygame.draw.circle(janela, (0,255,0), (x, y),50)

          janela.blit(fundo,(0,0))
          janela.blit(carro,(x,y))
          janela.blit(policia,(pos_x,pos_y))
          janela.blit(ambulancia,(pos_x + 140, pos_y))
          

          pygame.display.update() 


 pygame.quit()               