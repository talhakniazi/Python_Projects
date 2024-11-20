import pygame
import random
import math

# Initialize pygame and the mixer for sound
pygame.init()
pygame.mixer.init()

# Screen dimensions
WIDTH = 1550
HEIGHT = 800

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load and play background music
pygame.mixer.music.load("C:/Python Programming/Projects/Self Ideas/LIFE GOES ON - aleemrk (Official Audio)(MP3_160K).mp3")  # Replace with your sound file
pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Generative Art")

# Initialize clock to control the frame rate
clock = pygame.time.Clock()

# Function to draw random circles
def draw_random_circles():
    for _ in range(random.randint(5, 20)):  # Random number of circles
        radius = random.randint(10, 100)
        x = random.randint(radius, WIDTH - radius)
        y = random.randint(radius, HEIGHT - radius)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.circle(screen, color, (x, y), radius)

# Function to draw random lines
def draw_random_lines():
    for _ in range(random.randint(5, 15)):  # Random number of lines
        x1 = random.randint(0, WIDTH)
        y1 = random.randint(0, HEIGHT)
        x2 = random.randint(0, WIDTH)
        y2 = random.randint(0, HEIGHT)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.line(screen, color, (x1, y1), (x2, y2), random.randint(1, 5))

# Function to draw random polygons
def draw_random_polygons():
    for _ in range(random.randint(5, 10)):  # Random number of polygons
        num_sides = random.randint(3, 6)  # Triangles to hexagons
        points = []
        for _ in range(num_sides):
            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)
            points.append((x, y))
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.polygon(screen, color, points)

# Function to draw random curves
def draw_random_curves():
    for _ in range(random.randint(1, 3)):  # Random number of curves
        start_x = random.randint(0, WIDTH)
        start_y = random.randint(0, HEIGHT)
        control_x = random.randint(0, WIDTH)
        control_y = random.randint(0, HEIGHT)
        end_x = random.randint(0, WIDTH)
        end_y = random.randint(0, HEIGHT)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.aaline(screen, color, (start_x, start_y), (control_x, control_y), 5)
        pygame.draw.aaline(screen, color, (control_x, control_y), (end_x, end_y), 5)

# Main loop
running = True
while running:
    screen.fill(BLACK)  # Fill the screen with black

    # Draw random shapes
    draw_random_circles()
    draw_random_lines()
    draw_random_polygons()
    draw_random_curves()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the screen
    pygame.display.flip()

    # Control the frame rate (e.g., 30 frames per second)
    clock.tick(30)

# Stop the music and quit pygame
pygame.mixer.music.stop()
pygame.quit()
