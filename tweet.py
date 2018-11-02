from datetime import datetime

class Tweet(object):
    
    def __init__(self, id_str, author, date, content):
        self.__id_str = id_str 
        self.__author = self.__author_update(author)
        self.__date = date
        #dt = datetime.strptime(date, "%a %b %d %I:%M:%S %z %Y")
        #self.__date = dt.strftime("%A, %d. %B %Y %I:%M%p")
        self.__content = content

    def get_message(self): 
        msg = " Tweet from {} {}".format(self.__author, self.__content)
        return msg

    def id_str(self):
        return self.__id_str

    def __author_update(self, author):
        if author == "BPItrade": 
            return 'B-P-I-Trade'
        return author
