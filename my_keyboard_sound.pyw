# -*- coding: utf-8 -*-
VERSION=0.04
import portalocker
import os
import sys
import pkg_resources
import tkinter
from tkinter import messagebox
from traybar import SysTrayIcon
import threading
import pythoncom 
import pyHook
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
is_stop_thread = False
my = php.kit()
PWD = os.path.dirname(os.path.realpath(sys.argv[0]))
reload(sys)
sys.setdefaultencoding('UTF-8')

# hide root window
root = tkinter.Tk()
root.withdraw()

# 系統圖示                                                    
UCL_PIC_BASE64 = "AAABAAEAOT0AAAEAIABkOAAAFgAAACgAAAA5AAAAegAAAAEAIAAAAAAAVDYAAMMOAADDDgAAAAAAAAAAAAD////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////U/4BVgP/U////////////////////////////1P+qgFX/VVVV/1VVVf9VVVX/gICq/9TU/////////////////////////////////////////////////////////9TU/9TU1P/U1Kr/qqqq/6qqqv+qqqr/qqqq/6qqqv+qqqr/qqqq/6qqqv+qqqr/qqqq/6qqqv+q1NT/1NTU////////////////////////////////////////////////////////////////////////////////////////1Kr/VSsA/0yxIv9Vqv////////////////////////+qVf9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv8rVar////////////////////////////////////U/4BVK/9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv8rVar/1P/////////////////////////////////////////////////////////////////////UgP8rAAD/TLEi/0yxIv8AVar//////////////////////6pVAP9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/Var//////////////////////////6r/VQAA/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/ACuA/9T//////////////////////////////////////////////////////////////6pVAP9MsSL/TLEi/0yxIv8AAFX/qv////////////////+q/1UAAP9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/ACuA/9T////////////////////UgCv/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/1Wq//////////////////////////////////////////////////////////////+qVf9MsSL/TLEi/0yxIv9MsSL/Var/////////////1IAr/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/AABV/6r/////////////////1P+AKwD/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/wArgP/U////////////////////////////////////////////////////////////qv9VAAD/TLEi/0yxIv9MsSL/K4DU///////////////////////////////////////UgCv/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/AAAr/4Cqqv/U1NT/1NTU/9TU1P/U1NT/1NTU/9TU1P/U1NT/1NTU/9TU1P/U1NT/1NTU/9TU1P+qgFX/TLEi/0yxIv9MsSL/TLEi/wAAVf+q//////////////////////////////////////////////////////////////+qVQD/TLEi/0yxIv9MsSL/ACuA/9T/////////////////////////////////////qlX/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/K4DU////////////////////////////////////////////////////////////////////////////qlUA/0yxIv9MsSL/TLEi/wAAK/+A1P//////////////////////////////////////////////////////////////qlX/TLEi/0yxIv9MsSL/AABV/6r/////////////////////////////////////qlX/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/K4DU/////////////////////////////////////////////////////////////////////////////6pV/0yxIv9MsSL/TLEi/0yxIv8rgNT/////////////////////////////////////////////////////////////1ID/KwAA/0yxIv9MsSL/AAAr/4DU////////////////////////////////////qlX/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/K4DU/////////////////////////////////////////////////////////////////////////////9SA/ysAAP9MsSL/TLEi/0yxIv8rgNT//////////////////////////////////////////////////////////////6r/VQAA/0yxIv9MsSL/TLEi/1Wq////////////////////////////////////qlX/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/K4DU//////////////////////////////////////////////////////////////////////////////+q/1UAAP9MsSL/TLEi/0yxIv8AVar/////////////////////////////////////////////////////////////////qlUA/0yxIv9MsSL/TLEi/yuA1P//////////////////////////////////qlX/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/K4DU///////////////////////////////////////////////////////////////////////////////U/4ArAP9MsSL/TLEi/0yxIv8AK4D/1P//////////////////////////////////////////////////////////////1IAr/0yxIv9MsSL/TLEi/wBVqv//////////////////////////////////qlX/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/K4DU///////////////////////////////////////////////////////////////////////////////U/4ArAP9MsSL/TLEi/0yxIv8AAFX/qv//////////////////////////////////////////////////////////////1IAr/0yxIv9MsSL/TLEi/wArgP/U////////////////////////////////qlX/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/K4DU/////////////////////////////////////////////////////////////////////////////////6pVAP9MsSL/TLEi/0yxIv8rVar/1P///////////////////////////////////////////////////////////////6pV/0yxIv9MsSL/TLEi/wArgP/U///////U/9T/////////////////////qlX/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/K4DU/////////////////////////////////////////////////////////////////////////////////6pVAP8rK1X/gKrU/////////////////////////////////////////////////////////////////////////////9SA/ysAAP9MsSL/TLEi/wAAVf+q////qlUA/wArgP/U////////////////qlX/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/K4DU/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////9SA/ysAAP9MsSL/TLEi/wAAVf+q1ID/KwAA/0yxIv8AVar/1P//////////qlX/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/K4DU/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////9SA/ysAAP9MsSL/TLEi/wAAVf9VVQD/TLEi/0yxIv9MsSL/AFWq////////qlX/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/K4DU/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////9SA/ysAAP9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/yuA1P//qlX/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/K4DU//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////+q/1UAAP9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9VVVX/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/K4DU//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////+q/1UAAP9MsSL/TLEi/0yxIv9VqtT/gCsA/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/K4DU//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////+q/1UAAP9MsSL/TLEi/0yxIv9Vqv////+q/1UrAP9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/K4DU//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////+q/1UAAP9MsSL/TLEi/0yxIv9Vqv//////////qv9VAAD/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/K4Cq/9TU1P/U1NT/1NTU/9TU1P/U1NT/1NTU/9TU1P/U1NT/1NTU/9TU1P/U1NT/1NTU/9TU1P/U1NT/1NTU/9TU1P/U1NT/1NT///////////////////////////////////////////////////////////////////////////////+q/1UAAP9MsSL/TLEi/0yxIv9Vqv//////////////1ID/KwAA/0yxIv9MsSL/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/ACuA/9T///////////////////////////////////////////////////////////////////////////+q/1UAAP9MsSL/TLEi/0yxIv9Vqv///////////////////6pV/0yxIv9MsSL/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/ACuA/9T///////////////////////////////////////////////////////////////////////////+q/1UAAP9MsSL/TLEi/0yxIv9Vqv///////////////////////9SAK/9MsSL/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/ACuA/9T///////////////////////////////////////////////////////////////////////////+q/1UAAP9MsSL/TLEi/0yxIv9Vqv//////////////////////////1P+AKwD/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/ACuA/9T///////////////////////////////////////////////////////////////////////////+q/1UAAP9MsSL/TLEi/0yxIv9Vqv//////////////////////////////qlX/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/K1WA/6qqqv+qqqr/qqqq/6qqgP8rAAD/TLEi/0yxIv9MsSL/ACuA/6qqqv+qqqr/qqqq/6qqqv+AKwD/TLEi/0yxIv9MsSL/ACuA/9T///////////////////////////////////////////////////////////////////////////+q/1UAAP9MsSL/TLEi/0yxIv9Vqv/////////UgP8rACv/VarU////////qlX/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/K4DU////////////////////qv9VAAD/TLEi/0yxIv9MsSL/AFWq//////////////////////+qVQD/TLEi/0yxIv9MsSL/ACuA/9T///////////////////////////////////////////////////////////////////////////+q/1UAAP9MsSL/TLEi/0yxIv9Vqv///////9SAK/9MsSL/TLEi/ytVgP/UqlX/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/K4DU////////////////////qv9VAAD/TLEi/0yxIv9MsSL/AFWq//////////////////////+qVQD/TLEi/0yxIv9MsSL/ACuA/9T///////////////////////////////////////////////////////////////////////////+q/1UAAP9MsSL/TLEi/0yxIv9Vqv/////U/4ArAP9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/K4DU////////////////////qv9VAAD/TLEi/0yxIv9MsSL/AFWq//////////////////////+qVQD/TLEi/0yxIv9MsSL/ACuA/9T///////////////////////////////////////////////////////////////////////////+q/1UAAP9MsSL/TLEi/0yxIv9Vqv///9SA/ysAAP9MsSL/TLEi/0yxIv9VVVX/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/K4DU////////////////////qv9VAAD/TLEi/0yxIv9MsSL/AFWq//////////////////////+qVQD/TLEi/0yxIv9MsSL/ACuA/9T///////////////////////////////////////////////////////////////////////////+q/1UAAP9MsSL/TLEi/0yxIv9Vqv//1IAr/0yxIv9MsSL/TLEi/wAAVf+qqlX/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/K4DU////////////////////qv9VAAD/TLEi/0yxIv9MsSL/AFWq//////////////////////+qVQD/TLEi/0yxIv9MsSL/ACuA/9T///////////////////////////////////////////////////////////////////////////+q/1UAAP9MsSL/TLEi/0yxIv9Vqqr/VQAA/0yxIv9MsSL/TLEi/wBVqv//qlX/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/K4DU////////////////////qv9VAAD/TLEi/0yxIv9MsSL/AFWq//////////////////////+qVQD/TLEi/0yxIv9MsSL/ACuA/9T///////////////////////////////////////////////////////////////////////////+q/1UAAP9MsSL/TLEi/0yxIv8rKyv/TLEi/0yxIv9MsSL/AAAr/4DU////qlX/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/K4DU////////////////////qv9VAAD/TLEi/0yxIv9MsSL/AFWq//////////////////////+qVQD/TLEi/0yxIv9MsSL/ACuA/9T///////////////////////////////////////////////////////////////////////////+q/1UAAP9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/ACuA/9T/////qlX/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/K4DU////////////////////qv9VAAD/TLEi/0yxIv9MsSL/AFWq//////////////////////+qVQD/TLEi/0yxIv9MsSL/ACuA/9T///////////////////////////////////////////////////////////////////////////+q/1UAAP9MsSL/TLEi/0yxIv9VgKr/VSsA/0yxIv9MsSL/Var/////////qlX/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/K4DU////////////////////qv9VAAD/TLEi/0yxIv9MsSL/AFWq//////////////////////+qVQD/TLEi/0yxIv9MsSL/ACuA/9T///////////////////////////////////////////////////////////////////////////+q/1UAAP9MsSL/TLEi/0yxIv9Vqv/////U/6pVK/8AK4D/1P//////////qlX/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/K4DU////////////////////qv9VAAD/TLEi/0yxIv9MsSL/AFWq//////////////////////+qVQD/TLEi/0yxIv9MsSL/ACuA/9T///////////////////////////////////////////////////////////////////////////+q/1UAAP9MsSL/TLEi/0yxIv9Vqv//////////////////////////////qlX/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/K4DU////////////////////qv9VAAD/TLEi/0yxIv9MsSL/AFWq//////////////////////+qVQD/TLEi/0yxIv9MsSL/ACuA/9T///////////////////////////////////////////////////////////////////////////+q/1UAAP9MsSL/TLEi/0yxIv9Vqv//////////////////////////////qlX/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/K4DU////////////////////qv9VAAD/TLEi/0yxIv9MsSL/AFWq//////////////////////+qVQD/TLEi/0yxIv9MsSL/ACuA/9T///////////////////////////////////////////////////////////////////////////+q/1UAAP9MsSL/TLEi/0yxIv9Vqv//////////////////////////////qlX/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/K4DU////////////////////qv9VAAD/TLEi/0yxIv9MsSL/AFWq//////////////////////+qVQD/TLEi/0yxIv9MsSL/ACuA/9T///////////////////////////////////////////////////////////////////////////+q/1UAAP9MsSL/TLEi/0yxIv9Vqv//////////////////////////////qlX/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/K4Cq/9TU1P/U1NT/1NTU/9TUqv9VAAD/TLEi/0yxIv9MsSL/AFWq/9TU1P/U1NT/1NTU/9TU1P+qVQD/TLEi/0yxIv9MsSL/ACuA/9T///////////////////////////////////////////////////////////////////////////+q/1UAAP9MsSL/TLEi/0yxIv8AACv/Kysr/ysrK/8rKyv/Kysr/ysrK/8rAAD/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/ACuA/9T///////////////////////////////////////////////////////////////////////////+q/1UAAP9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/ACuA/9T///////////////////////////////////////////////////////////////////////////+q/1UAAP9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/ACuA/9T///////////////////////////////////////////////////////////////////////////+q/1UAAP9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/AABV/6r/////////////////qv9VAAD/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/TLEi/0yxIv9MsSL/ACuA/9T///////////////////////////////////////////////////////////////////////////+q/1UrK/8rKyv/Kysr/ysrK/8rKyv/Kysr/ysrK/8rKyv/Kysr/ysrK/8rKyv/Kysr/ysrK/8rKyv/KytV/6r/////////////////1P/Uqqr/qqqq/6qqqv+qqqr/qqqq/6qqqv+qqqr/qqqq/6qqqv+qqqr/qqqq/6qqqv+qqqr/qqqq/6qqqv+qqqr/qqqq/6qqqv+qqqr/qqqq/6qqqv+qqqr/qqrU//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=="
ICON_PATH = PWD + "\\icon.ico"

