import pygame
from time import sleep
import math
pygame.init()
# כמה פיקסלים אתה רוצה שיהיו יחידה אחת במסך
scale = 20
white = (255,255,255)
gray = (80,80,80)
#אורך ורוחב המסך, מעדיף שיהיה מספר שמתחלק יפה
W = 360*2
H = 360*2
N = 30
SCREEN = pygame.display.set_mode((W,H))
POSITION = [[0 for i in range(N)] for j in range(N)]
VELOCITY = [[0 for i in range(N)] for j in range(N)]

def change_grid():
    for i in range(N):
        for j in range(1,i):
            VELOCITY[i][j]+=(0.5*POSITION[i][j-1]+0.5*POSITION[i][j+1]-POSITION[i][j])

    for i in range(N):
        for j in range(N):
            POSITION[i][j]+=VELOCITY[i][j]


def puls(addition):
    for i in range(N):
        POSITION[i][1]+=addition

def draw():
    m = max([max(k) for k in POSITION[2:]])
    m2 = min([min(k) for k in POSITION[2:]])
    for i in range(3,N):
        for j in range(0, i+1):
            p = POSITION[i][j]

            if p>0:
                if m!=0:
                    p = (p / m)

                pygame.draw.circle(SCREEN, ((255 * p)//1, 20, 0), (i * 2*scale-20, 30+j * scale), scale // 3)
            else:

                if m!=0:
                    p = (p / m)
                if p<0:
                    p=-p
                if p>1:
                    p=1
                print(p)
                pygame.draw.circle(SCREEN,(0,20,(255*p)//1),(i*2*scale-20,30+j*scale),scale//3)


    pygame.display.flip()



def reset():
    SCREEN.fill((0,0,0))
    # pygame.draw.line(SCREEN,white,(0,H//2),(W-1,H//2))
    # pygame.draw.line(SCREEN,white,(W//2,0),(W//2,H-1))
    # pygame.draw.circle(SCREEN,(255,255,255,255),(W//2,H//2),scale,1)

reset()

pygame.display.flip()
I = 0
PATH = "C:\\Users\ohadz\Desktop\\frame\\"
running =True
while running:
    # sleep(0.1)
    puls(math.sin(I*2*math.pi/20))
    change_grid()
    # print(I)
    # for i in VELOCITY:
    #     print(i)
    # print()
    # for i in POSITION:
    #     print(i)
    # print()
    reset()
    draw()
    # pygame.image.save(SCREEN,PATH+str(I)+".png")
    I+=1

    ev = pygame.event.get()
    k = pygame.key.get_pressed()
    # אם לוחצים q המשחק נגמר
    if k[pygame.K_q]:
        running=False
