import mouse
import pyautogui
import random
import time

WIDTH, HEIGHT = pyautogui.size()

# range of time in seconds
WAIT_RANGE = {  
    "start": 0,
    "end": 10
}                

def main():
    done = False

    print(f"""-----
Screen dimensions: {WIDTH} by {HEIGHT}
Press Ctrl+C to quit the app.
-----\n\n""")

    try:
        while not done:
            sleep_time = random.randrange(WAIT_RANGE['start'], WAIT_RANGE['end'])
            print(f"Waiting {sleep_time} seconds...")
            time.sleep(sleep_time)

            x = random.randrange(0, WIDTH)
            y = random.randrange(0, HEIGHT)

            print(f"Moving mouse to ({x}, {y}).")
            mouse.move(x, y, duration=random.randrange(1, 3))
    except KeyboardInterrupt:
        done = True
        print("Quitting.")

if __name__ == "__main__":
    main()

