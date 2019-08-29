# **Bubble Detector** 
## Purpose
Project using OpenCV and potentially darknet/yoloV2 in Python to track and count bubbles in a tube. 

**Hardware Required:**
* Raspberry Pi 2/3 B/B+
* PiCamera V2.1
* Neopixel LED strips
* 74AHCT125 level shifting chip
* box
* tube of bubbles

**Packages/Programs:**
* OpenCV
* fswebcam
* Python 2 & 3
* NeoPixel library (instructions [here](https://www.raspberrypi.org/magpi/neopixels-python/) and more [here](https://thepihut.com/blogs/raspberry-pi-tutorials/using-neopixels-with-the-raspberry-pi))
* picamera
* matplotlib: use `sudo apt-get install python-matplotlib` for your Pi 
* darknet
* YOLOv2
* rpi_ws281x
* [adafruit-circuitpython-neopixel](https://learn.adafruit.com/adafruit-neopixel-uberguide/python-circuitpython)

## References
* [YOLOv2 Tutorial](https://timebutt.github.io/static/how-to-train-yolov2-to-detect-custom-objects/)
* [darknet](https://github.com/AlexeyAB/darknet.git)
* [Image Label Tool](https://github.com/puzzledqs/BBox-Label-Tool)
* [NeoPixel Setup on RasPi](https://learn.adafruit.com/neopixels-on-raspberry-pi/raspberry-pi-wiring)
* [NeoPixel Library](https://github.com/jgarff/rpi_ws281x)
