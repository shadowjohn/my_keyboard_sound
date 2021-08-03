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
    def basename(self,path):
        import os
        _output = "";
        if self.is_file(path):
          _output = os.path.basename(path)
        else:
          m = self.explode(self.SP(),path)
          _output = m[self.count(m)-1]
        return _output            
    def mainname(self,path):
        import os
        return os.path.splitext(self.basename(path))[0]
    def in_array(self, needle,arr):
        return ( needle in arr )        
    #def json_encode(self,dict_data):
    #    import json
    #    return json.dumps(dict_data); #, ensure_ascii=False);
    def rand(self,start_int,end_int):
        import random
        return random.randint(start_int,end_int)