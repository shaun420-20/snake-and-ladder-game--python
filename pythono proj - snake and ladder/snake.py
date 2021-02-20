import pygame
import time 
import random
# used to activate all pygame modules
pygame.init()
screen = pygame.display.set_mode((650,500))
pygame.display.set_caption('snake and Ladder ')
# background
backimg = pygame.image.load('bckimg.jpg')
backimg = pygame.transform.scale(backimg,(500,500))
bg2 = pygame.image.load("down.jpg")
arrow = pygame.image.load("arrow.png")
arrow = pygame.transform.scale(arrow,(25,25))

bx = 150
by = 5




#players

r1=pygame.image.load("pin (1).png")
r1 = pygame.transform.scale(r1,(25,25))
 
b1 =pygame.image.load("placeholder.png")
b1 = pygame.transform.scale(b1,(25,25))
rx =100
ry = 251

b1x =100
b1y =362
button = pygame.Rect(10,50,40,40)


font1 = pygame.font.SysFont("comicsansms",25)
font2 = pygame.font.SysFont("comicsansms",20)
def bck():
    screen.blit(bg2,(0,5))
    screen.blit(backimg,(bx,by))
    screen.blit(arrow,(10,50))

def rplayer(x,y):
    screen.blit(r1,(x,y))

def bplayer(x,y):
    screen.blit(b1,(x,y))
    
def pickNumber():
    diceroll = random.randint(1,6)
    if diceroll ==1:
        dice = pygame.image.load("d1.png")
    elif diceroll ==2:
        dice = pygame.image.load("d2.png")
    elif diceroll ==3:
        dice = pygame.image.load("d3.png")
    elif diceroll ==4:
        dice = pygame.image.load("d4.png")
    elif diceroll ==5:
        dice = pygame.image.load("d5.png")
    elif diceroll == 6:
        dice = pygame.image.load("d6.png")
    return (dice,diceroll)




def players():
    
    msg1 =font1.render("player1",True,(225,0,0))
    screen.blit(msg1,[5,251])
    msg2 =font1.render("player2",True,(0,0,225))
    screen.blit(msg2,[5,362])

    
def rollr():
    msg3 = font2.render("your turn",True,(255,255,255))
    screen.blit(msg3,[25,290])

def rollb():
    msg4 = font2.render("your turn",True,(255,255,255))
    screen.blit(msg4,[5,400])    
    
# gamel loop
running  = True
turn = 'red'

