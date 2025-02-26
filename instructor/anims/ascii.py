import time
import sys
import os

fish_frames = [">))'>", " >))'>", "  >))'>", "   >))'>"]

def hide_cursor():
    sys.stdout.write("\033[?25l")  # Hide cursor
    sys.stdout.flush()

def show_cursor():
    sys.stdout.write("\033[?25h")  # Show cursor when exiting
    sys.stdout.flush()

def move_fish():
    width = os.get_terminal_size().columns  # Get terminal width dynamically
    position = 0  # Start position

    try:
        hide_cursor()
        while True:
            sys.stdout.write("\033[H\033[J")  # Clear screen without flickering
            spaces = " " * (position % (width - len(fish_frames[0])))  # Keep within screen bounds
            print(spaces + fish_frames[position % len(fish_frames)])  # Print fish
            sys.stdout.flush()
            time.sleep(0.1)  # Adjust speed
            position += 1  # Move fish right
    except KeyboardInterrupt:
        show_cursor()
        sys.stdout.write("\033[H\033[J")  # Clear screen when stopped
        print("Animation stopped.")

move_fish()
