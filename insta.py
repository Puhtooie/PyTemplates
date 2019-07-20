https://medium.com/@dvoiak.stepan/https-medium-com-dvoiak-stepan-instagram-analitics-with-unofficial-api-ipython-and-matplotlib-a9f3f8b2b16a
https://github.com/oyvsyo/insta_play/blob/master/analys.ipynb?source=post_page---------------------------media_ids = []
from InstagramAPI import InstagramAPI
import time
import pandas as pd

class InstaAcct:

    def __init__(self):
        self.insta = InstagramAPI("username", "password")
        self.insta.login()
        self.acctData = pd.Series({'my_id':self.getUserId()})

    def getUserId(self):
        self.insta.getProfileData()
        return self.insta.LastJson['user']['pk']

    def getMediaCount(self):
        self.insta.getUsernameInfo(self.acctData.my_id)
        self.acctData.n_media =  self.insta.LastJson['user']['media_count']

    def getMaxID(self):
        self.getMediaCount()

        media_ids = []
        max_id = ''
        n_m = self.acctData.n_media
        available = True
        while available and n_m > 0:
            n = n_m/18+1
            for i in range(int(n)): 
                self.insta.getUserFeed(usernameId=self.acctData.my_id, maxid = max_id)
                media_ids += self.insta.LastJson['items'] 
                if self.insta.LastJson['more_available']==False:
                    print("no more id's avaliable")
                    available = False
                    break
                max_id = self.insta.LastJson['next_max_id'] 
                print(i, "   next media id = ", max_id, "  ", len(media_ids))
                time.sleep(3)
            n_m -=18
        self.acctData.media_ids = media_ids



    def getAllLikes(self):
        self.getMaxID()
        likers = []
        m_id = 0
        print("wait %.1f minutes" % (self.acctData.n_media*2/60.))
        for i in range(len(self.acctData.media_ids)):
            m_id = self.acctData.media_ids[i]['id']
            self.insta.getMediaLikers(m_id)
            likers += [self.insta.LastJson]
            time.sleep(2)
        print("likes query done!")    
        self.acctData.likers = likers


    def getUserLikeSet(self):

        self.getAllLikes()
        users = []
        for i in self.acctData.likers:
                users += map(lambda x: i['users'][x]['username'],
                             range(len(i['users'])))
        users_set = set(users)

        print("all users = ", len(users), " uniqum users = ", len(users_set))

        l_dict = {}
        for user in users_set:
            # l_dict structure - {username:number_of_liked_posts} 
            l_dict[user] = users.count(user)
        self.acctData.l_dict = l_dict



    def sortLikes(self):
        import operator
        self.getUserLikeSet()
        all_pairs = sorted(self.acctData.l_dict.items(), key=operator.itemgetter(1))
        n_users = 10 # top 10 users
        pairs = all_pairs[-n_users:]
        y=[]
        x=[]
        for i in range(len(pairs)):
            y.append(pairs[i][1])
            x.append(pairs[i][0])
        return [x,y,pairs]


    def plotLikes(self):
        import matplotlib.pyplot as plt
        from matplotlib.ticker import FormatStrFormatter

        x,y,pairs = self.sortLikes()

        fig = plt.figure()
        plt.xkcd()
        plt.xticks(range(len(pairs)), x, rotation='vertical')
        plt.ylim([int(min(y) - min(y) * .25), int(max(y) + max(y) * .25)])
        plt.bar(range(len(pairs)), y)
        plt.xlabel('USERS')
        plt.ylabel('number of liked posts')
        plt.show()


