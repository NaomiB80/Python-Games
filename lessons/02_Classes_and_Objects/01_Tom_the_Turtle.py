""" Turtle in Pygame

We really miss the turtle module from Python's standard library. It was a great
way to introduce programming, so let's make something similar in PyGame, using
objects. 

"""
import math

import turtle

import pygame


def event_loop():
    """Wait until user closes the window"""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            

class Turtle:
    def __init__(self, screen, x: int, y: int):
        self.x = x
        self.y = y
        self.screen = screen
        self.angle = 0  # Angle in degrees, starting facing right

    def forward(self, distance):
        # Calculate new position based on current angle
        radian_angle = math.radians(self.angle)

        start_x = self.x  # Save the starting position
        start_y = self.y

        # Calculate the new position displacement
        dx = math.cos(radian_angle) * distance
        dy = math.sin(radian_angle) * distance

        # Update the turtle's position
        self.x += dx
        self.y -= dy

        if self.pen_down:
            pygame.draw.line(self.screen, self.color, (start_x, start_y), (self.x, self.y), 2)

        # Draw line to the new position
        # pygame.draw.line(self.screen, black, (start_x, start_y), (self.x, self.y), 2)

    def left(self, angle):
        # Turn left by adjusting the angle counterclockwise
        self.angle = (self.angle + angle) % 360

class move(Turtle):
    def __init__(self, screen, color: str):
        super().__init__(self, screen, (self.x, self.y))
        self.angle = 0
        self.pencolor = color
    
    def right(self, angle):
        self.left(-angle)

    def pen_color(self, color):
        self.color = color
    
    def pen_up(self):
        self.pen_down = False
    
    def pen_down(self):
        self.pen_down = True


# Main loop

# Initialize Pygame
pygame.init()

# Screen dimensions and setup
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Turtle Style Drawing")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
Blue = (0, 255, 255)

screen.fill(white)
turtle = move(screen, screen.get_width() // 2, screen.get_height() // 2, Blue, (0, 0))  # Start at the center of the screen

turtle.pen_down()
# Draw a square using turtle-style commands
for _ in range(4):
    turtle.forward(100)  # Move forward by 100 pixels
    turtle.left(90)  # Turn left by 90 degrees
 
# Display the drawing
pygame.display.flip()

# Wait to quit
event_loop()

# Quit Pygame
pygame.quit()
