import winsound
import Leap, sys, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

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
		#hand = frame.hands
		for hand in frame.hands:
			#print "Grab strength; " + str(hand.grab_strength)
			#for pointable in hand.pointables:
			print "Pinch strength; " + str(hand.pinch_strength)
			v = int(hand.pinch_strength*10)
			for a in range(v):
				winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
				#winsound.Beep(100, 100)
def main():
	listener = LeapMotionListener()
	controller = Leap.Controller()
	controller.add_listener(listener)

	print "Press enter to quit"
	try:
		sys.stdin.readline()
	except KeyboardInterrupt:
		pass
	finally:
		controller.remove_listner(listner)

if __name__ == "__main__":
	main()