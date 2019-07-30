import cv2
import numpy as np
import os

def showcam(mirror=False):
    camera = cv2.VideoCapture(0)

    if (camera.isOpened() == False):
        print("UNABLE TO READ CAMERA")

    frame_width = int(camera.get(3))
    frame_height = int(camera.get(4))

    out = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width, frame_height))
    
    while True:
        retangleValue, img = camera.read()

        if mirror:
            img = cv2.flip(img, 1)

        if retangleValue == True:
            out.write(img)
            rgb = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
            cv2.imshow('WEBCAME', img)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break #ESC untuk keluar
        else:
            break

    camera.release()
    out.release()
    
    cv2.destroyAllWindows()

def main():
    showcam(mirror=True)

if __name__ == '__main__':
    main()
