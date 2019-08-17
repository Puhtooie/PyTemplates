#https://medium.com/@dvoiak.stepan/https-medium-com-dvoiak-stepan-instagram-analitics-with-unofficial-api-ipython-and-matplotlib-a9f3f8b2b16a
#https://github.com/oyvsyo/insta_play/blob/master/analys.ipynb?source=post_page---------------------------media_ids = []

from InstagramAPI import InstagramAPI
import json
import time
import pandas as pd


class InstaAcct:

    def __init__(self, user_name=None, pswd=None, ppg=False,
                 api=None, acctData=None, g=None, login=True):
        # make proxies an obj containing all the proxies to send and recieve signals from

        a = type(None)
        if login and a != type(pswd):
            # this instantiates the parent class
            # must include user_name and pswd
            self.insta = InstagramAPI(user_name, pswd)
            self.insta.login()

            self.getUserId()
            self.get_follows()


        elif a != type(api):
            # instantiates the child class. include api, acctData
            self.insta = api
            self.get_acct_Data(acctData)
            print(acctData)

            if self.acctData['is_private'] == False:
                self.get_follows()
            time.sleep(2)

        else:
            raise ValueError('Value of %r in Pswd, %r in api' % (pswd, api))

    def getUserId(self):

        self.insta.getProfileData()
        a = self.insta.LastJson['user']
        self.insta.getUsernameInfo(a['pk'])
        self.acctData = pd.DataFrame(self.insta.LastJson)
        self.acctData = self.acctData.user
        time.sleep(1)

    def get_acct_Data(self, acctData):

        self.insta.getUsernameInfo(acctData['pk'])
        self.acctData = pd.Series(inst.insta.LastJson)
        if 'user' in self.acctData:
            self.acctData = self.acctData.user

    def get_follows(self):
        time.sleep(1)
        self.followers = pd.DataFrame(self.insta.getTotalFollowers(self.acctData['pk']))
        time.sleep(1)
        self.followings = pd.DataFrame(self.insta.getTotalFollowings(self.acctData['pk']))

        
        
    def getFollowersData(self,ppg = False, chain = False):

        for i in range(len(self.followers.pk)):

            name = self.followers.iloc[i]['username']
            if name not in users.keys():

                self.followers.iloc[i] = InstaAcct(api=self.insta, 
                                               acctData=self.followers.iloc[i])
                users[name]= self.followers.iloc[i]
                users[name]= self.followers.iloc[i].pk
                time.sleep(1)
            else:
                self.followers.iloc[i] = users[name]

        self.followers = self.followers.pk
        
        if ppg:
            if chain:
                for i in self.followers.keys():
                    self.followers[i].getFollowersData(ppg = True, chain = True)
            else:
                for i in self.followers.keys():
                    self.followers[i].getFollowersData()


     
if __name__ == '__main__':
    inst = InstaAcct(user_name = username, pswd = pswd, ppg=True)
    users = {}
    users[inst.acctData.username] = inst
    '''
    to propegate data only for the parent node's followers - inst.getFollowersData()
    to propegate data through to the followers of the parent node's followers inst.getFollowersData(ppg= True)
    to pull all available public nodes through parent node inst.getFollowersData(ppg= True, chain = True)
    '''
    inst.getFollowersData(ppg= True)

