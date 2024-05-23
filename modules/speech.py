import speech_recognition as sr


def recognize_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print(f"\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            # Timeout after 5 seconds
            audio = recognizer.listen(source, timeout=5)
            print(f"\nRecognizing...")
            text = recognizer.recognize_google(audio)
            print(f"\nRecognized: {text}")
            return text
        except sr.WaitTimeoutError:
            print(f"\nNo speech detected within 5 seconds")
            return None
        except sr.UnknownValueError:
            print(f"\nSorry, I could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"\nCould not request results.")
            return None
