import numpy as np
import cv2
from PIL import Image

def video_to_frame(videofile):
    video_cap = cv2.VideoCapture(videofile)
    frame_count = 0
    while (video_cap.isOpened()):
        print('frame %d' % frame_count)
        ret, frame = video_cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("frame%d.png" % frame_count, frame)
        frame_count += 1
    return frame_count

def resize_frame(img):
    frame = Image.open(img, 'r').convert("L")
    frame = frame.resize(size)
    return frame

def frame_to_char(frame_num):
    gray_char=['@','#','$','%','&','?','*','o','/','{','[','(',
               '|','!','^','~','-','_',':',';',',','.','`',' ']
    count=len(gray_char)
    text = open("text1.txt", "w")
    for i in range(frame_num):
        frame = resize_frame('frame%d.png' % i)
        for y in range(size[1]):
            for x in range(size[0]):
                gray = frame.getpixel((x,y))
                char = gray_char[int(gray/(255/(count-1)))]
                text.write(char)
            text.write("\n")
        print("writing frame %d"%i)
    text.close()
    print('Done!')

if __name__ == '__main__':
    size = (236, 61) #size of output frame
    nframe = video_to_frame('maid.flv') #video to convert
    frame_to_char(nframe)