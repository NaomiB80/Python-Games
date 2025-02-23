"""

Moving Square

All this game does is move a square around the screen using the arrow keys.
The square is constrained to the screen, so it can't go off the edges. 

"""
import pygame

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
CIRCLE_RADIUS = 50
CIRCLE_COLOR = (0, 128, 255) # Red-Green-Blue color in the range 0-255
BACKGROUND_COLOR = (255, 255, 255) # White
CIRCLE_SPEED = 5
FPS = 60

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Move the Square")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Main function
def main():
    # Initial position of the square
    circle_x = SCREEN_WIDTH // 2 - CIRCLE_RADIUS // 2
    circle_y = SCREEN_HEIGHT // 2 - CIRCLE_RADIUS // 2
    
    running = True
    
    while running:
        

        # Event handling
        for event in pygame.event.get():
            
            # Check for clicking the close button
            if event.type == pygame.QUIT:
                running = False
        
        # Get the keys pressed. Gets an array of all the keys
        # with a boolean value of whether they are pressed or not
        keys = pygame.key.get_pressed()

        # Move the square based on arrow keys 
        if keys[pygame.K_a]:
            circle_x -= CIRCLE_SPEED
        if keys[pygame.K_d]:
            circle_x += CIRCLE_SPEED
        if keys[pygame.K_w]:
            circle_y -= CIRCLE_SPEED
        if keys[pygame.K_s]:
            circle_y += CIRCLE_SPEED

        # Prevent the square from going off the screen
        circle_x = max(0, min(SCREEN_WIDTH - CIRCLE_RADIUS, circle_x))
        circle_y = max(0, min(SCREEN_HEIGHT - CIRCLE_RADIUS, circle_y))

        # This will clear the screen by filling it 
        # with the background color. If we didn't do this, 
        # the square would leave a trail behind it.
        screen.fill(BACKGROUND_COLOR)

        # Draw the square
        pygame.draw.circle(screen, CIRCLE_COLOR, (circle_x, circle_y), CIRCLE_RADIUS, width=0, draw_top_right=True, draw_top_left=True, draw_bottom_left=True, draw_bottom_right=True)

        # Update the display. Imagine that the screen is two different whiteboards. One
        # whiteboard is currently visible to the player, and the other whiteboard is being
        # drawn on. When you call pygame.display.flip(), it's like taking the whiteboard
        # that was being drawn on and showing it to the player, while taking the whiteboard
        # that was visible to the player and giving it to the artist to draw on. This makes
        # it so that the player never sees the drawing process, only the final result.
        pygame.display.flip()

        # Cap the frame rate. This makes the game run at a consistent speed on all computers.
        clock.tick(FPS)

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
