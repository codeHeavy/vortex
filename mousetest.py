import win32api, win32con
import time
import math

while(True):
	x = input("x: ")
	y = input("y: ")
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
	#win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
	#win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)
	time.sleep(.01)