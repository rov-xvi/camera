import cv2

def showcam(mirror=False):
    camera = cv2.VideoCapture(0)
    while True:
        retangleValue, img = camera.read()
        if mirror:
            img = cv2.flip(img, 1)
        cv2.imshow('WEBCAME', img)
        if cv2.waitKey(1) == 27:
            break #ESC untuk keluar
    cv2.destroyAllWindows()

def main():
    showcam(mirror=True)

if __name__ == '__main__':
    main()
