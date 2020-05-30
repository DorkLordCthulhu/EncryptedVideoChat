import socket
import sys
import cv2
import wave
import pyaudio

class Video:

    def socketing(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((input(), 1234))
        msg = s.recv(1024)



    def display():
        capture = cv2.VideoCapture(0)
        while True:
            returned, frame = capture.read()
            cv2.imshow('Live Feed', frame)
            key = cv2.waitKey(1)
            if key in [27,8,113]:
                break
        capture.release()
        cv2.destroyAllWindows()

    def audio():
        bytechunk = 1024
        wavframe = wave.open(sys.argv[0], 'rb')
        player = pyaudio.PyAudio
        stream = player.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)
        data =wavframe.readframes(bytechunk)
        while len(data)>0:
            stream.write(data)
            data = wavframe.readframes(bytechunk)
            key = cv2.waitKey(1)
            if key in [27, 8, 113]:
                break
        stream.stop_stream()
        stream.close()
        player.terminate()


if __name__== '__main__':
    x = Video
    x.display()
    x.audio()
