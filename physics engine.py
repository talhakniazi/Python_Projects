import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions and constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAVITY = 0.5
FRICTION = 0.9  # Friction applied to the ball after bouncing
FPS = 60

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Engine - Gravity and Bouncing Ball")
clock = pygame.time.Clock()

# Ball class to handle physics properties
class Ball:
    def __init__(self, x, y, radius=20, color=(0, 128, 255)):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.dx = random.uniform(-5, 5)  # Random horizontal velocity
        self.dy = random.uniform(-5, 5)  # Random vertical velocity

    def apply_gravity(self):
        self.dy += GRAVITY  # Increase the downward velocity by gravity

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def bounce(self):
        # Bounce off the floor
        if self.y + self.radius >= HEIGHT:
            self.y = HEIGHT - self.radius
            self.dy = -self.dy * FRICTION
            self.dx *= FRICTION

        # Bounce off the ceiling
        if self.y - self.radius <= 0:
            self.y = self.radius
            self.dy = -self.dy * FRICTION

        # Bounce off the walls
        if self.x + self.radius >= WIDTH:
            self.x = WIDTH - self.radius
            self.dx = -self.dx * FRICTION
        elif self.x - self.radius <= 0:
            self.x = self.radius
            self.dx = -self.dx * FRICTION

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

def main():
    # Initialize ball object
    ball = Ball(WIDTH // 2, HEIGHT // 2)

    running = True
    while running:
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Apply physics to the ball
        ball.apply_gravity()
        ball.move()
        ball.bounce()
        
        # Draw the ball
        ball.draw()

        # Update display
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
