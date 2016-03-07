import Leap, sys, thread, time, win32api, win32con, math
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
from win32api import GetSystemMetrics
from Tkinter import *
from workspace import *
from visual import *


class Mouse:
	SCREEN_W = 0
	SCREEN_H = 0
	def __init__(self):
		self.SCREEN_W = GetSystemMetrics(0)
		self.SCREEN_H = GetSystemMetrics(1)

	def move(self,x,y,fist):
		x = 10*int(x)
		if x > self.SCREEN_W :
			x = self.SCREEN_W
		y = 5*((self.SCREEN_H/2)-int(y))
		if y > self.SCREEN_H :
			y = self.SCREEN_H
		win32api.SetCursorPos((x,y))
		if int(fist) == 1:
			self.leftClick(x,y)
		elif int(fist) <= 1:
			self.leftRelease(x,y)
		#elif tap == 3:
		#	self.leftClick(x,y)
		#	self.leftRelease(x,y)

	
	def leftClick(self,x,y):
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	def leftRelease(self,x,y):
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

	def rightClick(self,x,y):
		win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
	def rightRelease(self,x,y):
		win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)

cursor = Mouse()

class LeapMotionListener(Leap.Listener):
	finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
	bone_names = ['Metacarpol', 'Priximal', 'Intermediate', 'Distal']
	state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']
	

	def on_init(self, controller):
		#lpos = 0
		#rpos = 0
		#lgarb = 0
		#rgrab = 0
		print "initialized"

	def on_connect(self, controller):
		print "Motion sensor connected!!!!!"

		controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
		controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
		controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
		controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

	def on_disconnect(self, controller):
		print "Motion sensor disconnected!!!!"

	def on_exit(self, controller):
		print "Exited"

	def on_frame(self, controller):
		lgrab = 0
		rgrab = 0
		frame = controller.frame()
		#gesture = frame.gestures()
		for hand in frame.hands:
			#handType = "Left Hand" if hand.is_left else "Right Hand"
			#print handType + "Hand ID: " + str(hand.id) + "Palm position" + str(hand.palm_position) + "Hand grip: " + str(hand.grab_strength)
			if hand.is_left:
				lpos = hand.palm_position
				lgrab = hand.pinch_strength
				#print "lpos: " + str(lpos) + "lgrab " + str(lgrab)
			elif hand.is_right:
				rpos = hand.palm_position
				rgrab = hand.pinch_strength
				#print "rpos: " + str(rpos) + "rgrab " + str(rgrab)

			if lgrab >= 0.8 and rgrab >= 0.8:
				print str(int(lpos.x) - int(rpos.x))
			#obj.resize(hand.is_left,hand.is_right,lpos,rpos,lgrab,rgrab)
			if hand.is_right:
				#if gesture.type == Leap.Gesture.TYPE_KEY_TAP:
					#keytap = KeyTapGesture(gesture)
					cursor.move(hand.stabilized_palm_position.x,hand.stabilized_palm_position.y,hand.grab_strength)
					#print "Key Tap ID: " + str(gesture.id) + "State : " + str(gesture.state) + "Position: " + str(keytap.position) + "Direction: " + str(keytap.direction)

def test():
	print "sdf"

def main():
	listener = LeapMotionListener()
	controller = Leap.Controller()
	controller.add_listener(listener)
	
	scene = Workspace()
	scene.renderWorkspace().pack()	

	print "Press enter to quit"
	try:
		sys.stdin.readline()
	except KeyboardInterrupt:
		pass
	finally:
		controller.remove_listener(listener)
	
if __name__ == "__main__":
	main()