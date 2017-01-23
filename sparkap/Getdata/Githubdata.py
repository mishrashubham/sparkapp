'''
Created on 19-Sep-2016

@author: shubham
'''
from github import Github
from pprint import pprint as pp
class githubapi(object):

    def __init__(self,user,repo):
       ACCESS_TOKEN="dce09ea4b555192cd85f2a7e6c3d7aa7f1e7703b"
       USER="%s"%user
       REPO="%s"%repo
       self.g=Github(ACCESS_TOKEN,per_page=100)
       #print self.g
       self.user=self.g.get_user(USER)
       self.repo=self.user.get_repo(REPO)
       
    def process(self):
        repos_apache=[repo.name for repo in self.user.get_repos()]
        #print repos_apache
        lang=self.repo.get_languages()
        print len(lang)
        stargazers=[s for s in self.repo.get_stargazers()]
        try:
          k=[stargazers[i].login for i in range(0,20)]
        except :
            k=stargazers#print k
        return len(repos_apache),lang,len(lang),k
if __name__=="__main__":
    user_name=raw_input("enter the user name of the repository")
    repo_name=raw_input("enter the name of the repo")
    t1=githubapi(user_name,repo_name)

    a,b,c,d=t1.process()
    print "active apache repos:",a
    print "active languages:",b 
    print "active languages in which apache commit is done",c
    print "stargazer commitors:",d
