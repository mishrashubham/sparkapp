'''
Created on 19-Sep-2016

@author: shubham
'''
import twitter
import urlparse
from pprint import pprint as pp
class twitterapi(object):
   


    def __init__(self):
       self.api = twitter.Api(consumer_key='nvsoUdCvSyntUf9TKL6WWTn9d',
       consumer_secret='MhqcxvD19W5euqXIl3OUtXcS45HmsTanX92R0bM6DzKuOHj3gc',
       access_token_key='722662494259527680-fLfbBfFKEuyU8NBdVATKJT4JqafVAbS',
       access_token_secret='VeistBoKbAJCEpIIvaxoNAIAW9lMwaFcQbY6xem9RaCuS')
      
    def searchTwitter(self,q,max_res=10):
        search_results=self.api.GetSearch(q,count=10)
        #print search_results
        for i in search_results:
             print "%s\n"%i
        return search_results
    
    def parserdata(self,q,max_res):
        statuses=self.searchTwitter(q)
        parsedata=[]
        for i in statuses:
          try:
            parsedata.append((i.created_at,i.id,i.user_mentions[0].id,i.user_mentions[0].name,i.text,i.urls[0].expanded_url))
          except IndexError:
              continue
          
              
        return parsedata
            
if __name__=="__main__":
    t1=twitterapi()
    q="Hive"
    p=t1.parserdata(q,10)
    for y in p:
        print y
    

        
