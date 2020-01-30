#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 17:58:26 2020

@author: pengfei
"""

#%% import modules

import numpy as np
import matplotlib.pylab as plt
from Class_Simple_Function_Collections import SimpleFunctionCollections
import cv2

#%%
# Create simple function Collections obj
SFC_Obj = SimpleFunctionCollections()

img_name = 'logo_huawei.jpg'
img_name = 'timg.jpeg'
csv_name = img_name[0:-4]
img = cv2.imread("InputData/"+img_name,0)
cv2.imshow('image',img)
img_shape = np.shape(img)

# =============================================================================
# scale_percent = 220 # percent of original size
# width = int(img.shape[1] * scale_percent / 100)
# height = int(img.shape[0] * scale_percent / 100)
# =============================================================================

#resize the image
width = 16*5; height = 16*6
dim = (width, height)
# resize image
resized_img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
resized_img_shape = resized_img.shape
print('Resized Dimensions : ',resized_img.shape)
cv2.imshow("Resized image", resized_img)

#convert to powermap data
def convert2powermap(resized_img):
    resized_img_float = resized_img.astype(float)
    powermap_data = 15*(resized_img/255)
    powermap_data = 15 - powermap_data
    powermap_data_int = np.round(powermap_data).astype(int)
    return powermap_data_int

#Keep as original aspect ratio
original_aspect_ratio = img_shape[0]/img_shape[1]
target_aspect_ratio = height/width

if original_aspect_ratio > target_aspect_ratio:
    scale_for_height = img_shape[0]/height
    scale_for_width = scale_for_height
    width_within_scale = img_shape[1]/scale_for_width
    width_within_scale_int = int(width_within_scale)
    resized_img = cv2.resize(img, (width_within_scale_int,height), interpolation = cv2.INTER_AREA)
    add_width = width - width_within_scale_int
    add_patch_matrix = 255*np.ones((height,add_width))
    final_img = np.hstack((resized_img.astype(int),add_patch_matrix))
    final_img_uint8 = final_img.astype("uint8")
else:
    scale_for_width = img_shape[1]/width
    scale_for_height = scale_for_width
    height_within_scale = img_shape[0]/scale_for_height
    height_within_scale_int = int(height_within_scale)
    resized_img = cv2.resize(img, (width,height_within_scale_int), interpolation = cv2.INTER_AREA)
    add_height = height - height_within_scale_int
    add_patch_matrix = 255*np.ones((add_height,width))
    final_img = np.vstack((resized_img.astype(int),add_patch_matrix))
    final_img_uint8 = final_img.astype("uint8")
    
cv2.imshow("Resized image within scale", final_img_uint8)
#save to csv format
SFC_Obj.Save_Matrix2CSV_with_TimeStamp(csv_name,resized_img)
SFC_Obj.Save_Matrix2CSV_with_TimeStamp(csv_name+"Pmap",convert2powermap(resized_img))
SFC_Obj.Save_Matrix2CSV_with_TimeStamp(csv_name+"Pmap_keepscale",convert2powermap(final_img_uint8))
#cv2.waitKey(0)
#cv2.destroyAllWindows()
input("Enter any key to exit~")