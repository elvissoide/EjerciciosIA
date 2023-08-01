#mporta la biblioteca y crea un objeto para el reconocimiento de voz:
import speech_recognition as sr
import pyttsx3

def audioRespuesta(frase):
    engine = pyttsx3.init()
    engine.say(frase)
    engine.runAndWait()

def audioEntrada():
    # Especificar el archivo de audio de entrada
    reconocimiento = sr.Recognizer()
    with sr.Microphone() as source:
        texto = "Ingresa el audio a transcrbir:"
        print("ASISTENTE:",texto)
        audioRespuesta(texto)
        audio = reconocimiento.listen(source)

    # Imprimir el texto del audio
    frase=reconocimiento.recognize_google(audio, language="es-EC")
    print("USUARIO: ",frase)
    return frase

# condicionales

while True:
    try:
        frase = audioEntrada()

        if frase == "salir":
            print("ASISTENTE: Hasta pronto")
            audioRespuesta("Hasta pronto")
            break

        else:
            frase = audioEntrada()
            print("TEXTO:", frase)
            audioRespuesta("Texto transcrito")

    except sr.UnknownValueError:
        print("ASISTENTE: Lo siento, no pude entender lo que dijiste. ¿Podrías repetirlo?")
        audioRespuesta("Lo siento, no pude entender lo que dijiste.")