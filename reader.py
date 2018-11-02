import threading
import os
import subprocess
import queue
from gtts import gTTS
from tweet import Tweet

G_QUEUE_MAX_SIZE = 0

class Reader(object): 

    def __init__(self):
        self.__running = True
        self.__read_queue = queue.Queue(G_QUEUE_MAX_SIZE)
        self.__write_queue = queue.Queue(G_QUEUE_MAX_SIZE)

        self.__read_thread = threading.Thread(target=self.__read_audio)
        self.__write_thread = threading.Thread(target=self.__write_audio)

        self.__read_thread.start()
        self.__write_thread.start()
    #end __init__

    def stop(self):
        self.__running = False
        self.__write_thread.join()
        self.__read_thread.join()

    def write_enqueue(self, message):
        if self.__write_queue.full() is not True:
            self.__write_queue.put(message)
    #end

    def __read_audio(self):
        while self.__running == True:
            if self.__read_queue.empty() == False:
                audio_file = self.__read_queue.get()
                print(audio_file)
                if (os.name == 'nt'):
                    p = subprocess.Popen((audio_file,))
                else:
                    p = subprocess.Popen(('mpg321 ' + audio_file + ' -quiet',))
                p.wait()
    # end __read_audio



    def __write_audio(self): 
        while self.__running == True: 
            if self.__write_queue.empty() == False:
                item = self.__write_queue.get()
                print(item.get_message())
                tts = gTTS(text=item.get_message(), lang='en')
                tts.save(item.id_str() + '.mp3')
                self.__read_queue.put(item.id_str() + '.mp3')