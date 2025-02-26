import pygame
import sys
import random

# --- Game Constants ---
CELL_SIZE = 24

# A simple maze layout:
#   '#' = wall
#   '.' = pellet
#   ' ' = empty space
maze_layout = [
    "####################",
    "#........#.........#",
    "#.#######.#######..#",
    "#..................#",
    "#.####.#.####.#.####",
    "#......#....#......#",
    "####################"
]

# --- Maze Class ---
class Maze:
    def __init__(self, layout, cell_size):
        self.cell_size = cell_size
        # Convert each string row into a list so we can modify pellets as they're eaten
        self.grid = [list(row) for row in layout]
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

    def draw(self, surface):
        for y in range(self.rows):
            for x in range(self.cols):
                rect = pygame.Rect(x * self.cell_size, y * self.cell_size,
                                   self.cell_size, self.cell_size)
                if self.grid[y][x] == '#':
                    # Draw walls as blue blocks
                    pygame.draw.rect(surface, (0, 0, 255), rect)
                elif self.grid[y][x] == '.':
                    # Draw pellets as small white circles
                    pellet_radius = self.cell_size // 6
                    center = (x * self.cell_size + self.cell_size // 2,
                              y * self.cell_size + self.cell_size // 2)
                    pygame.draw.circle(surface, (255, 255, 255), center, pellet_radius)

    def is_wall(self, x, y):
        # Out-of-bound positions are considered walls.
        if x < 0 or x >= self.cols or y < 0 or y >= self.rows:
            return True
        return self.grid[y][x] == '#'

    def eat_pellet(self, x, y):
        # Remove pellet if present.
        if self.grid[y][x] == '.':
            self.grid[y][x] = ' '
            return True
        return False

# --- Pacman Class ---
class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # Direction as (dx, dy); initially stationary.
        self.direction = (0, 0)

    def update(self, maze):
        # Calculate the new cell position.
        new_x = self.x + self.direction[0]
        new_y = self.y + self.direction[1]
        # Move only if the target cell is not a wall.
        if not maze.is_wall(new_x, new_y):
            self.x = new_x
            self.y = new_y
            # Return True if a pellet was eaten.
            return maze.eat_pellet(self.x, self.y)
        return False

    def draw(self, surface, cell_size):
        center = (self.x * cell_size + cell_size // 2,
                  self.y * cell_size + cell_size // 2)
        # Draw Pacman as a yellow circle.
        pygame.draw.circle(surface, (255, 255, 0), center, cell_size // 2 - 2)

# --- Ghost Class ---
class Ghost:
    def __init__(self, x, y, color=(255, 0, 0)):
        self.x = x
        self.y = y
        # Choose an initial random direction.
        self.direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        self.color = color

    def update(self, maze):
        # Attempt to move in the current direction.
        new_x = self.x + self.direction[0]
        new_y = self.y + self.direction[1]
        if maze.is_wall(new_x, new_y):
            # If a wall is encountered, compile a list of valid moves.
            valid_moves = []
            for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx = self.x + d[0]
                ny = self.y + d[1]
                if not maze.is_wall(nx, ny):
                    valid_moves.append(d)
            if valid_moves:
                self.direction = random.choice(valid_moves)
        else:
            self.x = new_x
            self.y = new_y

    def draw(self, surface, cell_size):
        center = (self.x * cell_size + cell_size // 2,
                  self.y * cell_size + cell_size // 2)
        # Draw the ghost as a circle.
        pygame.draw.circle(surface, self.color, center, cell_size // 2 - 2)

# --- Game Class ---
class Game:
    def __init__(self):
        pygame.init()
        self.maze = Maze(maze_layout, CELL_SIZE)
        self.width = self.maze.cols * CELL_SIZE
        self.height = self.maze.rows * CELL_SIZE
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pacman")
        self.clock = pygame.time.Clock()
        # Start Pacman at (1, 1) (ensure this is not a wall).
        self.pacman = Pacman(1, 1)
        # Create one ghost positioned at the bottom-right (adjust as needed).
        self.ghosts = [Ghost(self.maze.cols - 2, self.maze.rows - 2)]
        self.score = 0
        self.font = pygame.font.SysFont("Arial", 18)
        self.game_over = False

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Change Pacman's direction with arrow keys.
                if event.key == pygame.K_UP:
                    self.pacman.direction = (0, -1)
                elif event.key == pygame.K_DOWN:
                    self.pacman.direction = (0, 1)
                elif event.key == pygame.K_LEFT:
                    self.pacman.direction = (-1, 0)
                elif event.key == pygame.K_RIGHT:
                    self.pacman.direction = (1, 0)

    def update(self):
        if not self.game_over:
            # Update Pacman and increase score if a pellet is eaten.
            if self.pacman.update(self.maze):
                self.score += 10
            # Update all ghosts.
            for ghost in self.ghosts:
                ghost.update(self.maze)
            # Check for collisions between Pacman and any ghost.
            for ghost in self.ghosts:
                if ghost.x == self.pacman.x and ghost.y == self.pacman.y:
                    self.game_over = True

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.maze.draw(self.screen)
        self.pacman.draw(self.screen, CELL_SIZE)
        for ghost in self.ghosts:
            ghost.draw(self.screen, CELL_SIZE)
        # Display the current score.
        score_text = self.font.render("Score: " + str(self.score), True, (255, 255, 255))
        self.screen.blit(score_text, (5, 5))
        # If the game is over, display a Game Over message.
        if self.game_over:
            game_over_text = self.font.render("Game Over!", True, (255, 0, 0))
            self.screen.blit(game_over_text, (self.width // 2 - 50, self.height // 2))
        pygame.display.flip()

    def run(self):
        while True:
            self.clock.tick(10)  # 10 frames per second
            self.process_events()
            self.update()
            self.draw()

if __name__ == "__main__":
    Game().run()
