#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import os
# os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
import cv2 as cv
#import pymf 

import site
import sys


def find_cameras():
    # site.addsitedir('')  # Always appends to end
    # print(sys.path)
    # # MSMF version using pymf
    # device_list = pymf.get_MF_devices()
    # for i, device_name in enumerate(device_list):
    #     print(f"opencv_index: {i}, device_name: {device_name}")
    #list APIs
    backends = cv.videoio_registry.getCameraBackends()
    for i in backends:
        print(cv.videoio_registry.getBackendName(i)) 
    # Test the ports and returns a tuple with the available ports and the ones that are working.
    camera_port = 0
    non_working_ports = []
    working_ports = []
    available_ports = []
    
    while len(non_working_ports) < 3: # if there are more than 5 non working ports stop the testing. 
        camera = cv.VideoCapture(camera_port, cv.CAP_DSHOW)
        if not camera.isOpened():
            non_working_ports.append(camera_port)
            print("Port %s is not working." %camera_port)
        else:
            is_reading, img = camera.read()
            w = camera.get(cv.CAP_PROP_FRAME_WIDTH)
            h = camera.get(cv.CAP_PROP_FRAME_HEIGHT)
            f = camera.get(cv.CAP_PROP_FPS)
            if is_reading:
                print("Port %s is working and reads images (%s x %s) at %s fps" %(camera_port,h,w,f))
                working_ports.append(camera_port)
            else:
                print("Port %s for camera ( %s x %s) is present but does not reads." %(camera_port,h,w))
                available_ports.append(camera_port)
        camera_port +=1
        # per the docs, the camera will be deinitialized automatically in VideoCapture destructor or on subsequent call
    return available_ports,working_ports,non_working_ports