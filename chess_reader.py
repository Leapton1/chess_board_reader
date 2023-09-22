import gtts
from playsound import playsound
import time
import os

rawfile="rr/ppp"
newfile=""
coords=[1,8]

def numtoletter(num):
    if num==1:
        return "a"
    elif num==2:
        return "b"
    elif num==3:
        return "c"
    elif num==4:
        return "d"
    elif num==5:
        return "e"
    elif num==6:
        return "f"
    elif num==7:
        return "g"
    elif num==8:
        return "h"

for rawletter in rawfile:
    if rawletter=="/":
        coords[0]=1
        coords[1]-=1
    elif rawletter.isdigit():
        coords[0]+=int(rawletter)
    elif rawletter=="r":
        newfile="rook "
        newfile+=numtoletter(coords[0])+" "+str(coords[1])
        print(newfile)
        tts = gtts.gTTS(newfile)
        tts.save("./hello.mp3")
        playsound("./hello.mp3")
        os.remove("./hello.mp3")
        coords[0]+=1
    elif rawletter=="p":
        newfile="pawn "
        newfile+=numtoletter(coords[0])+" "+str(coords[1])
        print(newfile)
        tts = gtts.gTTS(newfile)
        tts.save("./hello.mp3")
        playsound("./hello.mp3")
        os.remove("./hello.mp3")
        coords[0]+=1
    print(coords)
    time.sleep(1)


#tts = gtts.gTTS(newfile)
#tts = gtts.gTTS("ooga booga booga booga, eega dooga donga dinga")
#tts.save("hello.mp3")
#playsound("hello.mp3")