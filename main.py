# BOMB DISPOSAL by Darryl Sloan

from microbit import *

# Replacement for "set_pixel" to bypass error
def plot(x, y, glow):
    if x >=0 and x <=4 and y >=0 and y <=4:
        led.plotBrightness(x, y, glow)

# Animation of bomb exploding
def explode(x, y, radius):
    for blast in range(radius):
        plot(x-blast, y-blast, 9-blast)
        plot(x, y-blast, 9-blast)
        plot(x+blast, y-blast, 9-blast)
        plot(x-blast, y, 9-blast)
        plot(x+blast, y, 9-blast)
        plot(x-blast, y+blast, 9-blast)
        plot(x, y+blast, 9-blast)
        plot(x+blast, y+blast, 9-blast)
        basic.pause(50)
        plot(x-blast, y-blast, 0)
        plot(x, y-blast, 0)
        plot(x+blast, y-blast, 0)
        plot(x-blast, y, 0)
        plot(x+blast, y, 0)
        plot(x-blast, y+blast, 0)
        plot(x, y+blast, 0)
        plot(x+blast, y+blast, 0)

# Game setup
player_x = 2
player_y = 2
enemy_x = randint(0, 4)
enemy_y = randint(0, 4)
timer = 0
delay = 450
lives = 3
score = 0
basic.showString("GO!")

# Main game loop

while True:

    # Display
    basic.clearScreen()
    led.plotBrightness(enemy_x, enemy_y, timer)
    led.plotBrightness(player_x, player_y, 9)

    # Consequences
    if enemy_x == player_x and enemy_y == player_y:
        score += 1
        for glow in range(9, -1, -1):
            led.plotBrightness(enemy_x, enemy_y, glow)
            basic.pause(100)
        enemy_x = randint(0, 4)
        enemy_y = randint(0, 4)
        timer = 0
    if timer == 9:
        explode(enemy_x, enemy_y, 5)
        lives -= 1
        if lives == 0:
            break
        player_x = 2
        player_y = 2
        enemy_x = randint(0, 4)
        enemy_y = randint(0, 4)
        timer = 0

    # Movements
    if input.acceleration(Dimension.Y) < -40 and player_y > 0:
        player_y -= 1
    elif input.acceleration(Dimension.Y) > 40 and player_y < 4:
        player_y += 1
    if input.acceleration(Dimension.X) < -40 and player_x > 0:
        player_x -= 1
    elif input.acceleration(Dimension.X) > 40 and player_x < 4:
        player_x += 1
    timer += 1
    basic.pause(delay)
    if delay > 250:
        delay -= 2

# Game over
basic.showString("SCORE ")
basic.showNumber(score)