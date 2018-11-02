from gtts import gTTS
import os
import twitter
from reader import Reader
from tweet import Tweet

G_CONSUMER_KEY = 'DfaKNLkzFPbDqmItGJMdgy2Ae'
G_CONSUMER_SECRET_KEY = 'WpI2UxKxj6bnXJU7uLIG8iEd0PI8KDvlQoBzdleRg84dyvcg5x'
G_ACCESS_TOKEN = '1057990046110769152-VorCriYpORNDvKKbRVffIwk5vr8xSn'
G_ACCESS_TOKEN_SECRET = 'ALbNpZbQrg7DIGRYctrAS5g56pgo6Hf8gylOrtkAeaHsg'




if __name__ == '__main__':
    #tts = gTTS(text='Failure occured. Kindly contact Badong', lang='en')
    #tts.save('fail.mp3')
    audio_read = Reader()
    api = twitter.Api(consumer_key=G_CONSUMER_KEY,
                      consumer_secret=G_CONSUMER_SECRET_KEY,
                      access_token_key=G_ACCESS_TOKEN,
                      access_token_secret=G_ACCESS_TOKEN_SECRET)
    try:
        api.VerifyCredentials()
    except:
        exit(0)

    users = api.GetFriends()
    for user in users:
        statuses = api.GetUserTimeline(screen_name=user.screen_name)
        for status in statuses:
            tweet = Tweet(status.id_str, user.screen_name, status.created_at, status.text)
            audio_read.write_enqueue(tweet)
        break

    audio_read.stop()
