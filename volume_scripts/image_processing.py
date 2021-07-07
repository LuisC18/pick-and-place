#!/usr/bin/env python

from rectangle_support import *
from color_filter import *
import cv2
import pyrealsense2 as rs
import rospy
import numpy as np

def main():
  try:
		# Configure depth and color streams
		# pipeline = rs.pipeline()
		# config = rs.config()

		# # Get device product line for setting a supporting resolution
		# pipeline_wrapper = rs.pipeline_wrapper(pipeline)
		# pipeline_profile = config.resolve(pipeline_wrapper)
		# device = pipeline_profile.get_device()
		# device_product_line = str(device.get_info(rs.camera_info.product_line))

		# config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

		# if device_product_line == 'L500':
		# 	config.enable_stream(rs.stream.color, 960, 540, rs.format.bgr8, 30)
		# else:
		# 	config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

		# # Starts streaming
		# pipeline.start(config)
		# while True:
		# 	frames = pipeline.wait_for_frames()
		# 	color_frame = frames.get_color_frame()
		# 	if not color_frame:
		# 		continue
		# 	else:
		# 		break

		# color_image = np.asanyarray(color_frame.get_data())
		# cv2.imshow('test',color_image)
		# print(color_image.shape)
		precrop_image1 = cv2.imread("images/black1_Color.png")
		image1 = precrop_image1[60:250, 200:500]

		cv2.imshow('CroppedBlack Box', image1)
		precrop_image2 = cv2.imread("images/background_Color.png")
		image2 = precrop_image2[60:250, 200:500]
		cv2.imshow('Background only', image2)
		image3 = image1 - image2
		cv2.imshow('Subtracted image', image3)

		rospy.sleep(4.5)

		rect = detectRect()

		# cF = colorFilter('images/black8_Color.png')
		cF = colorFilter(image3)

		grayscale_filtered = cF.filterBackground()
		cv2.imshow('Grayscale after color filter',grayscale_filtered)
		raw_input('contours <enter>')

		imgContour,bigCont,boundingBox, pixel_x, pixel_y = rect.getContours(cF.original,grayscale_filtered)
		cv2.imshow('Contours',imgContour)

		drawingFit = cF.original.copy()
		# r ospy.sleep(5)
		# Locates center point
		nPoints= (bigCont)



		#draw centerpoint
		cv2.circle(drawingFit, (pixel_x,pixel_y), 0, (0,0,255), 3)
		print('x center pixel:',pixel_x)
		print('y center pixel:',pixel_y)

		#need pixel to cm conversion
		scale = 66.6/640 #cm/pixel
		centimeter_x = pixel_x * scale
		centimeter_y = pixel_y *scale

		angle, cntr, mean = rect.getOrientation(nPoints, imgContour)
		result_angle = int(np.rad2deg(angle))

		cv2.imshow('Fit',drawingFit)

		print('********* RESULTS ***************')
		print('Angle is ' + str(result_angle) + ' degrees [CW Positive]')
		print('Coordinate of center is (' + str(centimeter_x) + ' , ' + str(centimeter_y) + ') cm')

		cv2.waitKey(0)
		cv2.destroyAllWindows()

  except rospy.ROSInterruptException:
    exit()
  except KeyboardInterrupt:
    exit()

if __name__ == '__main__':
  main()
