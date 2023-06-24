#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import dearpygui.dearpygui as dpg


from pyCameraController import CameraController
from pyCameraWindow import CameraWindow
from pyCameraCheck import find_cameras

if __name__ == "__main__":
    #If not seeing any camera output, change the 1 below to 0, 2, 3, etc.
    #This could probably be automated or a user-select added.
    # Uncomment the next line to try to see what could be a valid index. 
    find_cameras()
    print ("Write the camera output PORT NUMBER and hit ENTER. It should be 1 if integrated webcam is present or 0, 2, 3, etc.")
    camNum = int(input())
    cc = CameraController(camNum)
    dpg.create_context()
    dpg.create_viewport(title='PyReflectorCollimator', width=1800, height=800)
    dpg.setup_dearpygui()

    cc.create_window()

    cw = CameraWindow(cc)
    print ("Initialized")


    dpg.show_metrics()
    dpg.show_viewport()
    while dpg.is_dearpygui_running():
        cw.update_frame()
        dpg.render_dearpygui_frame()
    


    cc.vid.release()
    #cv.destroyAllWindows() # when using upen cv window "imshow" call this also
    dpg.destroy_context()

