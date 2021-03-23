import cv2
video = cv2.VideoCapture(0)
left=10
top=10
right=110
bottom=110
while(1):
    ret, frame = video.read()
    frame_transformed_to_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #scala di grigi
    cv2.rectangle(frame, (left, top), (right, bottom), (0,0, 255), 3)
    cv2.imshow('Video Modificato',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
       break
video.release()
cv2.destroyAllWindows()
