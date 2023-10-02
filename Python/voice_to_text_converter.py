import speech_recognition as sr

def convert_voice_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")

        try:
            audio = recognizer.listen(source, timeout=5)
            print("Processing...")

            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")

        except sr.WaitTimeoutError:
            print("Listening timed out. Please try again.")

        except sr.RequestError as e:
            print(f"Could not request results; check your network connection: {e}")

        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")

if __name__ == "__main__":
    convert_voice_to_text()
