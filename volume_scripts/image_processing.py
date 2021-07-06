#!/usr/bin/env python

from rectangle_support import *
from color_filter import *
import cv2

def main():
  try:
		rect = detectRect()
		cF = colorFilter('images/Realsense.jpg')

		grayscale_filtered = cF.filterBackground()
		cv2.imshow('Grayscale after color filter',grayscale_filtered)

		imgContour,bigCont,boundingBox, pixel_x, pixel_y = rect.getContours(cF.original,grayscale_filtered)
		cv2.imshow('Contours',imgContour)

		drawingFit = cF.original.copy()

		# Locates center point
		nPoints= (bigCont)

		
		
		#draw centerpoint
		cv2.circle(drawingFit, (pixel_x,pixel_y), 0, (0,0,255), 3)
		print('x center pixel:',pixel_x)
		print('y center pixel:',pixel_y)

		#need pixel to cm conversion
		scale = 1
		centimeter_x = pixel_x * scale
		centimeter_y = pixel_y *scale

		angle, cntr, mean = rect.getOrientation(nPoints, imgContour)
		#result_angle = int(np.rad2deg(angle))

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