import os
import time
import gtts
from playsound import playsound

fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

def letter(num):
    return "abcdefgh"[num - 1]

def phoneme(num):
    return ["ay", "b",  "c", "d", "e", "f",  "g", "h"][num - 1]

def colour(piece):
    if piece.islower():
        return "black"
    return "white"

def say(text):
    tts = gtts.gTTS(text)
    tts.save("./speech.mp3")
    playsound("./speech.mp3")
    os.remove("./speech.mp3")


def main():
    coords = [1, 8]
    for character in fen:
        if character == "/":
            coords[0] = 1
            coords[1] -= 1
        elif character.isdigit():
            coords[0] += int(character)
        elif character in "kK":
            say(colour(character) + " king " + phoneme(coords[0]) + " " + str(coords[1]))
            coords[0] += 1
        elif character in "qQ":
            say(colour(character) + " queen " + phoneme(coords[0]) + " " + str(coords[1]))
            coords[0] += 1
        elif character in "rR":
            say(colour(character) + " rook " + phoneme(coords[0]) + " " + str(coords[1]))
            coords[0] += 1
        elif character in "bB":
            say(colour(character) + " bishop " + phoneme(coords[0]) + " " + str(coords[1]))
            coords[0] += 1
        elif character in "nN":
            say(colour(character) + " knight " + phoneme(coords[0]) + " " + str(coords[1]))
            coords[0] += 1
        elif character in "pP":
            say(colour(character) + " pawn " + phoneme(coords[0]) + " " + str(coords[1]))
            coords[0] += 1
        time.sleep(1)

main()
