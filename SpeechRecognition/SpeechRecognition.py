import speech_recognition as sr


text = ""

isWorking = True

r = sr.Recognizer()

while isWorking:
    with sr.Microphone() as source:
        print("Listen...")

        # recognize speech using Google
        try:
                audio = r.listen(source)
                tmp = r.recognize_google(audio, language = 'ru-RU')
                print("google thinks you said " + tmp)
                text += tmp
                text += '\n'
        except sr.UnknownValueError:
            print("Google could not understand audio")
        except sr.RequestError as e:
            print("Google error; {0}".format(e))
        except KeyboardInterrupt:
            isWorking = False

with open(".\output.txt", "a") as output:
    output.write(text)
