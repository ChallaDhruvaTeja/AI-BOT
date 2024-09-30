from typing import Any

import speech_recognition as sr
import pyttsx4
import datetime
import wikipedia
import wolframalpha

r = sr.Recognizer()
machine = pyttsx4.init()


def talk(text):
    machine.say(text)
    machine.runAndWait()


def takecommand():
    try:
        with sr.Microphone(device_index=0) as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source)
            speech = r.listen(source)
            instruction = r.recognize_google(speech)
            instruction = instruction.lower()
            if "leo" in instruction:
                instruction = instruction.replace('leo', "")
                return instruction
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print("Could not request results from Google; {0}".format(e))
    return None


def runcommand():
    instruction = ''
    while instruction != 'exit':
        instruction: Any | None = takecommand()
        print(instruction)
        if instruction:
            if instruction is not None and 'exit' in instruction:
                break

            elif instruction is not None and 'time' in instruction:
                time = datetime.datetime.now().strftime("%I:%M %p")
                talk("The current time is:" + time)
                print(time)

            elif instruction is not None and 'date' in instruction:
                date = datetime.datetime.now().strftime('%d /%m /%y')
                talk("Today's date is " + date)
                print(date)

            elif instruction is not None and ' ' in instruction:
                try:
                    app_id = '3TTWQK-VVRPYWPJQ3'
                    client = wolframalpha.Client(app_id)
                    res = client.query(instruction)
                    answer = next(res.results).text
                    print(answer)
                    talk("Your Answer is " + answer)

                except:
                    instruction = instruction.split(' ')
                    instruction = " ".join(instruction[0:])
                    talk("I am Searching for " + instruction)
                    print(wikipedia.summary(instruction, sentences=3))
                    talk(wikipedia.summary(instruction, sentences=3))


if __name__ == '__main__':
    runcommand()
