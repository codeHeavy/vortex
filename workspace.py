from __future__ import division, print_function
from visual import  *
import visual as vs   # for 3D panel 
import wx, sys   # for widgets
clr = vs.color
class Workspace:
  def __init__(self):
    win = vs.window(width=1024, height=720, menus=False, title='SIMULATE VPYTHON GUI')# make a main window. Also sets w.panel to addr of wx window object.
    scene = vs.display( window=win, width=800, height=720, forward=-vs.vector(1,1,2))# make a 3D panel
    vss = scene
    p = win.panel
    sphere_button = wx.Button(p, label='Sphere', pos=(810,10), size=(190,100))
    #sphere_button.Bind(wx.EVT_BUTTON, self.options())
    cube_button = wx.Button(p, label='Cube', pos=(810,120), size=(190,100))
    #cube_button.Bind(wx.EVT_BUTTON, functionname)
  # Draw 3D model ======================

  def axes(self, frame, colour, sz, posn ): # Make axes visible (of world or frame).
                                       # Use None for world.   
      directions = [vs.vector(sz,0,0), vs.vector(0,sz,0), vs.vector(0,0,sz)]
      texts = ["X","Y","Z"]
      posn = vs.vector(posn)
      for i in range (3): # EACH DIRECTION
         vs.curve( frame = frame, color = colour, pos= [ posn, posn+directions[i]])
         vs.label( frame = frame,color = colour,  text = texts[i], pos = posn+ directions[i],
                                                                      opacity = 0, box = False )

  
  def drawGrid(self, posn=(0,0,0), sq=1, H=12, W = 1, normal='z', colour= clr.white ) :
      ht = H*sq
      wd = W*sq
      for i in range( 0, ht+1, sq ):  # FOR EACH HORIZONTAL LINE
          if normal == 'x':
              vs.curve( pos=[(posn[1]+i, posn[0], posn[2]+wd),(posn[1]+i, posn[0], posn[2])], color=colour)
              #print (posn[0] + posn[1]+i + posn[2]+wd) #for testing purposes
          else: vs.curve( pos=[(posn[0],    posn[1], posn[2]+i),
                                             (posn[0]+wd, posn[1], posn[2]+i)], color=colour)
  def renderWorkspace(self):
    self.axes( None, clr.white, 3, (-11,6,0))
    self.drawGrid( normal = 'z', posn= (-6, 0, -6), colour = clr.blue,   W = 12 )
    self.drawGrid( normal = 'x', posn= (0, -6, -6), colour = clr.green,  W = 12 )
    #ball = sphere (color = color.blue, radius = 1.1, make_trail=True, retain=200,pos=(0,0,0))

  def options(self):
    sphere()
    print("her")
    pass

def main():
  scene1 = Workspace()
  scene1.renderWorkspace()

if __name__ == "__main__":
  main()