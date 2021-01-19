#python3

import pyautogui as pgui
import numpy as np
import time
import argparse

if __name__ == "__main__":
    #params
    parser = argparse.ArgumentParser(description="You can set mouse move inverval second by --interval.")
    parser.add_argument("--interval", help="move interval time(second)", default=60*3, type=int)
    args = vars(parser.parse_args())
    print("Let's start moving by %s second. If you want to stop, push CTRL + C."%args["interval"])
    #interval_second = 6

    #fetch window params
    width, _ = pgui.size()
    move_x_list = [width*4/10, width*6/10]
    _, y_pos = pgui.position()

    #absolute #relative pgui.moveRel
    t = 0
    while True:
        pgui.click()
        pgui.moveTo(move_x_list[t%len(move_x_list)], y_pos, duration=1)
        t += 1
        time.sleep(args["interval"])