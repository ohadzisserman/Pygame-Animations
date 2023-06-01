import pygame
from time import sleep
import math
pygame.init()
white = (255,255,255)
gray = (80,80,80)
#אורך ורוחב המסך
W = 360*2
H = 360*2
#מספר שורות
N = 22
# כמה פיקסלים אתה רוצה שיהיו יחידה אחת במסך
scale = 14
# התדירות בה האות מתקבל
FREQ = 20
global MAX
MAX = [0]
ENERGY_LOSS = 0
SCREEN = pygame.display.set_mode((W,H))
PRESSURE = [[0 for i in range(N)] for j in range(N)]
VELOCITY = [[0 for i in range(N)] for j in range(N)]
ENERGY = [0 for i in range(N)]

def update():
    #עדכון המהירויות לפי הכוח שמפיעילים עליהן האזורים השכנים
    for i in range(N):
        for j in range(1,i):
            VELOCITY[i][j]+=(0.5*PRESSURE[i][j-1]+0.5*PRESSURE[i][j+1]-PRESSURE[i][j])*(1-ENERGY_LOSS)
    #עדכון הלחץ לפי מהירות השינוי
    for i in range(N):
        for j in range(N):
            PRESSURE[i][j]+=VELOCITY[i][j]
    #עדכון סך האנגירה היחסית
    for i in range(1,len(ENERGY)):
        ENERGY[i] = sum([abs(PRESSURE[i][j])+abs(VELOCITY[i][j]) for j in range(N)])/i


def puls(addition):
    for i in range(N):
        PRESSURE[i][0]=addition
    pygame.draw.line(SCREEN, white, (10, 70 + (N + 8) * scale),
                     (W - 10, 70 + (N + 8) * scale), 1)

    if addition>0:
        pygame.draw.line(SCREEN,((255 * addition) // 1, 50, 20),(10, 70 + (N +8-addition*4) * scale),(W-10, 70 + (N +8-addition*4) * scale),int(addition*5)+3)
    else:

        pygame.draw.line(SCREEN,(20, 50, (255 * abs(addition)) // 1),(10, 70 + (N +8-addition*4) * scale),(W-10, 70 + (N +8-addition*4) * scale),int(abs(addition*5))+3)



def draw():

    maxGrid= max([max(k) for k in PRESSURE[2:]])
    if maxGrid > MAX[0]:
          MAX[0]=maxGrid
    m = MAX[0]
    Emax = max (ENERGY)
    if Emax == 0:
        Emax = 1
    m2 = min([min(k) for k in PRESSURE[2:]])
    for i in range(3,N):
        e = ENERGY[i]/Emax
        pygame.draw.rect(SCREEN,((255 * e) // 1, 20, (255 * (1-e)) // 1),(i * 2 * scale - 30-scale/2,70+N * scale,scale,scale))
        for j in range(0, i+1):
            p = PRESSURE[i][j]
            if p>0:
                if m!=0:
                    p = (p / m)
                pygame.draw.circle(SCREEN, ((255 * p)//1, 40, 20), (i * 2*scale-30, 70+j * scale), scale // 3+scale*p//3)
            else:
                if m!=0:
                    p = (p / m)
                if p<0:
                    p=-p
                if p>1:
                    p=1
                pygame.draw.circle(SCREEN,(20,40,(255*p)//1),(i*2*scale-30,70+j*scale),scale//3+scale*p//3)


    pygame.display.flip()



def reset():
    SCREEN.fill((0,0,0))

reset()

pygame.display.flip()
I = 0
PATH = "C:\\Users\ohadz\Desktop\\frame\\"
running =True
while running:
    # sleep(0.01)
    if I<300:
        add =math.sin(I*2*math.pi/FREQ)
    if I==300:
        PRESSURE = [[0 for i in range(N)] for j in range(N)]
        VELOCITY = [[0 for i in range(N)] for j in range(N)]
        MAX=[0]
    if I >= 300:
        add =0.5*( math.sin(I * 2 * math.pi / 32)+math.sin(I * 2 * math.pi / 42))
    reset()
    puls(add)
    update()
    print(I,MAX)

    draw()
    I+=1

    # pygame.image.save(SCREEN,PATH+str(I)+".png")

    k = pygame.key.get_pressed()
    # אם לוחצים q המשחק נגמר
    if k[pygame.K_q]:
        running=False
