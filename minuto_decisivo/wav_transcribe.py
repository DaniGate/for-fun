#!/usr/bin/env python3

# obtain file from the input arguments
def wav_transcribe(WAV_FILE, lang = "es-ES"):
    """ Transcribes a WAV file containing a speech into text
        using Google text-to-speech algorithm and returns the
        complete transcription in text format """

    import speech_recognition as sr
    import sys

    r = sr.Recognizer()
    fulltext = ""

    with sr.WavFile(WAV_FILE) as source:
        audio = r.record(source) # read the entire WAV file

        # recognize speech using Google Speech Recognition
        try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
            textfromwav = r.recognize_google(audio,language = lang)
            # print("Google Speech Recognition thinks you said ")
            print("\"" + textfromwav + "\"")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return textfromwav