check_file_run = open(PWD + '\\my_keyboard_sound.lock', "a+")
try:  
  portalocker.lock(check_file_run, portalocker.LOCK_EX | portalocker.LOCK_NB)
except:
  messagebox.showinfo(title='',message="【肥鍵盤打字聲】已執行...")    
  sys.exit(0)

# Preset play music
is_play_music = True
# Debug 模式
is_DEBUG_mode = False

NOW_VOLUME = 500 #預設音量

wavs = my.glob(PWD + "\\*.wav")
o_song = {}
m_play_song = []
max_thread___playMusic_counts = 3 #最多同時五個執行緒在作動
step_thread___playMusic_counts = 0 #目前0個執行緒
for i in range(0,len(wavs)):
  #from : https://pythonbasics.org/python-play-sound/
  #m_song.extend([ AudioSegment.from_wav(wavs[i]) ])
  o_song[ wavs[i] ] = {
                        "lastKey": None,
                        "mainname" : my.mainname(wavs[i]).lower(),
                        "filename":wavs[i],
                        "data":[],
                        "wf":"",
                        "paudio_stream":""      
                      }
  if o_song[ wavs[i] ]["mainname"] == "enter" or o_song[ wavs[i] ]["mainname"] == "return":
    o_song[ wavs[i] ]["lastKey"]=13;
  elif o_song[ wavs[i] ]["mainname"] == "delete" or o_song[ wavs[i] ]["mainname"] == "del":
    o_song[ wavs[i] ]["lastKey"]=46;
  elif o_song[ wavs[i] ]["mainname"] == "backspace" or o_song[ wavs[i] ]["mainname"] == "bs":
    o_song[ wavs[i] ]["lastKey"]=8;
  elif o_song[ wavs[i] ]["mainname"] == "space" or o_song[ wavs[i] ]["mainname"] == "sp":
    o_song[ wavs[i] ]["lastKey"]=32;
