import speech_recognition 

recognizer = speech_recognition .Recognizer()

with speech_recognition.Microphone() as source:
    print("Adjusting noise ")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("Recording for 4 seconds")
    recorded_audio = recognizer.listen(source, timeout=4)
    print("Done recording")

try:
    print("Recognizing the text")
    text = recognizer.recognize_google(
            recorded_audio, 
            language="en-US"
        )     
    print("Decoded Text : {}".format(text))

except Exception as ex:
    print(ex)
