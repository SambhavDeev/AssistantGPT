import openai
import pyttsx3
import speech_recognition as sr
#import time

openai.api_key = ""#write your api key
engine = pyttsx3.init()  # txt2spch


def adio_2_txt(filename):
    recognizer = sr.Recognizer()
    with sr.Audiofile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except:
        print("Skipping unknown error")


def gnrt_rspns(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response["choices"][0]["text"]


def spk_txt(text):
    engine.say(text)
    engine.runAndWait()


def main():
    while True:
        print("Say 'smbhv' to start recording your question")
    with sr.Microphone() as source:
        recognizer = sr.Recognizer()
        audio = reognizer.listen(source)
        try:
            transcription = recognizer.recognize_google(audio)
            if transcription.lower() == "smbhv":
                # record audio
                filename = "input.wav"
                print("Say Your Question")
                with sr.Microphone() as source:
                    recognizer = sr.Recognizer()
                    source.pause_threshold = 1
                    audio = recognizer_listen(source, phrase_time_limit=None, timeout=None)
                    with open(filename, "wb") as f:
                        f.write(audio.get_wav_data())

                text = adio_2_txt(filename)
                if text:
                    print("You said:{text}")
                    respone = gnrt_rspns(text)  # generate responses through gpt
                    print(f"GPT-3 says:{respone}")
                    spk_txt(response)
        except Exception as e:
            print("An error occured{}".format(e))


if __name__ == "__main__":
    main()