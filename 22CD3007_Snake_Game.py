#SNAKE GAME BY AYUSH PANDEY-22CD3007
import pygame
import random
import os

pygame.mixer.init()
pygame.init()


#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)


#Creating window :
screen_width=1400
screen_height=750
gameWindow=pygame.display.set_mode((screen_width,screen_height))


#Background image
bgimg=pygame.image.load("snake.jpg")
bgimg=pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()
#convert_alpha for constant speed of game



#Game by Ayush
pygame.display.set_caption("Snake Game By Ayush Pandey")
pygame.display.update()


clock=pygame.time.Clock()
font=pygame.font.SysFont(None,55)

#Function to display score on screen:
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])
def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,black,[x,y,snake_size,snake_size])

#Creating welcome screen:

def welcome():
    exit_game=False
    while not exit_game:
        
        gameWindow.fill((233,220,229))
        text_screen("Welcome to AYUSH Snake Xnezia",black,100,250)
        text_screen("Press Space bar to continue",black,120,300)
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pygame.mixer.music.load('bgm.mp3')
                    pygame.mixer.music.play()
                    
                    gameloop()   
        pygame.display.update()
        clock.tick(60)

#game loop
def gameloop():
    #Game specific variables:
    exit_game=False
    game_over=False
    snake_x=45
    snake_y=55
    velocity_x=0
    velocity_y=0
    
    snk_list=[]
    snk_length=1
    
    #Check if high score file exists:
    if(not os.path.exists("high_score.txt")):
        with open("high_score.txt","w")as f:
            f.write("0")
    
    
    with open("high_score.txt","r") as f:
        high_score=f.read()
    
    food_x=random.randint(0,screen_width)
    food_y=random.randint(0,screen_height)
    score=0
    snake_size=10
    init_velocity=5

    fps=60
    
    while not exit_game:
        
        if game_over:
            
            with open("high_score.txt","w") as f:
                f.write(str(high_score))
            gameWindow.fill(white)
            
            
            text_screen("Game over!Press enter to continue",red,100,100)
            
            
            for event in pygame.event.get():
                # print(event)
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()
        
        else:
            
            for event in pygame.event.get():
                # print(event)
                if event.type==pygame.QUIT:
                    exit_game=True
                
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0 
                        
                    if event.key==pygame.K_LEFT:
                        velocity_x=-init_velocity
                        velocity_y=0
                    if event.key==pygame.K_UP:
                        velocity_y=-init_velocity 
                        velocity_x=0  
                    if event.key==pygame.K_DOWN:
                        velocity_y=init_velocity
                        velocity_x=0 
                    
                    #Cheat CODE
                    # if event.key==pygame.K_q:
                    #     score=score+5        
            
            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y   
            
            if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
                score +=10
              
                
                food_x=random.randint(0,screen_width)
                food_y=random.randint(0,screen_height)
                snk_length+=5
                
                if score>int(high_score):
                    high_score=score
                
            gameWindow.fill(white)
            gameWindow.blit(bgimg,(0,0))
            #Displaying score on screen
            text_screen("Score:"+str(score)+"  HIGH SCORE:"+str(high_score),red,5,5)
            pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size])
            
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            
            # for deleting snake head or it will increase very much
            if len(snk_list)>snk_length:
                del snk_list[0]
            
            #for ending the game when the snake bite itself 
                            
            
            if head in snk_list[:-1]:
                game_over=True
                pygame.mixer.music.load('beep.mp3')
                pygame.mixer.music.play()
            
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True
                print("Game Over")
                pygame.mixer.music.load('beep.mp3')
                pygame.mixer.music.play()
            # pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
            plot_snake(gameWindow,black,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
