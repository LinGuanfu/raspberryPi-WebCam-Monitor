# camera.py
import cv2
import time
import threading
 
class VideoCamera(object):
    thread = None  # background thread that reads frames from camera
    pijpeg = None  # current frame is stored here by background thread
    usbjpeg = None  # current frame is stored here by background thread
    last_access = 0  # time of last client access to the camera

    def initialize(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        if VideoCamera.thread is None:
            # start background frame thread
            VideoCamera.thread = threading.Thread(target=self._thread)
            VideoCamera.thread.start()
            
            while self.pijpeg is None:
                time.sleep(0)
            while self.usbjpeg is None:
                time.sleep(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
    
    def piget_frame(self):
        VideoCamera.last_access = time.time()
        self.initialize()
        return self.pijpeg.tobytes()
    
    def usbget_frame(self):
        VideoCamera.last_access = time.time()
        self.initialize()
        return self.usbjpeg.tobytes()

    @classmethod
    def _thread(cls):
        cls.pi = cv2.VideoCapture(0)
        cls.pi.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cls.pi.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) #设置分辨率
        cls.usb = cv2.VideoCapture(1)
        cls.usb.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cls.usb.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) #设置分辨率
        
        while True:
            ret,piimage = cls.pi.read()
            sus,usbimage = cls.usb.read()
            # We are using Motion JPEG, but OpenCV defaults to capture raw images,
            # so we must encode it into JPEG in order to correctly display the
            # video stream.
            if ret == True:
                _,cls.pijpeg = cv2.imencode('.jpg', piimage)
            if sus == True:
                _,cls.usbjpeg = cv2.imencode('.jpg', usbimage)
            # if there hasn't been any clients asking for frames in
            # the last 10 seconds stop the thread
            if time.time() - cls.last_access > 10:
                cls.pi.release()
                cls.usb.release()
                break
    # 对于 python2.7 或者低版本的 numpy 请使用 jpeg.tostring()
        cls.thread = None