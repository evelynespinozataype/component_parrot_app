# import required module
from pydub import AudioSegment
from pydub.playback import play

audio_file_0 = "parrot_ahah1.wav"

# for playing mp3 file
song = AudioSegment.from_mp3(audio_file_0)
print('playing sound using  pydub')
play(song)