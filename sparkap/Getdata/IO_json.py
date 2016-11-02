'''
Created on 07-Oct-2016

@author: shubham
'''
import os
import io
import json
class IO_json(object):
    def __init__(self,filepath,filename,filesuffix):
         self.filepath=filepath
         self.filename=filename
         self.filesuffix=filesuffix
         
         
    def save(self,data):
        if os.path.isfile('%s/%s.%s'%(self.filepath,self.filename,self.filesuffix)):
            f=io.open("%s/%s.%s"%(self.filepath,self.filename,self.filesuffix),"ab+",encoding='utf-8')
        
            f.write(unicode(json.dumps(data,    ensure_ascii=    False)))
        else:
           f=io.open("%s/%s.%s"%(self.filepath,self.filename,self.filesuffix),"ab+",encoding='utf-8')
        
           f.write(unicode(json.dumps(data,    ensure_ascii=    False))) 
    def load(self,data):
         f=io.open("%s/%s.%s"%(self.filepath,self.filename,self.filesuffix),"ab+",encoding='utf-8')
         return    f.read()