import time
import sys
import os

train = [
    r"     (@@)    ",
    r"   (----)   ",
    r"   (----)   ",
    r"[O==O==O]"
]

def move_train():
    width = os.get_terminal_size().columns  # Get terminal width dynamically
    position = 0  # Start position

    try:
        while True:
            sys.stdout.write("\033[H\033[J")  # Clear screen in a non-flickering way
            spaces = " " * (position % (width - len(train[0])))  # Move within bounds
            
            for line in train:  # Print train with new position
                print(spaces + line)

            sys.stdout.flush()
            time.sleep(0.1)  # Adjust speed
            position += 1  # Move train right
    except KeyboardInterrupt:
        sys.stdout.write("\033[H\033[J")  # Clear screen when stopped
        print("Animation stopped.")

move_train()
