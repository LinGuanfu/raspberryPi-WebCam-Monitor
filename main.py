from flask import Flask, render_template, Response
from Camera_module import VideoCamera

 
app = Flask(__name__)
 
@app.route('/')
def index():
    
    return render_template('index.html')
 
def pigen(picamerabackup):
    #while True:
    pi_frame = picamerabackup.piget_frame()
    yield (b'--pi_frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + pi_frame + b'\r\n\r\n')

def usbgen(picamerabackup):
    #while True:
    usb_frame = picamerabackup.usbget_frame()
    yield (b'--usb_frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + usb_frame + b'\r\n\r\n')
 
@app.route('/Pi_image')
def Pi_image():
    return Response(pigen(PiVideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=pi_frame')

@app.route('/Usb_image')
def Usb_image():
    return Response(usbgen(PiVideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=usb_frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
