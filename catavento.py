# MEDIDA DE EFICIENCIA DA DISCIPLINA DE COMPUTAÇÃO VISUAL

import cv2
import numpy as np
from collections import namedtuple
import matplotlib.pyplot as plt

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
WINDOW_SIZE = (WINDOW_HEIGHT, WINDOW_HEIGHT, 3)
Object = namedtuple("Object", "x y")

# define the five objects
obj_1 = Object(320, 320)
obj_2 = Object(320, 425)
obj_3 = Object(190, 210)
obj_4 = Object(315, 190)
obj_5 = Object(0, 0)

# define colors
BLUE =  (255,  0 ,  0 )
GREEN = ( 0 , 255,  0 )
RED =   ( 0 ,  0 , 255)

scale = 5

canvas = np.ones(WINDOW_SIZE, dtype="uint8") * 40

def draw_obj_1(x:int, y:int, scale:int):
  center = (x, y - 8*scale)
  r = 6*scale
  cv2.circle(canvas, center, r, BLUE, cv2.FILLED)

def draw_obj_2(x:int,y:int , scale:int):
    init_point = (x - 2*scale , y - 25*scale)
    end_point = (x + 2*scale,y + 130*scale)
    cv2.rectangle(canvas, pt1=init_point, pt2=end_point, color=BLUE, thickness=-1)
    
def draw_obj_3(x:int,y:int , scale:int):
    point_a = [x + 12*scale,y - 22*scale]
    point_b = [x - 26*scale,y - 22*scale]
    triangle = np.array([point_a, point_b,[320, 280]], np.int32)
    cv2.fillPoly(canvas,[triangle],BLUE)

    point_a2 =  [x - 13*scale, y - 18*scale]
    point_c = [x + 13*scale, y + 2*scale]
    triangle = np.array([point_a2,point_c,[320, 280]], np.int32)
    cv2.fillPoly(canvas,[triangle],RED)

def draw_obj_4(x:int, y:int , scale:int):
    pass

def draw_obj_5(x:int, y:int , scale:int):
    pass
    
def draw_canvas():
    draw_obj_1(obj_1.x, obj_1.y, scale=scale)
    draw_obj_2(obj_2.x, obj_2.y, scale=scale)
    draw_obj_3(obj_3.x, obj_3.y, scale=scale)
    draw_obj_4(obj_4.x, obj_4.y, scale=scale)
    draw_obj_5(obj_5.x, obj_5.y, scale=scale)
    cv2.imshow("Catavento", canvas)

draw_canvas()
while True:
    key = cv2.waitKey(1000)

    # it waits till we press a key
    key = cv2.waitKey(0)
    
    # if we press esc
    if key == 27:
        print('esc is pressed closing all windows')
        cv2.destroyAllWindows()
        break
    
    draw_canvas()

if cv2.getWindowProperty('sunset', cv2.WND_PROP_VISIBLE) < 1:
    print("ALL WINDOWS ARE CLOSED")
cv2.waitKey(1)
