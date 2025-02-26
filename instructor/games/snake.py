import curses
import random

def main(stdscr):
    # Turn off cursor blinking
    curses.curs_set(0)
    # Get the size of the terminal window
    sh, sw = stdscr.getmaxyx()
    
    # Create a new window for the game
    # We'll use the full window size for simplicity
    win = curses.newwin(sh, sw, 0, 0)
    win.keypad(True)         # Enable keypad for arrow keys
    win.timeout(100)         # Game speed: lower value = faster
    
    # Initial snake coordinates (center of screen)
    snake_y = sh // 2
    snake_x = sw // 4
    snake = [
        (snake_y, snake_x),
        (snake_y, snake_x - 1),
        (snake_y, snake_x - 2)
    ]
    
    # Initial food coordinates
    food = (sh // 2, sw // 2)
    win.addch(food[0], food[1], '#')
    
    # Initial direction (going right)
    key = curses.KEY_RIGHT
    
    while True:
        # Get the next key pressed
        next_key = win.getch()
        # If no key is pressed, keep the same direction
        key = key if next_key == -1 else next_key
        
        # Calculate the new head of the snake based on the direction
        head_y, head_x = snake[0]
        if key == curses.KEY_DOWN:
            head_y += 1
        elif key == curses.KEY_UP:
            head_y -= 1
        elif key == curses.KEY_LEFT:
            head_x -= 1
        elif key == curses.KEY_RIGHT:
            head_x += 1
        
        # Insert the new head to the beginning of the snake list
        snake.insert(0, (head_y, head_x))
        
        # Check if snake collides with the border
        if (head_x == 0 or head_x == sw-1 or 
            head_y == 0 or head_y == sh-1):
            # Game over condition
            break
        
        # Check if snake runs over itself
        if (head_y, head_x) in snake[1:]:
            # Game over condition
            break
        
        # Check if snake eats the food
        if (head_y, head_x) == food:
            # Generate a new food location
            while True:
                new_food = (
                    random.randint(1, sh - 2),
                    random.randint(1, sw - 2)
                )
                # Make sure the new food isn't on the snake
                if new_food not in snake:
                    food = new_food
                    break
            win.addch(food[0], food[1], '#')
        else:
            # Remove the tail (since we didn't eat anything)
            tail = snake.pop()
            win.addch(tail[0], tail[1], ' ')
        
        # Draw the snake's head
        win.addch(snake[0][0], snake[0][1], 'O')
        # Optionally draw the snake's body
        if len(snake) > 1:
            # 'o' for the rest of the body
            for y, x in snake[1:]:
                win.addch(y, x, 'o')

def run_snake_game():
    curses.wrapper(main)

if __name__ == "__main__":
    run_snake_game()