while running:
    screen.fill((0,255,195))
    bck()
    players()

    if turn== 'red':
        rollr()
    else:
        rollb()
        
        
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button.collidepoint(mouse_pos):
                pickNumber()
                dice,diceroll = pickNumber()
                screen.blit(dice,(50,60))
                print(diceroll)

                # for player 1


                if pickNumber() and turn =='red':
                    turn = 'blue'
                    if  diceroll== 6 and rx ==100 and ry == 251:
                        rx = 162
                        ry = 447
                        turn = 'red'
                        # ry value stays same for the first row
                        
                    elif rx in range(162,358) and diceroll != 6 and (ry ==447 or ry== 349 or ry == 251 or ry == 153 or ry == 55):
                        
                        rx = rx + (49 * diceroll)
                            
                    elif  rx in range(162,358) and diceroll == 6 and (ry == 447 or ry== 349 or ry == 251 or ry == 153 or ry == 55):
                        
 
                        rx = rx + (49 * diceroll)
                        turn = 'red'
                            
                    elif  rx ==358 and diceroll != 6 and (ry == 447 or ry== 349 or ry == 251 or ry == 153 or ry == 55):
                        

                        rx = rx + (49 * diceroll)
                            
                    elif  rx ==358 and diceroll == 6 and (ry == 447 or ry== 349 or ry == 251 or ry == 153 or ry == 55):
                        
                        rx = rx + (49 * 5)
                        ry = ry - 49
                        turn = 'red'
                    elif  rx ==407 and diceroll <= 4 and (ry == 447 or ry== 349 or ry == 251 or ry == 153 or ry == 55):
                        rx = rx + (49 * diceroll)
                            
                    elif  rx ==407 and diceroll > 4 and diceroll != 6 and(ry == 447 or ry== 349 or ry == 251 or ry == 153 or ry == 55):
                        rx = rx + (49 * 4)
                        ry =ry-49
                            
                         # when dice roll comes 6 and we have to move to next y column then we do 1-diceroll   
                    elif  rx ==407 and diceroll == 6 and (ry == 447 or ry== 349 or ry == 251 or ry == 153 or ry == 55):
                        

                        rx = rx + (49* 4 )- (49*(diceroll -5))
                        ry = ry-49
                        turn ='red'
                        
                    elif  rx ==456 and diceroll <= 3 and (ry == 447 or ry== 349 or ry == 251 or ry == 153 or ry == 55):
                        rx = rx + (49 * diceroll)

                        

                            
                    elif  rx ==456 and diceroll>3 and diceroll!=6 and (ry == 447 or ry== 349 or ry == 251 or ry == 153 or ry == 55):
                        

                        rx= rx + (49 * 3)- (49*(diceroll -4))
                        ry = ry-49
                                                 
                    elif  rx ==456  and diceroll==6 and (ry == 447 or ry== 349 or ry == 251 or ry == 153 or ry == 55):
                        

                        rx= rx + (49 * 3)- (49*(diceroll -4)) # -2 of if 5 or 6 
                        ry = ry-49
                        turn ='red'
                                                 
                    elif  rx == 505 and diceroll <= 2 and (ry == 447 or ry== 349 or ry == 251 or ry == 153 or ry == 55):
                        rx = rx + (49 * diceroll)
                       
                    elif  rx ==505 and diceroll > 2 and diceroll != 6 and (ry == 447 or ry== 349 or ry == 251 or ry == 153 or ry == 55):
                        

                        rx = rx + (49 * 2)- (49*(diceroll -3))
                        ry = ry-49                     



                    elif  rx ==505  and diceroll==6 and (ry == 447 or ry== 349 or ry == 251 or ry == 153 or ry == 55):
                        rx = rx + (49 * diceroll)

                        rx= rx + (49 * 2)- (49*(diceroll -3))  
                        ry = ry-49
                        turn ='red'
                                                 
                    elif  rx == 554 and diceroll == 1 and (ry == 447 or ry== 349 or ry == 251 or ry == 153 or ry == 55):
                        rx = rx + (49 * diceroll)

                        
                            
                            
                    elif  rx ==554 and diceroll > 1 and diceroll != 6 and (ry == 447 or ry== 349 or ry == 251 or ry == 153 or ry == 55):
                        

                        rx = rx + (49 * 1)- (49*(diceroll -2))

                        ry = ry-49

                    elif  rx ==554  and diceroll==6 and (ry == 447 or ry== 349 or ry == 251 or ry == 153 or ry == 55):
                        

                        rx= rx + (49 * 1)- (49*(diceroll -2))  
                        ry = ry-49
                        turn ='red'
                                                
                    elif  rx >=603 and diceroll != 6 and (ry == 447 or ry== 349 or ry == 251 or ry == 153 or ry == 55):
                    

                        rx = rx - (49*(diceroll -1))
                        ry = ry-49
                            
                    elif  rx ==603 and diceroll == 6 and (ry == 447 or ry== 349 or ry == 251 or ry == 153 or ry == 55):
                        

                        rx = rx - (49*(diceroll -1)
                        ry= ry-49
                        turn ='red'
                                                 
                        # for row 2
                                                 
                    elif  rx >358 and rx <= 603 and ry ==398 and diceroll != 6:
                        rx = rx-(49* diceroll)
                            
                    elif  rx > 358 and rx <= 603 and ry ==398 and diceroll == 6:
                        rx = rx-(49* 5)
                        ry = ry - 49
                        turn ='red'
                            
                    elif  rx > 407  and ry ==398 and diceroll != 6:
                        rx = rx-(49* diceroll)
                            
                    elif  rx > 407  and ry ==398 and diceroll == 6:
                        rx = rx-(49* 5)
                        ry = ry -49
                        turn = 'red'

                    elif  rx == 358  and ry ==398 and diceroll == 5:
                        rx = rx-(49* 4)+ (49*(diceroll-5))
                        ry = ry - 49

                    elif  rx == 309  and ry ==398 and diceroll <4 :
                        rx = rx-(49* diceroll)
                            

                    elif  rx == 309  and ry ==398 and diceroll >=4 and diceroll !=6:
                        rx = rx-(49* 3)+ (49*(diceroll-4))
                        ry = ry - 49
                            
                            
                    elif  rx == 309  and ry ==398 and  and diceroll ==6:
                        rx = rx-(49* 3)+ (49*(diceroll-4))
                        ry = ry - 49
                        turn = 'red'
                            
                    elif  rx == 260  and ry ==398 and diceroll <3:
                        rx = rx-(49* diceroll)
                            
                            
                    elif  rx == 260  and ry ==398 and dicerll>=3 and diceroll !=6:
                        rx = rx-(49* 2)+ (49*(diceroll-3))
                        ry = ry - 49


                    elif  rx == 260  and ry ==398 and diceroll ==6:
                        rx = rx-(49* 2)+ (49*(diceroll-3))
                        ry = ry - 49    
                        turn ='red'
                            
                    elif  rx == 211  and ry ==398   and diceroll <2:
                        rx = rx-(49* diceroll)
                            
                            
                    elif  rx == 211  and ry ==398 and dicerll>=2 and diceroll !=6:
                        rx = rx-49+ (49*(diceroll-2))
                        ry = ry - 49


                    elif  rx == 211  and ry ==398 and diceroll ==6:
                        rx = rx-49+ (49*(diceroll-2))
                        ry = ry - 49
                        turn = 'red


                    elif  rx ==162  and ry ==398 and diceroll !=6:
                        rx = rx+(49* diceroll-1))
                        ry= ry -49
                            
                    elif  rx == 162  and ry ==398 and diceroll ==6:
                        rx = rx +(49*(diceroll-1))
                        ry = ry - 49
                        turn = 'red'
                            


    

                            


                            
 




                            

                 # for player 2    
                elif pickNumber() and turn =='blue':
                    turn = 'red' 
                    if  diceroll== 6 and b1x ==100 and b1y == 362:
                        b1x = 162
                        b1y = 450
                        turn = 'blue'


    rplayer(rx,ry)
    bplayer(b1x,b1y)
    pygame.display.update()
    time.sleep(1.3)
    
pygame.quit()
quit()
