import time
import colorconsole.terminal
text = open(r"text1.txt", "r")
frame = ""
size = (236, 61)
for line_count, line in enumerate(text, start=1):
    frame = frame + line
    if line_count % size[1] == 0:
        print(frame)
        frame = ""
        time.sleep(0.0278) # interval per frame
        colorconsole.terminal.get_terminal().gotoXY(0,0)