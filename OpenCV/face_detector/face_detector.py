import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread("news.jpg")
gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert bgr image to grey

faces = face_cascade.detectMultiScale(gray_img,
scaleFactor=1.1,
minNeighbors=5)

for x, y, w, h in faces:
    # img - our image
    # (x, y) - start point of the rectangle
    # (x + w, y + h) - end point of the rectangle
    # (0, 255, 0) - color, green in this case
    # 3 - width
    img=cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 3)

print(type(faces))
print(faces)

resized = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

cv2.imshow("Gray", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
