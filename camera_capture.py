import cv2
i=0
def camX():
    i=0
    while(True):
        i+=1
        webcam = cv2.VideoCapture(0)
        check, frame = webcam.read()
        cv2.imwrite('C:/Users/SIRI/Desktop/cap/img_'+(str(i))+'.jpg',frame)
        webcam.release()

camX()
