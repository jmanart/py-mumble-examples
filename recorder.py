import io
import wave
import pymumble_py3
import readline
from pymumble_py3.callbacks import PYMUMBLE_CLBK_SOUNDRECEIVED as PCS
from time import sleep

CHUNK = 1024

server = ""
pwd = "recorder"  # password
nick = "recorder" # username
port = 64738  # port number

outputFilename = "./output.wav"
output = wave.open(outputFilename, "w")
output.setnchannels(1)
output.setsampwidth(2)
output.setframerate(48000)

def sound_receive_handler(user, soundchunk):
    output.writeframesraw(soundchunk.pcm)

mumble = pymumble_py3.Mumble(server, nick, password=pwd, port=port)
mumble.callbacks.set_callback(PCS, sound_receive_handler)
mumble.set_receive_sound(1)
mumble.start()
mumble.is_ready()  # Wait for client is ready

print("server ready")

for timeout in range(0, 10):
    sleep(1)

output.close()

print("done writting")
