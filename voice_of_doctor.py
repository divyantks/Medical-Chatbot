#Step1: Setup Text to Speech–TTS–model with gTTS
import os 
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text,output_filepath):
    language="en"

    audioobj=gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)

# input_text="Hi This is Divyant"
# text_to_speech_with_gtts_old(input_text=input_text,output_filepath="gtts_testing.mp3")


#Step2: Use Model for Text output to Voice
import subprocess
import platform

def text_to_speech_with_gtts(input_text,output_filepath):
    language="en"

    audioobj=gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name=="Windows":
            wav_file="temp.wav"
            subprocess.run(["ffmpeg","-y","-i",output_filepath,wav_file])
            subprocess.run(["powershell","-c",f'(New-Object Media.SoundPlayer "{wav_file}").PlaySync();'])
            os.remove(wav_file)
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


# input_text="Hi This is Divyant,new version testing"
# text_to_speech_with_gtts(input_text=input_text,output_filepath="gtts_testing.mp3")