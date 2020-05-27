# -*- coding: utf-8 -*-
###########################################
#  Auther:FeatherMountain(http://3wa.tw)  #
#  Version: 1.3_Custom                    #
#  Date: 2016-09-21                       #
#  License: LGPLv3                        #
###########################################
# # how to :
# import include
# my = include.kit()
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
class kit:           
    def __init__(self):
        pass    
    def is_file(self,filename):
        import os
        return os.path.isfile(filename)        
    def file_put_contents(self,filename,data,IS_APPEND=False):
        f = "";
        if IS_APPEND==True:
          f = open(filename, 'a');
        else:
          f = open(filename, 'wb');
        f.write(data)
        f.close()                                          
    def glob(self,pathdata):
        import glob
        return glob.glob(pathdata)