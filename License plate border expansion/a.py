import numpy as np
import cv2
import argparse
import os
import xml.etree.ElementTree as ET
parser = argparse.ArgumentParser(description='Multiple rec demo')
parser.add_argument('--detect_parent_path', action='store', dest='detect_parent_path')
args = parser.parse_args()
for filename in os.listdir(args.detect_parent_path):
        path = os.path.join(args.detect_parent_path, filename)
        if path.endswith(".jpg") or path.endswith(".png"):
            img = cv2.imread(path)
            name = filename.split('.',1)[0]
            
            #print(img.shape)
            x, y = img.shape[0:2]
            #print "x:",x
            #print "y:",y
            top =int(x * 0.1)
            bottom =int(x * 0.1)
            left =int(y * 0.1)
            right =int(y* 0.1)
            #print "top",top
            #print "bottom",bottom
            #print "left",left
            #print "right",right
            #cv2.imshow('OriginalPicture', img)
            a = cv2.copyMakeBorder(img,top,bottom,left,right, cv2.BORDER_CONSTANT,value=[0,0,0])
            #print(a.shape)
            x, y = a.shape[0:2]
            h= x
            w= y
            #print "h:",h
            #print "w:",w
            #cv2.imshow('a', a)
            #cv2.waitKey(1000)
            #cv2.destroyAllWindows()
            save_path = "/home/gch/AI/w/out/"
            cv2.imwrite(save_path  + name + ".jpg" , a)
            
            inputpath = '/home/gch/AI/w/xml/' + str(name)+'.xml'
            if inputpath.endswith('xml'):
               tree = ET.parse(inputpath)
               root = tree.getroot()
               ii =0
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
