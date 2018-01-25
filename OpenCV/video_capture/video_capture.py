import cv2, time

video=cv2.VideoCapture(0)

a=0

while True:
    check, frame = video.read()

    if check == False:
        break

    a=a+1

    cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Capturing", frame)

    cv2.waitKey(1)

    if key==ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows()
