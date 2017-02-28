import time
import colorconsole.terminal
text = open(r"text1.txt", "r")
size = (236, 61)
line_count = 1
frame = ""
for line in text:
    frame = frame + line
    if line_count % size[1] == 0:
        print(frame)
        frame = ""
        time.sleep(0.0278) # interval per frame
        colorconsole.terminal.get_terminal().gotoXY(0,0)
    line_count += 1