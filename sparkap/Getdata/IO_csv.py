'''
Created on 07-Oct-2016

@author: shubham
'''
import os
import csv
from collections  import namedtuple
from _sqlite3 import Row
class IO_csv(object):
    def __init__(self,filepath,filename,filesuffix):
         self.filepath=filepath
         self.filename=filename
         self.filesuffix=filesuffix
    def save(self,data,NTname,fields):
        
        NTuple=namedtuple(NTname,fields)
        if os.path.isfile('%s/%s.%s'%(self.filepath,self.filename,self.filesuffix)):
            f=open("%s/%s.%s"%(self.filepath,self.filename,self.filesuffix),"ab+")
            writer=csv.writer(f)
            writer.writerow(fields)
            writer.writerows([row for row in map(NTuple._make,data)])
            
        else:
            f=open("%s/%s.%s"%(self.filepath,self.filename,self.filesuffix),"ab+")
            writer=csv.writer(f)
            writer.writerow(fields)
            writer.writerows([row for row in map(NTuple._make,data)])
             
    def load(self,NTname,fields):
        NTuple=namedtuple(NTname,fields)
        f=open("%s/%s.%s"%(self.filepath,self.filename,self.filesuffix),"ab+")
        reader=csv.reader(f)
        for row in map(NTuple._make,reader):
            yield row
    fields01    =    ['id',    'created_at',    'user_id',    'user_name',    'tweet_text',    
'url']
    Tweet01 =namedtuple('Tweet01',fields01)
    def parsetweet(self,data,Tweet01):
           
            return Tweet01(id=data.get('id',    None),
                              created_at=data.get('created_at',    None),
                              user_id=data.get('user_id',    None),
                              user_name=data.get('user_name',    None),
                              tweet_text=data.get('tweet_text',    None),
                              url=data.get('url'))         
            
            