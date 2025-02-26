import curses
import random

def main(stdscr):
    curses.curs_set(0)       # Turn off cursor visibility
    stdscr.nodelay(True)     # Don't block I/O calls
    sh, sw = stdscr.getmaxyx()

    # Create a game window (same size as the terminal)
    win = curses.newwin(sh, sw, 0, 0)
    win.keypad(True)
    win.timeout(120)         # Controls the game speed

    # Game variables
    score = 0
    is_paused = False

    # Define the walls (static example: a horizontal wall somewhere)
    # You can add more walls or get creative with shapes.
    walls = []
    wall_y = sh // 3
    for x in range(sw // 4, (3 * sw) // 4):
        walls.append((wall_y, x))

    # Draw all walls on the window
    for wy, wx in walls:
        if 0 < wy < sh-1 and 0 < wx < sw-1:
            win.addch(wy, wx, 'X')

    # Helper function to display the scoreboard and instructions at the top
    def draw_scoreboard():
        # Clear the first row
        win.move(0, 0)
        win.clrtoeol()
        # Print score and instructions
        msg = f"Score: {score} | Press 'P' to Pause/Resume, 'Q' to Quit"
        # Make sure we don't write beyond screen width
        if len(msg) < sw - 2:
            win.addstr(0, 2, msg, curses.A_BOLD)

    # Initial snake setup (start near the center)
    snake_y = sh // 2
    snake_x = sw // 4
    snake = [
        (snake_y, snake_x),
        (snake_y, snake_x - 1),
        (snake_y, snake_x - 2)
    ]
    
    # Place initial food
    def place_food():
        """Return a random coordinate for new food that is not on the snake or a wall."""
        while True:
            fy = random.randint(1, sh - 2)
            fx = random.randint(1, sw - 2)
            if (fy, fx) not in snake and (fy, fx) not in walls:
                return (fy, fx)
    food = place_food()
    win.addch(food[0], food[1], '#')

    # Initial direction (right)
    key = curses.KEY_RIGHT
    
    while True:
        draw_scoreboard()

        # If paused, show paused message on screen
        if is_paused:
            pause_msg = "PAUSED - Press 'P' to Resume"
            # Show it near the center of the screen
            pause_y = sh // 2
            pause_x = max(0, (sw // 2) - (len(pause_msg) // 2))
            win.addstr(pause_y, pause_x, pause_msg, curses.A_REVERSE)

        next_key = win.getch()

        # Handle quit
        if next_key in [ord('q'), ord('Q')]:
            break

        # Handle pause toggle
        if next_key in [ord('p'), ord('P')]:
            is_paused = not is_paused
            if not is_paused:
                # Clear paused message area by re-drawing that line
                win.move(sh // 2, 0)
                win.clrtoeol()
            continue  # Skip movement/update if we just toggled pause

        if not is_paused:
            # If a valid arrow key is pressed, update direction
            if next_key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
                key = next_key

            # Calculate the new head of the snake
            head_y, head_x = snake[0]
            if key == curses.KEY_DOWN:
                head_y += 1
            elif key == curses.KEY_UP:
                head_y -= 1
            elif key == curses.KEY_LEFT:
                head_x -= 1
            elif key == curses.KEY_RIGHT:
                head_x += 1

            # Insert new head
            snake.insert(0, (head_y, head_x))

            # Check collision with borders
            if head_y == 0 or head_y == sh-1 or head_x == 0 or head_x == sw-1:
                # Game over
                break

            # Check collision with itself
            if (head_y, head_x) in snake[1:]:
                # Game over
                break

            # Check collision with walls
            if (head_y, head_x) in walls:
                # Game over
                break

            # Check if snake eats the food
            if (head_y, head_x) == food:
                score += 1
                # Place new food
                food = place_food()
                win.addch(food[0], food[1], '#')
            else:
                # Remove the tail
                tail = snake.pop()
                win.addch(tail[0], tail[1], ' ')

            # Draw the new head
            win.addch(snake[0][0], snake[0][1], 'O')
            # Draw the body
            if len(snake) > 1:
                for y, x in snake[1:]:
                    win.addch(y, x, 'o')

    # End of game screen
    win.nodelay(False)  # Allow blocking for final message
    win.clear()
    end_msg = f"Game Over! Final Score: {score}"
    win.addstr(sh // 2, (sw // 2) - (len(end_msg) // 2), end_msg, curses.A_BOLD)
    win.addstr(sh // 2 + 1, (sw // 2) - 10, "Press any key to exit.", curses.A_DIM)
    win.getch()

def run_snake_game():
    curses.wrapper(main)

if __name__ == "__main__":
    run_snake_game()
