import pygame
import os
import random


WIDTH = 800
HEIGHT = 600
SIZE = 25

pygame.init()

fontsPath = os.path.join("fonts","COMIC.TTF")

font = pygame.font.Font(fontsPath,32)
start_text = font.render("Press ANY key to start! Or press ESC to exit",True,(255,255,0))
start_textRect = start_text.get_rect()
start_textRect.center = (WIDTH//2,HEIGHT//2)

end_text = font.render("Press R to try again! Or Press ESC to exit",True,(255,255,0))
end_textRect = end_text.get_rect()
end_textRect.center = (WIDTH//2,HEIGHT//2)


# draw snack
def drawSnack(snack):
    for [x,y] in snack:
        pygame.draw.rect(window,(0,255,0),[x,y,SIZE,SIZE])

#generate food position
def generateFood():
    while True:
        food_x = random.randrange(0,775,25)
        food_y = random.randrange(0,575,25)
        for x,y in snack:
            if x == food_x and y == food_y:
                continue
            else:
                return food_x,food_y
        

#is snack eat food
def getFood(head_x,head_y,food_x,food_y):
    if head_x == food_x and head_y == food_y:
        tail_x = snack[len(snack)-1][0]
        tail_y = snack[len(snack)-1][1]
        snack.append([tail_x,tail_y])
        return True
    else:
        return False
    

# draw food    
def drawFood(food_x,food_y):
    pygame.draw.rect(window,(255,0,0),[food_x,food_y,SIZE,SIZE])
    


# update position of each of the snack of body
def updatPosition(snack,pos_x,pos_y):
    for i in range(len(snack)-1,0,-1):
        snack[i][0] = snack[i-1][0]
        snack[i][1] = snack[i-1][1]

    snack[0][0] = pos_x
    snack[0][1] = pos_y


# logic of game

def moveDirection(event,dir_x,dir_y):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w and dir_y != speed:
            dir_y = -speed
            dir_x = 0
        elif event.key == pygame.K_s and dir_y != -speed:
            dir_y = speed
            dir_x = 0
        elif event.key == pygame.K_a and dir_x != speed:
            dir_x = -speed
            dir_y = 0
        elif event.key == pygame.K_d and dir_x != -speed:
            dir_x = speed
            dir_y = 0

    return dir_x,dir_y
        
def isOver(head_x,head_y,snack):
    if head_x > WIDTH-SIZE or head_x < 0 or head_y > HEIGHT-SIZE or head_y < 0:
        return True
    for i in range(1,len(snack)):
        if head_x == snack[i][0] and head_y == snack[i][1]:
            return True
    return False

def goBack():
    return [
[400,300],
[400,325],
[400,350]
],initX,initY,initDX,initDY


speed = SIZE


snack = [
[400,300],
[400,325],
[400,350]
]

# head initial position 
pos_x = 400 
pos_y = 300

#initial move driection
dir_x = 0
dir_y = -speed

# food initial position
food_x,food_y = generateFood()


initS = [
[400,300],
[400,325],
[400,350]
]

initX = pos_x
initY = pos_y
initDX = dir_x
initDY = dir_y



window = pygame.display.set_mode((WIDTH,HEIGHT))

clock = pygame.time.Clock()

running = True

game_state = "Start"
score = 0

while running:
    clock.tick(18)
    window.fill((0,0,0))

            

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if game_state == "Start":
                if event.key == pygame.K_ESCAPE:
                    running = False
                else:
                    game_state = "Playing"
            elif game_state == "Playing":
                dir_x,dir_y = moveDirection(event,dir_x,dir_y)
            elif game_state == "Over":
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    game_state = "Playing"



    if game_state == "Start":
        window.blit(start_text,start_textRect)
    elif game_state == "Playing":

        pos_x += dir_x
        pos_y += dir_y

        drawFood(food_x,food_y)

        if getFood(pos_x,pos_y,food_x,food_y):
            food_x,food_y = generateFood()    
        drawSnack(snack)

        if isOver(pos_x,pos_y,snack):
            snack,pos_x,pos_y,dir_x,dir_y = goBack()
            food_x,food_y = generateFood()
            game_state = "Over"


        if game_state != "Over":
            updatPosition(snack,pos_x,pos_y)
    elif game_state == "Over":
        window.blit(end_text,end_textRect)

    pygame.display.flip()

pygame.quit()
