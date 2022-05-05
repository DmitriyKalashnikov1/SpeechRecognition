import speech_recognition as sr
import time

text = ""

def callback(recognizer, audio):

    global text

    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        tmp = recognizer.recognize_google(audio, language = 'ru-RU')
        print("google thinks you said " + tmp)
        text += tmp
        text += '\n'
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


def listenForSeconds(sec: int):
    r = sr.Recognizer()
    m = sr.Microphone()
  #  with m as source:
 #       r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening
    print("Start background listening")
    # start listening in the background (note that we don't have to do this inside a `with` statement)
    stop_listening = r.listen_in_background(m, callback)
    # `stop_listening` is now a function that, when called, stops background listening
    print("Listening...")
    # do some unrelated computations for sec seconds
    for i in range(sec*10):
        ##print(i)
        time.sleep(0.1)  # we're still listening even though the main thread is doing other things

    # calling this function requests that the background listener stop listening
    stop_listening(wait_for_stop=False)
    print("Stop background listening")


isWorking = True


while isWorking:
    try:
        listenForSeconds(60)
    except KeyboardInterrupt:
        isWorking = False

with open(".\output.txt", "a") as output:
    output.write(text)
