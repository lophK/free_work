from flask import Flask
#import camera_capture as CM
import cv2
app = Flask(__name__)

def camX():
    i=0
    
    while(True):
        i+=1
        webcam = cv2.VideoCapture(0)
        check, frame = webcam.read()
        cv2.imwrite('C:/Users/SIRI/Desktop/cap/img_'+(str(i))+'.jpg',frame)
        webcam.release()


@app.route("/")
def home():
    camX()
    print("Content-type:text/html\n")
    print("<h1>This is the Home Page</h1>")
##    return "homepage<h1>TEST<h1>"

if __name__=="__main__":
    app.run()
##    home()
    




