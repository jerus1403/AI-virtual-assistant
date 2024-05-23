import pyaudio
from openai import OpenAI
from config.settings import GPT_PIOT_API_KEY

client = OpenAI(api_key=GPT_PIOT_API_KEY)


def text_to_speech(text):
    print('Generating audio from text review using Open AI API')
    player_stream = pyaudio.PyAudio().open(
        format=pyaudio.paInt16, channels=1, rate=24000, output=True)

    with client.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice="onyx",
        input=text,
        response_format="wav"
    ) as response:
        print("Audio Response")
        for chunk in response.iter_bytes(chunk_size=1024):
            player_stream.write(chunk)
