import cv2

def showcam(mirror=False):
    camera = cv2.VideoCapture(0)
    while True:
        retangleValue, img = camera.read()

        if mirror:
            img = cv2.flip(img, 1)

        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
        cv2.imshow('WEBCAME', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            out = cv2.imwrite('images.jpg', img)
            break #ESC untuk keluar
        
    cv2.destroyAllWindows()

def main():
    showcam(mirror=True)

if __name__ == '__main__':
    main()
