#!/usr/bin/env python

import pyrealsense2 as rs
import numpy as np
import math
import cv2
import rospy
from std_msgs.msg import *
import geometry_msgs.msg 
from os.path import join



def write():
    print('Creating a new file')
    path = "/home/khan764/ws_Robot/src/pick-and-place/scripts"
    name = 'Depth_data.txt'  # Name of text file coerced with +.txt
    return name, path

def main():
    try: 
        # Configure depth and color streams
        pipeline = rs.pipeline()
        config = rs.config()

        # Get device product line for setting a supporting resolution
        pipeline_wrapper = rs.pipeline_wrapper(pipeline)
        pipeline_profile = config.resolve(pipeline_wrapper)
        device = pipeline_profile.get_device()
        device_product_line = str(device.get_info(rs.camera_info.product_line))

        config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

        if device_product_line == 'L500':
            config.enable_stream(rs.stream.color, 960, 540, rs.format.bgr8, 30)
        else:
            config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

        # Starts streaming
        pipeline.start(config)
        rospy.sleep(2)
        try:
            while True:
                

        frames = pipeline.wait_for_frames()
        depth_frame= frames.get_depth_frame()
        color_frame= frames.get_color_frame()
        #infared_frame= frames.get_infared_frame()
        # if not depth_frame or not color_frame:
        #     continue

        # Converts images to numpy arrays
        depth_image = np.asanyarray(depth_frame.get_data()) #DEPTH DATA

        color_image = np.asanyarray(color_frame.get_data())


        # Applys colormap on depth image (image must be converted to 8-bit per pixel first)
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

        #finds dimensions of arrays(resolution)
        depth_colormap_dim = depth_colormap.shape
        color_colormap_dim = color_image.shape

        # If depth and color resolutions are different, resize color image to match depth image for display
        if depth_colormap_dim != color_colormap_dim:
            resized_color_image = cv2.resize(color_image, dsize=(depth_colormap_dim[1], depth_colormap_dim[0]),
                                             interpolation=cv2.INTER_AREA)
            images = np.hstack((resized_color_image, depth_colormap))
        else:
            images = np.hstack((color_image, depth_colormap))

        # Show images
        cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
        img_color = depth_colormap.copy()
        cv2.imshow(img_color)

        print(depth_colormap)
        name, path = write()
        file = open(join(path, name),'w')   # Trying to create a new file or open one
        file.write(depth_colormap)
        file.close()
        print('wrote to file')

    except rospy.ROSInterruptException:
      exit()
    except KeyboardInterrupt:
      exit()


if __name__ == '__main__':
  main()
