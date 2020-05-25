# -*- coding: utf-8 -*-
VERSION=0.01
import portalocker
import os
import sys
import gtk
from gtk import gdk 
import pythoncom, pyHook
import thread
import base64
import php
import time
import random
# 播放打字音用
import pyaudio
import audioop
import wave
paudio_player = pyaudio.PyAudio()

my = php.kit()
reload(sys)
sys.setdefaultencoding('UTF-8')

UCL_PIC_BASE64 = "AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAMIOAADCDgAAAAAAAAAAAAD////////////////////////////////////////////////////////////////////////////////////////////////+/v7//Pz8//v7+//7+/v//f39////////////////////////////////////////////////////////////1s7B/1pVU/9PT0//Tk5Q/56rtP/Cua7/bGlp/2pqa/9tbGz/ampp/25xd//R2eL//////////////////////8O1of8kIyn/fYCD/0A0Lf9vgZD/kIJv/yUrMv9WUEr/FBcd/19eXv8fHR//q7zL///////////////////////CtKH/MDE4/6qwt/9zZFf/boCP/49/bf9VZXf/v7Ok/y0zP//T09P/QDcw/6q7yv//////////////////////w7Wj/yEcGv8pKy//OTUy/3GCkf+Pf23/VWV3/7+zo/8sMz//09PS/0A3MP+qu8r//////////////////////8KzoP84O0H/b2to/y4pJf9wgpH/j4Bt/1BfcP+1qpv/KjA7/8fHx/89NC//qrvK///////////////////////Cs6D/O0FM/9HS0f9IOi//boGQ/5KCcP8UFhn/Ly0p/w0PEv80MzP/FRcc/62+zP//////////////////////wrOh/zI1Ov9hXFT/AwAB/3GDk/+QgW//NkBK/6iqrP+trKz/qqqq/62vs//l6u///////////////////////76vnf8aFhb/Mzs+/0M9OP9wgpD/j39t/1Fhc//7//////////////////////////////////////////////+vnYv/QUtX/9ff3/96alv/bX+P/49/bf9RYHL/+/7/////////////v7Ko/5ifqf/7/v//////////////////inhn/19vgf//////fGpa/21/jv+Of23/UWBy//v+/////////////4Z0Yv9KWmv/+f3/////////////+/bv/1pNQv+Kmaf/samg/z01L/93iZn/n5B+/ygrMf93eXr/fHx8/3p4dv8vKib/eIqc//////////////////37+P/Mycf/5+rt/9HMxv+zs7X/3uPo/+zo4/+4trT/srKy/7Kysv+ysrL/tba5/+Tp7v//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=="
PWD = os.path.dirname(os.path.realpath(sys.argv[0]))

# Preset play music
is_play_music = True
# Debug 模式
is_DEBUG_mode = False

wavs = my.glob(PWD + "\\*.wav")
o_song = {}
m_play_song = []
max_thread___playMusic_counts = 3 #最多同時五個執行緒在作動
step_thread___playMusic_counts = 0 #目前0個執行緒
for i in range(0,len(wavs)):
  #from : https://pythonbasics.org/python-play-sound/
  #m_song.extend([ AudioSegment.from_wav(wavs[i]) ])
  o_song[ wavs[i] ] = {
                        "filename":wavs[i],
                        "data":[],
                        "wf":"",
                        "paudio_stream":""      
                      }
def thread___playMusic(keyboard_valume):
  try:
    # https://stackoverflow.com/questions/43679631/python-how-to-change-audio-volume
    # 調整聲音大小
    # https://stackoverrun.com/cn/q/10107660
    # Last : https://www.thinbug.com/q/45219574
    global paudio_player
    global o_song
    global m_play_song
    global step_thread___playMusic_counts
    
    #time.sleep(0.01)      
    if len(m_play_song) !=0 :
      #print("TEST")
      # https://stackoverflow.com/questions/36664121/modify-volume-while-streaming-with-pyaudio
      chunk = 2048
      #s = random.choice(m_song)
      m_play_song = m_play_song[ : 2]
      #print("TEST1")
      s = m_play_song.pop(0) #m_play_song[0]
      #print("TEST2")  
      if len(o_song[s]["data"]) == 0:
        #print("TEST3")
        o_song[s]["wf"] = wf = wave.open(s, 'rb')
        o_song[s]["paudio_stream"] = paudio_player.open(format = paudio_player.get_format_from_width(o_song[s]["wf"].getsampwidth()),
                      channels = o_song[s]["wf"].getnchannels(),
                      rate = o_song[s]["wf"].getframerate(),
                      output = True)
        # 寫聲音檔輸出來播放
        while True:
          #print("TEST4")    
          d = o_song[s]["wf"].readframes(chunk)
          if d == "": break      
          # 這是調整音量大小的方法
          o_song[s]["data"].extend([ audioop.mul(d, 2, keyboard_valume / 100.0 ) ])              
      #print("TEST5")
      for i in range(0,len(o_song[s]["data"])):
        o_song[s]["paudio_stream"].write(o_song[s]["data"][i])
    if step_thread___playMusic_counts > 0:
      step_thread___playMusic_counts = step_thread___playMusic_counts -1         
  except Exception as e:
    debug_print("thread___playMusic error:")
    debug_print(e)  
           
def about_my_keyboard_sound():
  _msg_text = ("肥鍵盤打字聲\n\n作者：羽山秋人 (http://3wa.tw)\n版本：%s" % VERSION)
  return _msg_text  
