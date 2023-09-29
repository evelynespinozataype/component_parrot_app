# import required module
from pydub import AudioSegment
from pydub.playback import play

audio_file_ah1 = "audio/parrot_ahah1.mp3"
audio_file_ah2 = "audio/parrot_ahah2.mp3"
audio_file_hi = "audio/parrot_hola.mp3"
audio_file_rr1 = "audio/parrot_rrr1.mp3"
audio_file_rr2 = "audio/parrot_rrr2.mp3"
audio_file_rr3 = "audio/parrot_rrr3.mp3"
audio_file_sil = "audio/parrot_silvido.mp3"

def happy_emotion(emotional_state):
    # emotional_state = 2
    if emotional_state == 1:
        song = AudioSegment.from_mp3(audio_file_ah1)
    if emotional_state == 2:
        song = AudioSegment.from_mp3(audio_file_ah2)
    if emotional_state == 3:
        song = AudioSegment.from_mp3(audio_file_sil)
    if emotional_state == 4:
        song = AudioSegment.from_mp3(audio_file_sil)
    if emotional_state == 5:
        song = AudioSegment.from_mp3(audio_file_sil)
    if emotional_state == 6:
        song = AudioSegment.from_mp3(audio_file_sil)
    if emotional_state == 7:
        song = AudioSegment.from_mp3(audio_file_sil)
    print('playing sound using  pydub')
    play(song)

