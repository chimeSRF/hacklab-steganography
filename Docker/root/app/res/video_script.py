import cv2

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break

    #Note to self: The colors seem interesting