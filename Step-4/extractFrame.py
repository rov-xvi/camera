import cv2
import numpy as np
import os

def extractFrame(pathIn, pathOut):
    os.mkdir(pathOut)

    captures = cv2.VideoCapture(pathIn)
    count = 0

    while(captures.isOpened()):
        ret, frame = captures.read()

        if ret == True:
            print('Read %d frame : ' % count, ret)
            cv2.imwrite(os.path.join(pathOut, "frame{:d}.jpg".format(count)), frame)
            count += 1
        else:
            break
    captures.release()
    cv2.destroyAllWindows()

def main():
    extractFrame('video.avi', 'data')

if __name__ == '__main__':
    main()
