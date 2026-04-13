import speech_recognition as sr

r=sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            print("Adjusting for ambient noise, please wait...")
            r.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            audio=r.listen(source)
            text=r.recognize_google(audio)
            text=text.lower()
            print(f"Recognized text:{text}")

            if text == "abcd":
                print("Stopping the program.")
                break
            
    except:
        print("not recognized")
        r=sr.Recognizer()
        continue
    