#print(my.json_encode(o_song))
def play_sound():
  global is_play_music
  global m_play_song
  global max_thread___playMusic_counts
  global step_thread___playMusic_counts
  global NOW_VOLUME
  global o_song
  global PWD
  
  m_play_song.extend( [ random.choice(o_song.keys()) ])
  if len(o_song.keys())!=0 and step_thread___playMusic_counts < max_thread___playMusic_counts:
    step_thread___playMusic_counts = step_thread___playMusic_counts + 1                  
    
    thread.start_new_thread( thread___playMusic,(NOW_VOLUME,))
                            
def thread___playMusic(keyboard_valume):
  global lastKey
  global PWD
  try:
    # https://stackoverflow.com/questions/43679631/python-how-to-change-audio-volume
    # 調整聲音大小
    # https://stackoverrun.com/cn/q/10107660
    # Last : https://www.thinbug.com/q/45219574
    global paudio_player
    global o_song
    global m_play_song
    global step_thread___playMusic_counts     
    global lastKey                 
    if len(m_play_song) !=0 :      
      # https://stackoverflow.com/questions/36664121/modify-volume-while-streaming-with-pyaudio
      chunk = 2048
      #s = random.choice(m_song)
      #print(my.json_encode(m_play_song))                    
      #m_play_song = m_play_song[ : 2]
      #s = m_play_song.pop(0) #m_play_song[0]   

      #print("lastKey")
      #print(lastKey)      
      s = ""
      if my.in_array(lastKey,[13,46,32,8]):
        for key in o_song:
          #print("Key")
          #print(key)
          #print(o_song[key]["lastKey"])
          if o_song[key]["lastKey"]!=None and o_song[key]["lastKey"] == lastKey:
            s = key
            #print("s")
            #print(s)  
            break;     
      else:
        _arr = []
        for key in o_song:
          if o_song[key]["lastKey"]==None:
            _arr.append(key)
          pass
        s = _arr[my.rand(0,len(_arr)-1)]
        
      #print(my.json_encode(s))      
      #return     
      if len(o_song[s]["data"]) == 0 or o_song[s]["volume"] != keyboard_valume:        
        o_song[s]["volume"] = keyboard_valume
        o_song[s]["data"] = []
        o_song[s]["wf"] = wave.open(s, 'rb')
        o_song[s]["paudio_stream"] = paudio_player.open(format = paudio_player.get_format_from_width(o_song[s]["wf"].getsampwidth()),
                      channels = o_song[s]["wf"].getnchannels(),
                      rate = o_song[s]["wf"].getframerate(),
                      output = True)
        # 寫聲音檔輸出來播放
        while True:
          d = o_song[s]["wf"].readframes(chunk)
          if d == "": break      
          # 這是調整音量大小的方法
          o_song[s]["data"].extend([ audioop.mul(d, 2, keyboard_valume / 100.0 ) ])                    
      for i in range(0,len(o_song[s]["data"])):
        o_song[s]["paudio_stream"].write(o_song[s]["data"][i])
    if step_thread___playMusic_counts > 0:
      step_thread___playMusic_counts = step_thread___playMusic_counts -1         
  except Exception as e:
    thread___playMusic(keyboard_valume)
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

