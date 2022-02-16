from graphics import *
from math import pi, cos, radians, sin
import time

def clock_background(width, height) -> Circle:
    '''
    Returns Circle(centered, 0.45*width of GraphWin)
    '''
    return Circle(Point(0,0),0.45*width)

def getCurrentTime():
    '''
    Returns current time as tuple (hr, min)
    '''
    return tuple([int(val) for val in time.strftime("%H,%M").split(',')])

def get_minuteHandPoints(mn, width, height):
    '''
    Returns tuple of Point objects for usage in Polygon describing a minute hand
    positioned at mn.
    '''
    min_rotation = radians((6 * mn)+90)
    radius_outer = 0.40*width
    radius_inner = 0.2*width
    p1 = Point(0, 0)
    p2 = Point(radius_inner*cos(min_rotation+.08), radius_inner*sin(min_rotation+.08))
    p3 = Point(radius_outer*cos(min_rotation), radius_outer*sin(min_rotation))
    p4 = Point(radius_inner*cos(min_rotation-.08), radius_inner*sin(min_rotation-.08))
    return p1, p2, p3, p4

def getMinuteHand(mn, width, height):
    '''
    Returns Polygon object for minute hand positioned at mn.
    '''
    points = get_minuteHandPoints(mn, width, height)
    return Polygon(list(points))

def get_hourHandPoints(hr, width, height):
    '''
    Returns tuple of Point objects for usage in Polygon describing an hour hand,
    positioned at hr.
    '''
    hour_rotation = radians(((15 * hr)*2)+90)
    radius_outer = 0.3*width
    radius_inner = 0.1*width
    p1 = Point(0, 0)
    p2 = Point(radius_inner*cos(hour_rotation+.08), radius_inner*sin(hour_rotation+.08))
    p3 = Point(radius_outer*cos(hour_rotation), radius_outer*sin(hour_rotation))
    p4 = Point(radius_inner*cos(hour_rotation-.08), radius_inner*sin(hour_rotation-.08))
    return p1, p2, p3, p4

def getHourHand(hr, width, height):
    '''
    Returns Polygon object for hour hand positioned at hr.
    '''
    points = get_hourHandPoints(hr, width, height)
    return Polygon(list(points))

def main():
    '''
    This (DONE!):
    X creates a GraphWin app window with WIDTH and HEIGHT specified below
    X sets the window coordinates with (0, 0) at the center
    X circular perimeter for an analog clock
    X engages in infinite loop:
      X gets current time in hr and min
      X gets Polygon shapes for hour and minute hands and draws them
      X updates geometry for min and hr hand with undraw
      X checks the mouse, and if clicked, terminates
    '''
    width = 800; height = 800

    win = GraphWin("Clock", width,height)
    win.setCoords(-(width*.5), -(height*.5), width*.5, height*.5)
    win.setBackground("gray")

    clock_border = clock_background(width, height)
    clock_border.setFill("lightgray")
    clock_border.setWidth(.005*width)
    clock_border.draw(win)

    current_time = getCurrentTime()
    hour = -current_time[0]
    min = -current_time[1]
    previous_time = current_time

    minute_hand = getMinuteHand(min, width, height)
    minute_hand.setFill("red")
    minute_hand.setOutline("red")
    minute_hand.draw(win)

    hour_hand = getHourHand(hour, width, height)
    hour_hand.setFill("blue")
    hour_hand.setOutline("blue")
    hour_hand.draw(win)

    inner_circle = Circle(Point(0,0), .02*width)
    inner_circle.setFill("black")
    inner_circle.draw(win)

    while True:
        current_time = getCurrentTime()
        hour = -current_time[0]
        min = -current_time[1]
        
        if current_time != previous_time:
            minute_hand.undraw()
            hour_hand.undraw()

            minute_hand = getMinuteHand(min, width, height)
            minute_hand.setFill("red")
            minute_hand.setOutline("red")
            minute_hand.draw(win)

            hour_hand = getHourHand(hour, width, height)
            hour_hand.setFill("blue")
            hour_hand.setOutline("blue")
            hour_hand.draw(win)

            inner_circle = Circle(Point(0,0), .02*width)
            inner_circle.setFill("black")
            inner_circle.draw(win)

            previous_time = current_time
        
        if win.checkMouse():
            exit()

if __name__ == "__main__":
    try:  main()
    except: print("Force closed")
