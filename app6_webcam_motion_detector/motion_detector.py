import cv2, time, pandas
from datetime import datetime

first_frame = None
status_list = [None, None]
times = []
df = pandas.DataFrame(columns=["Start", "End"])

video=cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    if check == False:
        break

    status = 0

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convert image to gray
    gray = cv2.GaussianBlur(gray, (21,21), 0) # blur the image

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray) # find delta between first_frame (greyed blured) and greyed blured current frame image
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1] # if on delta_frame difference is greater than 30 then mark this pixel as white 255
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2) # dilate (increase) white area

    (_,cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # find conturs of the white areas on the frame

    # filter out conturs where white areas are less than 10000
    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status = 1
        (x, y, w, h) = cv2.boundingRect(contour) #parameters of the rectange bound the contour
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 3) #draw this rectangle on the frame

    status_list.append(status)

    status_list = status_list[-2];

    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())

    cv2.imshow("Gray frame", gray)
    cv2.imshow("Delta frame", delta_frame)
    cv2.imshow("Threshhold frame", thresh_frame)
    cv2.imshow("Color frame", frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break

for t in range(0, len(times), 2): # 2 is step
    df = df.append({"Start":times[t],"End":times[t+1]}, ignore_index=True)

df.to_csv("Times.csv")

video.release()
cv2.destroyAllWindows()
