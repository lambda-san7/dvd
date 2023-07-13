import pygame
import random
import time
import os

pygame.init()
width, height = 800, 600
window = pygame.display.set_mode((width, height),pygame.RESIZABLE)

dir_path = os.path.dirname(os.path.realpath(__file__))


dvd_image = pygame.transform.scale(pygame.image.load(f"{dir_path}/dvd.png"),(185,85))

color = (50,50,50)

corners = 0
flipped_x = False
flipped_y = False

class logo:
    def __init__(self,speed,function):
        self.x = random.randint(1,500)
        self.y = random.randint(1,500)
        self.w = 185
        self.h = 85
        self.horizontal = speed
        self.vertical = speed
        self.function = function
    def handle(self):
        global corners
        global color
        if self.function == "obs":
            color = (0,255,0)
        flipped_x, flipped_y = False, False
        self.x += self.horizontal
        self.y += self.vertical
        if self.x + self.horizontal <= 0:
            self.horizontal += self.horizontal * -2
            flipped_x = True
        if self.y + self.vertical <= 0:
            self.vertical += self.vertical * -2
            flipped_y = True
        if (self.x + self.horizontal) + self.w >= pygame.display.Info().current_w:
            self.horizontal -= self.horizontal * 2
            flipped_x = True
        if (self.y + self.vertical) + self.h >= pygame.display.Info().current_h:
            self.vertical -= self.vertical * 2
            flipped_y = True
        if flipped_x and flipped_y:
            window.fill((0,255,0))
            corners += 1
            if self.function == "teleport":
                self.x, self.y = random.randint(1,200),random.randint(1,200)
            if self.function == "speed":
                self.horizontal += 10
                self.vertical += 10
            if self.function == "chaos":  
                self.x, self.y = random.randint(0,pygame.display.Info().current_w),random.randint(0,pygame.display.Info().current_w)
                self.horizontal = random.randint(1,1000)
                self.vertical = random.randint(1,1000)
                color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                print(self.horizontal, self.vertical)
        window.blit(dvd_image,(self.x,self.y))

dvd = logo(10,"bounce")

class text:
    def __init__(self, size, text):
        self.font = pygame.font.Font(f"{dir_path}/font.fon",size)
        self.text_holder = text
        self.text = self.font.render(text, True, (255,255,255))
    def render(self,x,y):
        font = pygame.font.Font(f"{dir_path}/font.fon",32)
        text = font.render(self.text_holder, True, (0,0,0))
        window.blit(text,(x + 2,y))
        window.blit(text,(x - 2,y))
        window.blit(text,(x,y + 2))

        window.blit(text,(x,y - 2))

        window.blit(text,(x + 2,y + 2))
        window.blit(text,(x - 2,y + 2))
        window.blit(text,(x - 2,y - 2))
        window.blit(text,(x + 2,y - 2))

        window.blit(self.text,(x,y))

clock = pygame.time.Clock()

pygame.display.set_caption("DVD Bounce")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                dvd2 = logo(dvd.horizontal,dvd.function)
                dvd = dvd2
            if event.key == pygame.K_BACKSPACE:
                dvd2 = logo(50,dvd.function)
                dvd = dvd2
            if event.key == pygame.K_ESCAPE:
                pygame.display.set_caption("Exiting...")
                window.fill(0,0,0)
                corner = text(32, "Thanks For Using DVD Bounce!")
                corner.render((pygame.display.Info().current_w / 2) - corner.text.get_height(),(pygame.display.Info().current_h / 2) - corner.text.get_width())
                pygame.display.update()
                running = False
            if event.key == pygame.K_1:
                dvd.function = "bounce"
                color = (50,50,50)
            if event.key == pygame.K_2:
                dvd.function = "teleport"
                color = (50,50,50)
            if event.key == pygame.K_3:
                dvd.function = "speed"
                color = (50,50,50)
            if event.key == pygame.K_4:
                dvd.function = "chaos"
            if event.key == pygame.K_5:
                dvd.function = "obs"
            if event.key == pygame.K_PLUS:
                dvd.horizontal += 1
                dvd.vertical += 1
            if event.key == pygame.K_MINUS:
                dvd.horizontal -= 1
                dvd.vertical -= 1
    clock.tick(60)
    window.fill(color)
    corner = text(32, str(corners))
    corner.render(10,10)
    corner = text(32, dvd.function)
    corner.render((pygame.display.Info().current_w - corner.text.get_width()) - 10,10)
    corner = text(32, str(dvd.horizontal))
    if dvd.horizontal < 0:
        corner = text(32, str(dvd.horizontal * -1))
    corner.render(10,(pygame.display.Info().current_h - corner.text.get_height()) - 10)
    dvd.handle()
    pygame.display.update()

pygame.quit()