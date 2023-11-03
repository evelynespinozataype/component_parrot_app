# import required module
from pydub import AudioSegment
from pydub.playback import play
from random import randrange
import time

emotion_parrot_ahah1='audio/1.emotion_parrot_ahah1.mp3'
emotion_parrot_ahah2='audio/2.emotion_parrot_ahah2.mp3'
emotion_parrot_fear='audio/3.emotion_parrot_fear.mp3'
emotion_parrot_sad_humhum='audio/4.emotion_parrot_sad_humhum.mp3'
emotion_parrot_sad1='audio/5.emotion_parrot_sad1.mp3'
emotion_parrot_sad2='audio/6.emotion_parrot_sad2.mp3'
emotion_parrot_sad3='audio/7.emotion_parrot_sad3.mp3'
emotion_parrot_sad4='audio/8.emotion_parrot_sad4.mp3'
emotion_parrot_anger='audio/9.emotion_parrot_anger.mp3'
interaction_parrot_hola='audio/10.interaction_parrot_hola.mp3'
interaction_parrot_rrr1='audio/11.interaction_parrot_rrr1.mp3'
interaction_parrot_rrr2='audio/12.interaction_parrot_rrr2.mp3'
interaction_parrot_rrr3='audio/13.interaction_parrot_rrr3.mp3'
interaction_parrot_silvido='audio/14.interaction_parrot_silvido.mp3'
interaction_parrot_sing='audio/15.interaction_parrot_sing.mp3'
interaction_parrot_talk='audio/16.interaction_parrot_talk.mp3'

print('playing sound using  pydub')

def start_parrot():
    song = AudioSegment.from_mp3(interaction_parrot_hola)
    play(song)

def emotion(emotional_state):
    

def interaction(interaction_state):
    state = randrange(3)
    if state == 0:
        song = AudioSegment.from_mp3(interaction_parrot_rrr1)
        play(song)
    if state == 1:
        song = AudioSegment.from_mp3(interaction_parrot_rrr2)
        play(song)
    if state == 2:
        song = AudioSegment.from_mp3(interaction_parrot_rrr3)
        play(song)
    state = randrange(3)
    if state == 0:
        song = AudioSegment.from_mp3(interaction_parrot_hola)
        play(song)
    if state == 1:
        song = AudioSegment.from_mp3(interaction_parrot_silvido)
        play(song)
    if state == 2:
        song = AudioSegment.from_mp3(interaction_parrot_sing)
        play(song)
    print("Interaction sound: ", interaction_state)