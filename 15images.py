import time
import picamera
with picamera.PiCamera() as camera:
    camera.vflip = True
    camera.hflip = True

    camera.start_preview()
    try:
        for i, filename in enumerate(camera.capture_continuous('seed3image{counter:02d}.jpg')):
            print(filename)
            time.sleep(300)
            if i == 15:
                break
    finally:
        camera.stop_preview()
#taken from chap10
