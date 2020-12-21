import os
import speech_recognition as sr

voice = sr.Recognizer()

def add(x):
    if "plus" in x:
        values = x.split('plus')
        val1 = values[0]
        val2 = values[1]
        add = int(val1) + int(val2)
        os.system("say 'The answer is '" + str(add))
    else:
        values = x.split('+')
        val1 = values[0]
        val2 = values[1]
        add = int(val1) + int(val2)
        os.system("say 'The answer is '" + str(add))


def subtract(x):
    if "minus" in x:
        values = x.split('minus')
        val1 = values[0]
        val2 = values[1]
        minus = int(val1) - int(val2)
        os.system("say 'The answer is '" + str(minus))
    else:
        values = x.split('-')
        val1 = values[0]
        val2 = values[1]
        minus = int(val1) - int(val2)
        os.system("say 'The answer is '" + str(minus))


def multiply(x):
    if "times" in x:
        values = x.split('times')
        val1 = values[0]
        val2 = values[1]
        multiplied = int(val1) * int(val2)
        os.system("say 'The answer is '" + str(multiplied))
    else:
        values = x.split('*')
        val1 = values[0]
        val2 = values[1]
        multiplied = int(val1) * int(val2)
        os.system("say 'The answer is '" + str(multiplied))


def divide(x):
    if "divided by" in x:
        values = x.split('divided by')
        val1 = values[0]
        val2 = values[1]
        divided = int(val1) / int(val2)
        os.system("say 'The answer is '" + str(divided))
    else:
        values = x.split('/')
        val1 = values[0]
        val2 = values[1]
        divided = int(val1) / int(val2)
        os.system("say 'The answer is '" + str(divided))


while True:
    with sr.Microphone() as source:
        audio = voice.listen(source)
        try:
            source = voice.recognize_google(audio)
            if "+" in source or "plus" in source:
                add(source)
            if "-" in source or "minus" in source:
                subtract(source)
            if "*" in source or "times" in source:
                multiply(source)
            if "/" in source or "divided by" in source:
                divide(source)
            else:
                convo(source)
        except sr.UnknownValueError:
            os.system("say 'Sorry  I didnt hear you'")