def debug_print(data):
  global is_DEBUG_mode
  if is_DEBUG_mode == True:
    print(data)


if len(sys.argv) == 2:
  if sys.argv[1]=="-d":
    is_DEBUG_mode = True
    
# 加入 trayicon
def message(data=None):
  "Function to display messages to the user."
  msg=gtk.MessageDialog(None, gtk.DIALOG_MODAL,
    gtk.MESSAGE_INFO, gtk.BUTTONS_OK, data)
  msg.run()
  msg.destroy()
# From : https://github.com/gevasiliou/PythonTests/blob/master/TrayAllClicksMenu.py
class TrayIcon(gtk.StatusIcon):
    def __init__(self):
      global VERSION
      global PWD
      global UCL_PIC_BASE64
      gtk.StatusIcon.__init__(self)
      # base64.b64decode
      # From : https://sourceforge.net/p/matplotlib/mailman/message/20449481/
      raw_data = base64.decodestring(UCL_PIC_BASE64)
      #debug_print(gtk.gdk.Pixbuf)
      w = 16
      h = 16
      img_pixbuf = gtk.gdk.pixbuf_new_from_data(
              raw_data, gtk.gdk.COLORSPACE_RGB, True, 8, w, h, w*4)

      self.set_from_pixbuf(img_pixbuf)
      self.set_tooltip("肥鍵盤打字聲：%s" % (VERSION))
      self.set_has_tooltip(True)
      self.set_visible(True)
      self.connect("button-press-event", self.on_click)

    def m_about(self,data=None):  # if i ommit the data=none section python complains about too much arguments passed on greetme
      message = gtk.MessageDialog(type=gtk.MESSAGE_INFO, buttons=gtk.BUTTONS_OK)
      message.set_position(gtk.WIN_POS_CENTER_ALWAYS)
      message.set_keep_above(True)
      _msg_text = about_my_keyboard_sound()       
      message.set_markup( _msg_text )      
      message.show()      
      response = message.run()            
      if response == -5 or response == -4:
        message.destroy()
    def m_pm_switch(self,data=None):
      global is_play_music
      if is_play_music == False:
        is_play_music = True
      else:
        is_play_music = False     
    def m_quit(self,data=None):
      self.set_visible(False)      
      sys.exit()
    def m_none(self,data=None):
      return False              
    def on_click(self,data,event): #data1 and data2 received by the connect action line 23            
      btn=event.button #Bby controlling this value (1-2-3 for left-middle-right) you can call other functions.                 
      global menu
      global menu_items      
      menu.set_visible(False)      
      for i in range(0,len(menu_items)):
        menu.remove(menu_items[i])
      menu_items=[]
      menu_items.append(gtk.MenuItem("1.關於肥鍵盤聲"))
      menu.append( menu_items[len(menu_items)-1] )
      menu_items[len(menu_items)-1].connect("activate", self.m_about) #added by gv - it had nothing before
              
      if is_play_music==True:
        menu_items.append(gtk.MenuItem("2.【●】打字音"))
        menu.append( menu_items[len(menu_items)-1] )
        menu_items[len(menu_items)-1].connect("activate", self.m_pm_switch)
      else:
        menu_items.append(gtk.MenuItem("2.【　】打字音"))
        menu.append( menu_items[len(menu_items)-1] )
        menu_items[len(menu_items)-1].connect("activate", self.m_pm_switch)
                        
      menu_items.append(gtk.MenuItem(""))
      menu.append( menu_items[len(menu_items)-1] )
      
      menu_items.append(gtk.MenuItem("離開(Quit)"))
      menu.append( menu_items[len(menu_items)-1] )
      menu_items[len(menu_items)-1].connect("activate", self.m_quit)

      #add space
      menu_items.append(gtk.MenuItem(""))
      menu.append( menu_items[len(menu_items)-1] )
      menu_items.append(gtk.MenuItem(""))
      menu.append( menu_items[len(menu_items)-1] )
      menu_items.append(gtk.MenuItem(""))
      
      
      menu.show_all()      
      menu.popup(None, None, None, btn, 2) #button can be hardcoded (i.e 1) but time must be correct.      


def OnKeyboardEvent(event):    
  global m_play_song
  global max_thread___playMusic_counts
  global step_thread___playMusic_counts
  try:  
    if is_play_music == True and event.MessageName == "key down" and len(o_song.keys())!=0 and step_thread___playMusic_counts < max_thread___playMusic_counts:
      step_thread___playMusic_counts = step_thread___playMusic_counts + 1                  
      m_play_song.extend( [ random.choice(o_song.keys()) ])
      thread.start_new_thread( thread___playMusic,(50,))  
  except:
    pass
  return True
# create a hook manager
hm = pyHook.HookManager()
# watch for all mouse events
hm.KeyAll = OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever


menu_items = []
menu = gtk.Menu()

tray = TrayIcon()  
#win.show_all()
updateGUI_Step = 0
def updateGUI():
  global updateGUI_Step
  #global is_shutdown
  while gtk.events_pending():
    gtk.main_iteration(False)
  updateGUI_Step = updateGUI_Step + 1
  if updateGUI_Step % 100 == 0:
    updateGUI_Step = 0    
while True:
  time.sleep(0.01)  
  updateGUI()    
pythoncom.PumpMessages()