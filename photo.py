import picamera
camera = picamera.PiCamera()
camera.vflip = True
camera.brightness = 30
camera.contrast = 50
camera.capture('veg.jpg')
camera.start_preview()
