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
        print("ASISTENTE: Hola, en que puedo ayudarte")
        audioRespuesta("Hola, en que puedo ayudarte")
        audio = reconocimiento.listen(source)

    # Imprimir el texto del audio
    frase=reconocimiento.recognize_google(audio, language="es-EC")
    print("USUARIO: ",frase)
    return frase

# condicionales

while True:
    try:
        frase = audioEntrada()
        if frase == "enciende la luz" or frase == "prende la luz":
            print("ASISTENTE: Luz encendida")
            audioRespuesta("Luz encendida")

        elif frase == "apaga la luz":
            print("ASISTENTE: Luz apagada")
            audioRespuesta("Luz apagada")

        elif frase == "enciende el ventilador" or frase == "prende el ventilador":
            print("ASISTENTE: Ventilador encendido")
            audioRespuesta("Ventilador encendido")

        elif frase == "riega la planta" or frase == "humedece la planta":
            print("ASISTENTE: Planta regada")
            audioRespuesta("Planta regada")

        elif frase == "salir":
            print("ASISTENTE: Hasta luego. ¡Que tengas un buen día!")
            break

        else:
            print("ASISTENTE: No tengo esa instrucción en mi base de datos. Vuelve a repetirla.")
            audioRespuesta("Instrucción no reconocida")

    except sr.UnknownValueError:
        print("ASISTENTE: Lo siento, no pude entender lo que dijiste. ¿Podrías repetirlo?")
        audioRespuesta("Lo siento, no pude entender lo que dijiste.")