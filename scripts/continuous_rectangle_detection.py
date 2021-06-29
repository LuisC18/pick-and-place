#!/usr/bin/env python

import pyrealsense2 as rs
import numpy as np
import math
import cv2
import rospy
from std_msgs.msg import *
import geometry_msgs.msg 
from rectangle_support import *
from cv_bridge import CvBridge, CvBridgeError


def callback(data):
    try:
      cv_image = CvBridge().imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)

    cv2.imshow("Image window", cv_image)
    cv2.waitKey(1)
    return cv_image


def main():
  rect = detectRect()
  # Makes list for coords and angle
  index = 0
  xList = []
  yList = []
  angleList = []

  loop =True

 
  rospy.init_node('image_converter', anonymous=True)
  image_sub = rospy.Subscriber("/camera/color/image_raw",Image,callback)


  #depth_image = np.asanyarray(depth_frame.get_data())
  color_img_preCrop = np.asanyarray(cv_image.get_data())

  #cropping the color_img to ignore table
  color_img = color_img_preCrop[60:250, 200:500]

  cv2.imshow("Cropped color image",color_img)

  # Applys colormap on depth image (image must be converted to 8-bit per pixel first)
  #depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

  # depth_colormap_dim = depth_colormap.shape
  # color_colormap_dim = color_img.shape

  # # If depth and color resolutions are different, resize color image to match depth image for display
  # if depth_colormap_dim != color_colormap_dim:
  #     resized_color_img = cv2.resize(color_img, dsize=(depth_colormap_dim[1], depth_colormap_dim[0]),
  #                                      interpolation=cv2.INTER_AREA)
  #     images = np.hstack((resized_color_img, depth_colormap))
  # else:
  #     images = np.hstack((color_img, depth_colormap))



  # Show images
  cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
  #cv2.imshow('RealSense',images)

  image = color_img.copy()

  #imgDepth=depth_frame.copy()
  #cv2.imshow('Depth',depth_frame)
  #cv2.imshow('Depth color',depth_colormap)
  #print('Depth Array',depth_frame)

  cv2.imshow('RealSense',image)

  rect.

  a2, b2, c2 = getContours(color_img, image, minArea = 150, filter = 4)
  if len(b2) != 0:
      # Finds biggest contour
      biggest2 = b2[0]
      cv2.polylines(image,b2,True,(0,255,0),2)
      nPoints = (biggest2)
      if len(nPoints) != 0:
          # Locates center point, distance to edge of paper and finds angle
          NewWidth = round(findDis(nPoints[0][0]//scale, nPoints[1][0]//scale)/10,3)   #in cm
          NewHeight = round(findDis(nPoints[0][0]//scale, nPoints[2][0]//scale)/10,3)  #in cm
        #  print('New Width: ',cntr[0])
        #  print('New Height: ',cntr[2])
          cv2.arrowedLine(image, (nPoints[0][0][0], nPoints[0][0][1]),(nPoints[1][0][0], nPoints[1][0][1]),
                      (255,0,255),3,8,0, 0.05)
          cv2.arrowedLine(image, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[2][0][0], nPoints[2][0][1]),
                      (255,0,255),3,8,0,0.05)
          x,y,w,h = c2[0]

          angle, cntr, mean = getOrientation(nPoints, image)
          y_range=range((cntr[1]-50),(cntr[1]+50),1)
          x_range=range((cntr[0]-50),(cntr[0]+50),1)
          # print('X' + str(len(x_range)) + 'Y' + str(len(y_range)))
          # y_pixels=[np.ones(len(y_range))]
          # x_pixels=[np.ones(len(x_range))]
          # dis_pixels= np.zeros((len(x_range),len(y_range)))
          # stray = []
          # i = 0
          # while(i < len(y_range)-1):
          #     j = 0
          #     while(j < len(x_range)-1):
          #         dis_pixels[j,i] = depth_frame.get_distance(x_range[j], y_range[i])
          #         var = str(dis_pixels[j,i])
          #         stray.append(var)
          #         j = j+1
          #     i = i+1
          # name, path = write()
          # file = open(join(path, name),'w')   # Trying to create a new file or open one
          # i2 = 0
          # # DO NOT RUN BELOW --> Run risk to craashing computer & creating 7.0 gB txt file
          # # while (i2 < len(stray)-1):
          # #     file.write(stray[i2] +'/n')

          # #file.write()
          # file.close()
          # print('wrote to file')

                  
          result_angle = int(np.rad2deg(angle)) # in deg
          # multiplying by negative 1 to match gripper CW(-) & CCW(+)
          xC = round(findDis((cntr[0], cntr[1]), (0, cntr[1])) / (10*scale), 3) # in cm
          yC = round(findDis((cntr[0], cntr[1]), (cntr[0], 0)) / (10*scale), 3) # in cm
          #round((hP/(10*scale)) - 
          # Makes List for coordinates and angle
          xList.append(xC)
          yList.append(yC)
          angleList.append(result_angle)
          index = index + 1

          # Draws arrows and puts text on image
          cv2.arrowedLine(image, (cntr[0], cntr[1]), (cntr[0],1000), (0, 255, 0), 2, 8, 0, 0.05)
          cv2.arrowedLine(image, (cntr[0],cntr[1]), (0, cntr[1]), (0, 255,0),2,8,0,0.05)
          center = [NewWidth / 2, NewHeight / 2]
          cv2.putText(image, '{}cm'.format(NewWidth),(x+30, y-10), cv2.FONT_HERSHEY_PLAIN, 0.75, (0,0,0),1)
          cv2.putText(image, '{}cm'.format(NewHeight),(x-70, y+h//2), cv2.FONT_HERSHEY_PLAIN, 0.75, (0,0,0),1)
          label = "  Rotation Angle: " + str(int(np.rad2deg(angle)) + 90) + " degrees"
          #
          textbox = cv2.rectangle(image, (cntr[0], cntr[1] - 25), (cntr[0] + 250, cntr[1] + 10),
                                  (255, 255, 255), 1)
          cv2.putText(image, label, (cntr[0], cntr[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1,
                      cv2.LINE_AA)
          cv2.imshow('Warp',image)

          # Checks whether the same coords and angle are being detected consistently
          if (index >= 19):
              print('counting')
              same = isSame(index, xList, yList, angleList)
              if (same == True):
                  print('********* RESULTS ***************')
                  print('Angle is ' + str(result_angle) + ' degrees [CW Positive]')
                  print('Coordinate of center is (' + str(xC) + ' , ' + str(yC) + ') cm')
                  pub_angle = int(np.rad2deg(result_angle))
                  #talker()
                  a = [str(xC),str(yC),str(result_angle)]
                  #np.savetxt('Coordinate-angle.txt', zip(a), fmt="%5.2f")
                  #file.write(str(xC)+ '/n'+str(yC)+ '/n'+str(pub_angle))
                  # name, path = write()
                  # file = open(join(path, name),'w')   # Trying to create a new file or open one
                  # file.write(a[0] +'\n' +a[1] + '\n' +a[2])
                  # file.close()
                  # print('wrote to file')
                  #with open("/home/martinez737/ws_pick_camera/Coordinate-angle.txt", "r") as f:
                      #file_content = f.read()
                      #fileList = file_content.splitlines()
                      #xCNew = float(fileList[0])
                      #yCNew = float(fileList[1])
                      #angleNew = float(fileList[2])


                  loop=False

      cv2.waitKey(1)


  except rospy.ROSInterruptException:
    exit()
  except KeyboardInterrupt:
    exit()

if __name__ == '__main__':
  main()