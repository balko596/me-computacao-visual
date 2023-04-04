# MEDIDA DE EFICIENCIA DA DISCIPLINA DE COMPUTAÇÃO VISUAL

import cv2
import numpy as np
from collections import namedtuple
import matplotlib.pyplot as plt

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
WINDOW_SIZE = (WINDOW_HEIGHT, WINDOW_HEIGHT, 3)
Object = namedtuple("Object", "x y scale theta")

# define the five objects
obj_1 = Object(320, 320, 5, 0)
obj_2 = Object(480, 480, 5, 0)
obj_3 = Object(210, 210, 5, 0)
obj_4 = Object(0, 0, 5, 0)
obj_5 = Object(0, 0, 5, 0)

# define colors
BLUE =  (255,  0 ,  0 )
GREEN = ( 0 , 255,  0 )
RED =   ( 0 ,  0 , 255)

canvas = np.ones(WINDOW_SIZE, dtype="uint8") * 40

def draw_obj_1(x:int, y:int, scale:int, theta:int):
    center = (x, y - 8*scale)
    r = 6*scale
    cv2.circle(canvas, center, r, BLUE, cv2.FILLED)

    init_point = (x - 2*scale , y - 10*scale)
    end_point = (x + 2*scale,y + 100*scale)
    cv2.rectangle(canvas, pt1=init_point, pt2=end_point, color=BLUE, thickness=-1)

def draw_obj_2(x:int, y:int, scale:int, theta:int):
    center = (x, y - 12*scale)
    r = 6*scale
    cv2.circle(canvas, center, r, BLUE, cv2.FILLED)


def draw_obj_3(x:int, y:int, scale:int, theta:int):
    pass

def draw_obj_4(x:int, y:int, scale:int, theta:int):
    pass

def draw_obj_5(x:int, y:int, scale:int, theta:int):
    pass
    
def draw_canvas():
    draw_obj_1(obj_1.x, obj_1.y, obj_1.scale, obj_1.theta)
    draw_obj_2(obj_2.x, obj_2.y, obj_2.scale, obj_2.theta)
    draw_obj_3(obj_3.x, obj_3.y, obj_3.scale, obj_3.theta)
    draw_obj_4(obj_4.x, obj_4.y, obj_4.scale, obj_4.theta)
    draw_obj_5(obj_5.x, obj_5.y, obj_5.scale, obj_5.theta)
    cv2.imshow("Catavento", canvas)

def translate():
    pass

def rotate():
    pass

def scale():
    pass

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

    elif key == "t":
        translate()
    
    elif key == "r":
        rotate()

    elif key == "s":
        scale()

    draw_canvas()

if cv2.getWindowProperty('sunset', cv2.WND_PROP_VISIBLE) < 1:
    print("ALL WINDOWS ARE CLOSED")
cv2.waitKey(1)
