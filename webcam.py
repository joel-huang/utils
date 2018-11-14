import cv2

def show_webcam(mirror=False, square=False):
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        if mirror: 
            img = cv2.flip(img, 1)
        if square:
            img = cv2.resize(img, (342, 256))
            img = crop_square(img, px=512)
        cv2.imshow('my webcam', img)
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    cv2.destroyAllWindows()

def crop_square(img, px):
    h, w, ch = img.shape
    return img[int(h-(px/2)):int(h+(px/2)),int(w-(px/2)):int(w+(px/2))]

