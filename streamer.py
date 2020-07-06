import io
from pydub import AudioSegment
import pymumble_py3
import readline


CHUNK = 1024 # size of the chunk being captured each time

server = ""
pwd = "streamer"  # password
nick = "streamer" # username
port = 64738  # port number

filename = "./input.wav" # audio being transmited
wf = AudioSegment.from_file(filename, format="wav")

mumble = pymumble_py3.Mumble(server, nick, password=pwd, port=port)
mumble.start()
mumble.is_ready()  # Wait for client is ready

print("server ready")

s = " "
while s: # if there is input text we play
    bf = io.BytesIO(wf.raw_data)
    data = bf.read(CHUNK)
    while len(data) > 0:
        mumble.sound_output.add_sound(data)
        data = bf.read(CHUNK)
    s = input(">")

print("done with the data")
