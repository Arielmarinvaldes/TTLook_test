import pyttsx3


# tipo de voz del asistente
def spanish_voice():
    change_voice('spanish-spain')
    talk("Esta es mi voz en Español")


def english_voice():
    change_voice('english-us')
    talk("This is my voice in English")


def change_voice(voice_id):
    engine.setProperty('voice', voice_id)
    engine.setProperty('rate', 138)


engine = pyttsx3.init()

# Obtener las voces instaladas
voices = [voice.id for voice in engine.getProperty('voices')]


def talk(text):
    engine.say(text)
    engine.runAndWait()
