import pygame
from time import sleep
from math import sin,cos,pi,sqrt
pygame.init()
white = (255,255,255)
W = 900
H = 900
F = -200
L = 8
M = 9
RADIUS = min(H,W) / 2.6
SCREEN = pygame.display.set_mode((W,H))
SCREEN.fill((0, 0, 0))
pygame.display.flip()


class Electron:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed_x = 0
        self.speed_y = 0
        self.force_x = 0
        self.force_y = 0
        self.pressure = 0

    def distance_squared(self, other):
        return ((self.pos_x - other.pos_x) ** 2 + (self.pos_y - other.pos_y) ** 2)

    def apply_force(self, electrons):
        # Reset force and pressure to zero
        self.force_x = 0
        self.force_y = 0
        self.pressure = 0

        # Loop through all electrons
        for electron in electrons:
            # Skip over self
            if electron != self:
                # Calculate distance squared between self and electron
                dist = self.distance_squared(electron)
                if dist == 0:
                    dist = 0.001
                # Calculate force between self and electron using Coulomb's Law
                force = F / dist

                # Calculate x and y components of force
                if electron.pos_x - self.pos_x == 0:
                    self.force_x += force
                else:
                    self.force_x += force * ((electron.pos_x - self.pos_x) / sqrt(dist))
                    self.force_y += force * ((electron.pos_y - self.pos_y) / sqrt(dist))

                # Calculate pressure
                self.pressure += abs(force)

        # Update speed based on force
        self.speed_x += self.force_x
        self.speed_y += self.force_y

    def move(self):
        # Check if the next position is inside the circle with radius RADIUS centered at (W // 2, H // 2)
        if (((self.pos_x + self.speed_x) - W // 2) ** 2 + ((self.pos_y + self.speed_y) - H // 2) ** 2) <= RADIUS ** 2:
            # Update position if inside circle
            self.pos_x += self.speed_x
            self.pos_y += self.speed_y
        else:
            # Stop movement if outside circle and reset force
            self.speed_x = 0
            self.speed_y = 0
            self.force_x = 0
            self.force_y = 0

    def draw(self, screen, max_pressure):
        # calculate the color of the circle based on the pressure and max pressure
        color = self.pressure / max_pressure

        # draw a circle on the screen with the calculated color
        pygame.draw.circle(screen, (255 * color, 0, 255 * (1 - color), 0), [int(self.pos_x), int(self.pos_y)], 10)

        # draw a line representing the current velocity of the particle
        # the velocity is multiplied by 500 to make it more visible
        pygame.draw.line(screen, (255, 0, 255), [int(self.pos_x), int(self.pos_y)],
                         [int(self.pos_x + 15 * self.speed_x), int(self.pos_y + 15 * self.speed_y)], 2)

        # draw a line representing the current force acting on the particle
        # the force is multiplied by 500 to make it more visible
        pygame.draw.line(screen, (0, 255, 0), [int(self.pos_x), int(self.pos_y)],
                         [int(self.pos_x + 500 * self.force_x), int(self.pos_y + 500 * self.force_y)], 2)


# Create a list of electrons
electrons = []
for i in range(2, L):
    for j in range(2, M):
        electrons.append(Electron(30 + i * W / (L + 2), 30 + j * H / (M + 2)))

# Main game loop
PATH = "C:\\Users\ohadz\Desktop\\frame\\"
I = 0
#set the number of frames you like
while I < 700:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # sys.exit()

    # Clear the screen
    SCREEN.fill((0, 0, 0))

    # Apply forces to electrons
    max_pressure = 0
    for electron in electrons:
        electron.apply_force(electrons)
        max_pressure = max(max_pressure, electron.pressure)

    # Move electrons
    for electron in electrons:
        electron.move()
    sleep(0.01)
    # Draw electrons
    for electron in electrons:
        electron.draw(SCREEN,max_pressure)
    # update the screen
    pygame.display.flip()