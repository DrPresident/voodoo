#!/usr/bin/env python3

import curses


def main(scr):
    while True:
        scr.clear()

        scr.refresh()

if __name__ == '__main_':
    curses.wrapper(main)
