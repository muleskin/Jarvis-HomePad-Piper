from openai import OpenAI
import time
#from pygame import mixer
import os
from dotenv import load_dotenv
from piper.voice import PiperVoice
import numpy as np
import sounddevice as sd
import soundfile as sf
import wave


# Load environment variables from .env file
load_dotenv()

#https://platform.openai.com/playground/assistants
# Initialize the client and mixer
client = OpenAI(default_headers={"OpenAI-Beta": "assistants=v2"}, api_key= os.getenv('API_KEY'))
#mixer.init()
filename = './temp.wav'
voicedir = os.path.expanduser('./')
model = voicedir+"en_US-kristin-medium.onnx"
voice = PiperVoice.load(model)

# Retrieve the assistant and thread
assistant = client.beta.assistants.retrieve(os.getenv('ASSISTANT_ID'))
thread = client.beta.threads.retrieve(os.getenv('THREAD_ID'))

def ask_question_memory(question):
    global thread
    client.beta.threads.messages.create(thread.id, role="user", content=question)
    run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=assistant.id)
    
    while (run_status := client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)).status != 'completed':
        if run_status.status == 'failed':
            return "The run failed."
        time.sleep(1)
    
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    #print(messages)
    return messages.data[0].content[0].text.value

def generate_tts(sentence, speech_file_path):
    wav_file = wave.open(filename, 'w')
    audio = voice.synthesize(sentence,wav_file)
    data, fs = sf.read(filename, dtype='float32')
    #response = client.audio.speech.create(model="tts-1", voice="echo", input=sentence)
    #response.stream_to_file(speech_file_path)
    return str(filename)

def play_sound(file_path):
    data, fs = sf.read(filename, dtype='float32')
    sd.play(data, fs)
    status = sd.wait()  # Wait until file is done playing
    os.remove(filename)
    return "done"

def TTS(text):
    wav_file = wave.open(filename, 'w')
    audio = voice.synthesize(text,wav_file)
    data, fs = sf.read(filename, dtype='float32')
    sd.play(data, fs)
    status = sd.wait()  # Wait until file is done playing
    os.remove(filename)
    #speech_file_path = generate_tts(text, "speech.mp3")
    #play_sound(speech_file_path)
    #while mixer.music.get_busy():
    #    time.sleep(1)
    #mixer.music.unload()
    #os.remove(speech_file_path)
    return "done"

# question = "make it slightly vary every time"
# response = ask_question_memory(question)
# print(response)
