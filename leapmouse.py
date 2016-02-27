import Leap, sys, thread, time, win32api, win32con, math
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
from win32api import GetSystemMetrics

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
		else:
			self.leftRelease(x,y)
	
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
		frame = controller.frame()
		for hand in frame.hands:
			handType = "Left Hand" if hand.is_left else "Right Hand"
			print handType + "Hand ID: " + str(hand.id) + "Palm position" + str(hand.palm_position)
			
			cursor.move(hand.palm_position.x,hand.palm_position.y,hand.grab_strength)
			

def main():
	listener = LeapMotionListener()
	controller = Leap.Controller()
	controller.images

	controller.add_listener(listener)

	print "Press enter to quit"
	try:
		sys.stdin.readline()
	except KeyboardInterrupt:
		pass
	finally:
		controller.remove_listener(listener)

if __name__ == "__main__":
	main()