import numpy as np
import cv2
import argparse
import os
import xml.etree.ElementTree as ET
parser = argparse.ArgumentParser(description='Multiple rec demo')
parser.add_argument('--detect_parent_path', action='store', dest='detect_parent_path')
args = parser.parse_args()
def computeSafeRegion(shape,bounding_rect):
    top = bounding_rect[1] # y
    bottom  = bounding_rect[1] + bounding_rect[3] # y +  h
    left = bounding_rect[0] # x
    right =   bounding_rect[0] + bounding_rect[2] # x +  w
    min_top = 0
    max_bottom = shape[0]  
    min_left = 0
    max_right = shape[1]
    if top < min_top:
        top = min_top
    if left < min_left:
        left = min_left
    if bottom > max_bottom:
        bottom = max_bottom
    if right > max_right:
        right = max_right
    return [left,top,right-left,bottom-top]

def cropImage(image,rect):
    print "rect",rect
    print "image.shape",image.shape
    x, y, w, h = computeSafeRegion(image.shape,rect)
    return image[y:y+h,x:x+w]

for filename in os.listdir(args.detect_parent_path):
        path = os.path.join(args.detect_parent_path, filename)
        if path.endswith(".jpg") or path.endswith(".png"):
            img = cv2.imread(path)
            #cv2.imshow('img', img)
            #cv2.waitKey(5000)
            name = filename.split('.',1)[0]
            
            inputpath = '/home/gch/AI/w/img_xml/' + str(name)+'.xml'
            if inputpath.endswith('xml'):
               tree = ET.parse(inputpath)
               root = tree.getroot()
               ii =0
               for object22 in root.findall('object'):
                   for object33 in object22.findall('bndbox'):
                       for x11 in object33.findall('xmin'):
                              x11 = x11.text
                              #print "x1:",x1
                       for y11 in object33.findall('ymin'):
                              y11 = y11.text
                              #print "y1:",y1
                       for x22 in object33.findall('xmax'):
                              x22 = x22.text
                              #print "x2:",x2
                       for y22 in object33.findall('ymax'):
                              y22 = y22.text
                
                   h2 = int(y22) - int(y11)
                   w2 = int(x22) - int(x11)
                   x = int(x11)
                   y = int(y11)
                   w = w2
                   h = h2
            x = h
            y = w
         
            #x, y = img.shape[0:2]
            #print "x:",x
            #print "y:",y
            top =int(x * 0.1)
            bottom =int(x * 0.1)
            left =int(y * 0.1)
            right =int(y* 0.1)
            x1_crop = int(x11) - left
            y1_crop = int(y11) - top
            x2_crop = int(x22) + right
            y2_crop = int(y22) + bottom
            h1 = y2_crop - y1_crop
            w1 = x2_crop - x1_crop
            cropped = cropImage(img, (int(x1_crop), int(y1_crop), int(w1), int(h1)))
            #cv2.imshow('cropped', cropped)
            #cv2.waitKey(5000)
            save_path = "/home/gch/AI/w/img_out/"
            cv2.imwrite(save_path  + name + ".jpg" , cropped)
            
            #print "top",top
            #print "bottom",bottom
            #print "left",left
            #print "right",right
            #cv2.imshow('OriginalPicture', img)
            #a = cv2.copyMakeBorder(img,top,bottom,left,right, cv2.BORDER_CONSTANT,value=[0,0,0])
            print(cropped.shape)
            x, y = cropped.shape[0:2]
            h= x
            w= y
            print "h:",h
            print "w:",w
            #cv2.imshow('a', a)
            #cv2.waitKey(1000)
            #cv2.destroyAllWindows()
            #save_path = "/home/gch/AI/w/out/"
            #cv2.imwrite(save_path  + name + ".jpg" , a)
            #print "asa"
            inputpath = '/home/gch/AI/w/xml/' + str(name)+'.xml'
            if inputpath.endswith('xml'):
               tree = ET.parse(inputpath)
               root = tree.getroot()
               ii =0
               print "######"
               for object2 in root.findall('object'):
                   for object3 in object2.findall('bndbox'):
                       for x1 in object3.findall('xmin'):
                              x1.text = str(left + int(x1.text))
                              tree.write(inputpath,encoding = 'utf-8')
                              #print "x1:",x1
                       for y1 in object3.findall('ymin'):
                              y1.text = str(top + int(y1.text))
                              tree.write(inputpath,encoding = 'utf-8')
                              #print "y1:",y1
                       for x2 in object3.findall('xmax'):
                              x2.text = str(left + int(x2.text))
                              tree.write(inputpath,encoding = 'utf-8')
                              #print "x2:",x2
                       for y2 in object3.findall('ymax'):
                              y2.text = str(top + int(y2.text))
                              tree.write(inputpath,encoding = 'utf-8')
                              #print "y2:",y2
               
               for object4 in root.findall('size'):
                   for ww1 in object4.findall('width'):
                       ww1.text = str(w)
                       tree.write(inputpath,encoding = 'utf-8')
                       print "****"
                   for hh1 in object4.findall('height'):
                       hh1.text = str(h)
                       tree.write(inputpath,encoding = 'utf-8') 
             
