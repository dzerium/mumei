from datetime import datetime

class Tweet(object):
    
    def __init__(self, id_str, author, date, content):
        self.__id_str = id_str 
        self.__author = author
        self.__date = date
        #dt = datetime.strptime(date, "%a %b %d %I:%M:%S")
        #self.__date = dt.strftime("%A, %d. %B %Y %I:%M%p")
        self.__content = content

    def get_message(self): 
        msg = " Tweet from {} on {}. {}".format(self.__author, self.__date, self.__content)
        return msg

    def id_str(self):
        return self.__id_str
