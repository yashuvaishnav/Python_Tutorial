import pygame
import sys
import random

# Constants for the game
BLOCK_SIZE = 20
GRID_WIDTH = 30  # number of blocks in horizontal direction
GRID_HEIGHT = 30  # number of blocks in vertical direction
SCREEN_WIDTH = BLOCK_SIZE * GRID_WIDTH
SCREEN_HEIGHT = BLOCK_SIZE * GRID_HEIGHT

class Snake:
    def __init__(self):
        # Initialize snake with 3 segments in the center of the screen
        self.body = [
            (GRID_WIDTH // 2, GRID_HEIGHT // 2),
            (GRID_WIDTH // 2 - 1, GRID_HEIGHT // 2),
            (GRID_WIDTH // 2 - 2, GRID_HEIGHT // 2)
        ]
        self.direction = (1, 0)  # Initially moving to the right

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        # Insert new head and remove tail to simulate movement
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        # When eating food, add a new segment by duplicating the tail segment
        self.body.append(self.body[-1])

    def change_direction(self, new_direction):
        # Prevent the snake from reversing directly onto itself
        if (self.direction[0] * -1, self.direction[1] * -1) == new_direction:
            return
        self.direction = new_direction

    def draw(self, surface):
        for segment in self.body:
            rect = pygame.Rect(segment[0] * BLOCK_SIZE,
                               segment[1] * BLOCK_SIZE,
                               BLOCK_SIZE,
                               BLOCK_SIZE)
            pygame.draw.rect(surface, (0, 255, 0), rect)

    def check_self_collision(self):
        head = self.body[0]
        return head in self.body[1:]


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.randomize_position([])

    def randomize_position(self, snake_body):
        # Keep generating a new position until it's not on the snake's body
        while True:
            pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if pos not in snake_body:
                self.position = pos
                break

    def draw(self, surface):
        rect = pygame.Rect(self.position[0] * BLOCK_SIZE,
                           self.position[1] * BLOCK_SIZE,
                           BLOCK_SIZE,
                           BLOCK_SIZE)
        pygame.draw.rect(surface, (255, 0, 0), rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()

    snake = Snake()
    food = Food()
    food.randomize_position(snake.body)

    running = True
    while running:
        clock.tick(10)  # Set game speed (FPS)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((1, 0))

        snake.move()

        # Check for collision with the walls
        head_x, head_y = snake.body[0]
        if head_x < 0 or head_x >= GRID_WIDTH or head_y < 0 or head_y >= GRID_HEIGHT:
            print("Game Over! You hit the wall.")
            running = False

        # Check for self-collision
        if snake.check_self_collision():
            print("Game Over! You ran into yourself.")
            running = False

        # Check if the snake has eaten the food
        if snake.body[0] == food.position:
            snake.grow()
            food.randomize_position(snake.body)

        # Draw everything
        screen.fill((0, 0, 0))  # Clear the screen with black
        snake.draw(screen)
        food.draw(screen)
        pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
