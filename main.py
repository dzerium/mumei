from gtts import gTTS
import os



if __name__ == '__main__':
    tts = gTTS(text="Hello Badong", lang='en')
    tts.save("audio.mp3")

    if (os.name == 'nt'):
# Windows OS
        os.system("audio.mp3")
    else:
# Linux
        os.system('mpg321 audio.mp3 -quiet')
