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
csv_name = img_name[0:-4]
img = cv2.imread(img_name,0)
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
resized_img_float = resized_img.astype(float)
powermap_data = 15*(resized_img/255)
powermap_data = 15 - powermap_data
powermap_data_int = np.round(powermap_data).astype(int)

#save to csv format
SFC_Obj.Save_Matrix2CSV_with_TimeStamp(csv_name,resized_img)
SFC_Obj.Save_Matrix2CSV_with_TimeStamp(csv_name+"Pmap",powermap_data_int)

#cv2.waitKey(0)
#cv2.destroyAllWindows()