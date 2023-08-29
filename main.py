from pynput.mouse import Listener
import logging
import time

logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

def on_move(x, y):
    print(x, y)


def on_click(x, y, button, pressed):
    logging.info(str(button))
    print(x, y, button, pressed)


def on_scroll(x, y, dx, dy):
    print(x, y, dx, dy)


if __name__ == "__main__": 
    print("Waiting 20 seconds before starting")
    time.sleep(20)
    with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()