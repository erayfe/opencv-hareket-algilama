#https://github.com/erayfe

import cv2

kamera = cv2.VideoCapture(0)
ret, kare1 = kamera.read()
ret, kare2 = kamera.read()

while kamera.isOpened():
    fark = cv2.absdiff(kare1,kare2)
    gri = cv2.cvtColor(fark, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gri, 20, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) < 100:
            continue
        cv2.rectangle(kare1, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.putText(kare1, "HAREKET ALGILANDI", (10, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 3)

    cv2.imshow("Hareket Algilama",kare1)
    cv2.imshow("Thresh",thresh)
    kare1 = kare2
    ret, kare2 = kamera.read()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

kamera.release(); cv2.waitKey(0); cv2.destroyAllWindows()