# From : https://github.com/Infinidat/infi.systray

    
# From : https://github.com/gevasiliou/PythonTests/blob/master/TrayAllClicksMenu.py

class TrayIcon():
    systray = ""
    def __init__(self):
      global VERSION
      global PWD
      global UCL_PIC_BASE64
      global my
      global ICON_PATH
      # base64.b64decode
      # From : https://sourceforge.net/p/matplotlib/mailman/message/20449481/
      raw_data = base64.decodestring(UCL_PIC_BASE64)      
      #if my.is_file(ICON_PATH) == False:
      my.file_put_contents(ICON_PATH,raw_data,False)
      self.reload_tray()
   
    def reload_tray(self):
      global is_play_music
      global ICON_PATH
      global NOW_VOLUME            
      menu_options = (
          ("1.關於肥鍵盤打字聲", None, [self.m_about] ),
          
        )
      if is_play_music==True:
        menu_options = menu_options + (("2.【●】打字音", None, [self.m_pm_switch]),)
      else:
        menu_options = menu_options + (("2.【　】打字音", None, [self.m_pm_switch]),)
      
      # 接下來作打字音
      sound_level_list = ()
      for i in range(0,11):        
        v = i*10
        real_v = i*100        
        is_o = "　"
        if NOW_VOLUME == real_v:
          is_o = "●"
        if i == 0:
          sound_level_list = sound_level_list + (('【%s】靜音' % (is_o) , None, [self.m_change_volume,real_v] ),)
        else:
          sound_level_list = sound_level_list + (("【%s】%s %%" % (is_o,v), None, [self.m_change_volume,real_v]),)
                                                     
      menu_options = menu_options + ((
                ('3.打字音大小', None, sound_level_list),))
        
      menu_options = menu_options + (("離開(Quit)", None, [self.m_quit]),)
      if self.systray=="":
        self.systray = SysTrayIcon(ICON_PATH, "肥鍵盤打字聲 V%s" % (VERSION) , menu_options) #, on_quit=self.m_quit)
        self.systray.start()
      else:
        #self.systray = SysTrayIcon(ICON_PATH, "肥鍵盤打字聲 V %s" % (VERSION) , menu_options)
        self.systray.update(menu_options=menu_options)        
    def m_about(self,event,data=None):  # if i ommit the data=none section python complains about too much arguments passed on greetme      
      _msg_text = about_my_keyboard_sound()       
      messagebox.showinfo(title="肥鍵盤打字機",message=_msg_text)  
    def m_pm_switch(self,event,data=None):
      global is_play_music
      if is_play_music == False:
        is_play_music = True
      else:
        is_play_music = False  
      self.reload_tray()   
    def m_quit(self,event,data=None):
      
      self.systray.shutdown()            
      sys.exit()
    def m_none(self,data=None):
      return False
    def m_change_volume(self,event,new_volume):
      global NOW_VOLUME      
      NOW_VOLUME = new_volume[0]      
      #然後播一下新的聲音大小
      play_sound()
      self.reload_tray()               
   
lastKey = None
def OnKeyboardEvent(event):
  global lastKey
  try:
    #print(event.KeyID);
    if is_play_music == True and event.MessageName == "key down":      
      if lastKey != event.KeyID:
        lastKey = event.KeyID   
        play_sound()
    if is_play_music == True and event.MessageName == "key up":
      lastKey = None
  except:
    pass
  return True
# create a hook manager
hm = pyHook.HookManager()
# watch for all mouse events
hm.KeyAll = OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# generator tray
tray = TrayIcon()  
# wait forever    
pythoncom.PumpMessages()