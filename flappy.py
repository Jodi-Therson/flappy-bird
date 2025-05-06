import pygame
import random
import sys
from collections import deque

pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
YELLOW = (255, 255, 0)
BLUE = (70, 197, 206)
BLACK = (0, 0, 0)

FPS = 60
clock = pygame.time.Clock()

FONT = pygame.font.SysFont(None, 48)
SMALL_FONT = pygame.font.SysFont(None, 32)
PIPE_DISTANCE = 250

# Bird class
class Bird:
    def __init__(self, image_path=None):
        self.x = 80
        self.y = HEIGHT // 2
        self.radius = 15
        self.vel = 0
        self.gravity = 0.5
        self.jump_force = -8

        if image_path:
            try:
                self.image = pygame.image.load(image_path).convert_alpha()
                self.image = pygame.transform.scale(self.image, (self.radius * 2, self.radius * 2))
            except:
                print("⚠️ Could not load image, using circle instead.")
                self.image = None
        else:
            self.image = None

    def update(self):
        self.vel += self.gravity
        self.y += self.vel

    def jump(self):
        self.vel = self.jump_force

    def draw(self):
        if self.image:
            rect = self.image.get_rect(center=(int(self.x), int(self.y)))
            WIN.blit(self.image, rect)
            pygame.draw.circle(WIN, YELLOW, (int(self.x), int(self.y)), self.radius, 2)
        else:
            pygame.draw.circle(WIN, YELLOW, (int(self.x), int(self.y)), self.radius)

# Pipe class
class Pipe:
    WIDTH = 60
    GAP = 150
    SPEED = 3

    def __init__(self, x):
        self.x = x
        self.top_height = random.randint(50, HEIGHT - Pipe.GAP - 50)
        self.bottom_y = self.top_height + Pipe.GAP
        self.passed = False

    def update(self):
        self.x -= Pipe.SPEED

    def draw(self):
        pygame.draw.rect(WIN, GREEN, (self.x, 0, Pipe.WIDTH, self.top_height))
        pygame.draw.rect(WIN, GREEN, (self.x, self.bottom_y, Pipe.WIDTH, HEIGHT - self.bottom_y))

    def off_screen(self):
        return self.x + Pipe.WIDTH < 0

    def collides_with(self, bird):
        within_x = bird.x + bird.radius > self.x and bird.x - bird.radius < self.x + Pipe.WIDTH
        hit_top = bird.y - bird.radius < self.top_height
        hit_bottom = bird.y + bird.radius > self.bottom_y
        return within_x and (hit_top or hit_bottom)

# Reset game state
def reset():
    global bird, pipes, score, game_over
    bird = Bird("bird.png")  # Replace with None if you don't want an image
    pipes = deque()
    for i in range(4):
        new_pipe = Pipe(WIDTH + i * PIPE_DISTANCE)
        pipes.append(new_pipe)
        print(f"✅ Added pipe at x={new_pipe.x}")
    score = 0
    game_over = False

# Draw score during gameplay
def draw_score(score):
    text = FONT.render(str(score), True, BLACK)
    rect = text.get_rect(center=(WIDTH // 2, 40))
    WIN.blit(text, rect)

# Draw Game Over screen with high score
def draw_game_over(score, high_score):
    WIN.fill(BLUE)
    game_over_text = FONT.render("Game Over", True, BLACK)
    score_text = SMALL_FONT.render(f"Score: {score}", True, BLACK)
    high_score_text = SMALL_FONT.render(f"High Score: {high_score}", True, BLACK)
    play_again_text = SMALL_FONT.render("Click or press SPACE to play again", True, BLACK)

    WIN.blit(game_over_text, game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 80)))
    WIN.blit(score_text, score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30)))
    WIN.blit(high_score_text, high_score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 10)))
    WIN.blit(play_again_text, play_again_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50)))
    pygame.display.update()

# Main game loop
def main():
    global bird, pipes, score, game_over
    high_score = 0
    reset()
    run = True

    while run:
        clock.tick(FPS)

        if not game_over:
            WIN.fill(BLUE)

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    bird.jump()

            # Update bird
            bird.update()

            # Remove off-screen pipes
            while pipes and pipes[0].off_screen():
                removed = pipes.popleft()
                print(f"🗑️ Removed pipe at x={removed.x}")

            new_pipes = []

            for pipe in pipes:
                pipe.update()

                if pipe.collides_with(bird):
                    game_over = True
                    if score > high_score:
                        high_score = score

                if not pipe.passed and pipe.x + Pipe.WIDTH < bird.x:
                    pipe.passed = True
                    score += 1
                    print(f"🎯 Bird passed pipe at x={pipe.x} — score: {score}")
                    new_pipe = Pipe(pipes[-1].x + PIPE_DISTANCE)
                    new_pipes.append(new_pipe)

            for np in new_pipes:
                pipes.append(np)
                print(f"➕ Queued new pipe at x={np.x}")

            if bird.y + bird.radius >= HEIGHT or bird.y - bird.radius <= 0:
                game_over = True
                if score > high_score:
                    high_score = score

            # Draw elements
            bird.draw()
            for pipe in pipes:
                pipe.draw()
            draw_score(score)
            pygame.display.update()

        else:
            draw_game_over(score, high_score)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    reset()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    reset()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
