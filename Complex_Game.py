import pygame
from time import sleep
import cmath
pygame.init()
# כמה פיקסלים אתה רוצה שיהיו יחידה אחת במסך
scale = 50
white = (255,255,255)
gray = (80,80,80)
#אורך ורוחב המסך, מעדיף שיהיה מספר שמתחלק יפה
W = 360*3
H = 360*3
GRID = False
GRID_FUNC = False
SCREEN = pygame.display.set_mode((W,H))
#הפונקציה אותה המסך מציג
def CF(z):
     try:
        # return cmath.log(z ** 2, cmath.e)
        # return z*complex(0.2,0.2)
        # return cmath.sin(z)
        return cmath.log(z)

        # return complex(0,1)/z**2
        # return z**3
     except:
         return complex(0,0)
def draw_dots(input_pos):
    # A,B = the input and output position of the function at the pygame window
    # z,w = the compelx input and the complex output of the function
    # the position need to be shifted to center and change to scale to be converted to the complex value
    A = input_pos
    z = complex((A[0] - W // 2) / scale, (H // 2 - A[1]) / scale)
    w = CF(z)
    B = [int(w.real * scale + W // 2), int(H // 2 - w.imag * scale)]

    font = pygame.font.SysFont(None, 24)
    # draw line betweeen A and B
    pygame.draw.line(SCREEN, white, A, B)
    # draw a red circle at A
    pygame.draw.circle(SCREEN, (255, 0, 0, 0), A, 5)

    # draw a blue circle at B
    pygame.draw.circle(SCREEN, (0, 0, 255, 0), B, 5)
    if not GRID_FUNC:
        to_round = scale//70
        # add text of the complex values of z at A
        img = font.render(str(round(z.real, to_round)) + " + " + str(round(z.imag, to_round)) + "i", True, white)
        SCREEN.blit(img, [input_pos[0], input_pos[1] - 30])
        # add text of the complex values of w at B
        img = font.render(str(round(w.real,to_round)) + " + " + str(round(w.imag,to_round)) + "i", True, white)
        SCREEN.blit(img, [B[0],B[1]-30])

def grid_func():
        # scale = W//20
        # takse evrey combenation of hole numbers and set it to "draw_dots"
        for i in range(W // (2 * scale)):
            for j in range(H // (2 * scale)):
                try:
                    draw_dots((W // 2 - scale*i, H // 2 + scale*j))
                    draw_dots((W // 2 - scale*i, H // 2 - scale*j))
                    draw_dots((W // 2 + scale*i, H // 2 + scale*j))
                    draw_dots((W // 2 + scale*i, H // 2 - scale*j))
                except:
                    pass
                pygame.display.flip()
        # אם רוצים שרק הציר הממשי ישמש כקלט אפשר להשתמש בלולאה הזאת במקום
        # for i in range(W // (2 * scale)):
            # draw_dots((W // 2 - scale * i, H // 2))
            # draw_dots((W // 2 + scale * i, H // 2))

# הפונקציה שמוחקת את הנקודות לפני שהיא רושמת נקודות חדשות
def add_gride():
    for i in range(W // (2 * scale)):
        pygame.draw.line(SCREEN, gray, (W // 2 + scale * i, 0), (W // 2 + scale * i, H - 1))
    for i in range(W // (2 * scale)):
        pygame.draw.line(SCREEN, gray, (W // 2 - scale * i, 0), (W // 2 - scale * i, H - 1))
    for i in range(H // (2 * scale)):
        pygame.draw.line(SCREEN, gray, (0, H // 2 - scale * i), (W - 1, H // 2 - scale * i))
    for i in range(H // (2 * scale)):
        pygame.draw.line(SCREEN, gray, (0, H // 2 + scale * i), (W - 1, H // 2 + scale * i))

def reset():
    SCREEN.fill((0,0,0))
    pygame.draw.line(SCREEN,white,(0,H//2),(W-1,H//2))
    pygame.draw.line(SCREEN,white,(W//2,0),(W//2,H-1))
    pygame.draw.circle(SCREEN,(255,255,255,255),(W//2,H//2),scale,1)
    global GRID
    if GRID:
        add_gride()
    if GRID_FUNC:
        grid_func()
    # pygame.display.flip()

reset()
font = pygame.font.SysFont(None, 45)
s = ["Q -> quit program","SPACE -> show mouse output","F -> show vector field (integers)","G -> show grid lines","UP/DONE -> change distance"]
for i in range(len(s)):
    img = font.render(s[i], True, white)
    SCREEN.blit(img, [70, 150+50*i])

pygame.display.flip()

running =True
while running:
    ev = pygame.event.get()
    k = pygame.key.get_pressed()
    # אם לוחצים q המשחק נגמר
    if k[pygame.K_q]:
        running=False
    #כאשר לוחצים על רווח הקלט מהעכבר מגיע
    if k[pygame.K_SPACE]:
        reset()
        p = pygame.mouse.get_pos()
        draw_dots(p)
        pygame.display.flip()
        sleep(0.08)
    # אם לוחצים g הרשת מופיעה
    if k[pygame.K_g]:
        GRID = not GRID
        pygame.display.flip()
        sleep(0.1)
    # מקשי החיצים משנים מרחק מתצוגה
    if k[pygame.K_UP]:
        scale +=10
        reset()
        pygame.display.flip()
        sleep(0.1)
    if k[pygame.K_DOWN]:
        if scale>10:
            scale-=10
        reset()
        pygame.display.flip()
        sleep(0.1)
    # לחיצה על f מראה לאן הולכת כל נקודה שלמה בלוח
    if k[pygame.K_f]:
        GRID_FUNC = not GRID_FUNC
        reset()
        pygame.display.flip()
        sleep(0.1)