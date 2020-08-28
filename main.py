import pygame

pygame.init()
display = pygame.display.set_mode((800, 600))

pygame.display.set_caption("foo")
clock = pygame.time.Clock()

ded = False

player1_img = pygame.image.load('assets/plane_small_grey.png')
p1vx, p1vy, p1x, p1y, p1ro = (0, 0, 0, 0, 0)

def player1(x, y, ro):
    display.blit(pygame.transform.rotate(player1_img, ro) , (x, y))


while not ded:
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_w]:
        p1y -= 5

    elif pressed[pygame.K_s]:
        p1y += 5

    elif pressed[pygame.K_a]:
        p1ro = (p1ro - 5) % 360

    elif pressed[pygame.K_d]:
        p1ro = (p1ro + 5) % 360

    display.fill((255, 255, 255))
    player1(50, 50, p1ro)

    pygame.display.update()
    clock.tick(60)

def i():
    goto(xcor(), ycor() + in_game_speed)

def w():
    goto(xcor(), ycor() + in_game_speed)

def k():
    goto(xcor(), ycor() - in_game_speed)

def s():
    goto(xcor(), ycor() - in_game_speed)

screen.onkeypress(player.up, "i")
screen.onkeypress(player.up, "w")
screen.onkeypress(player.down, "k")
screen.onkeypress(player.down, "s")