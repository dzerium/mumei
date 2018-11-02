import threading
import os
import queue
from gtts import gTTS
from tweet import Tweet

G_QUEUE_MAX_SIZE = 0

class Reader(object): 

    def __init__(self):
        self.__running = True
        self.__read_queue = queue.Queue(G_QUEUE_MAX_SIZE)
        self.__write_queue = queue.Queue(G_QUEUE_MAX_SIZE)
        self.read_thread = threading.Thread(target=self.__read_audio)
        self.write_thread = threading.Thread(target=self.__write_audio)

        self.read_thread.start()
        self.write_thread.start()
    #end __init__

    def stop(self):
        self.__running = False
        self.write_thread.join()
        self.read_thread.join()

    def write_enqueue(self, message):
        if self.__write_queue.full() is not True:
            self.__write_queue.put(message)
    #end

    def __read_audio(self):
        while self.__running == True:
            if self.__read_queue.empty() == False:
                audio_file = self.__read_queue.get()
                if (os.name == 'nt'):
                    os.system(audio_file)
                else:
                    os.system('mpg321 ' + audio_file + ' -quiet')
    # end __read_audio

    def __write_audio(self): 
        while self.__running == True: 
            if self.__write_queue.empty() == False:
                item = self.__write_queue.get()
                print(item.get_message())
                tts = gTTS(text=item.get_message(), lang='en')
                tts.save(item.id_str() + '.mp3')
                self.__read_queue.put(item.id_str() + '.mp3')