import speech_recognition as sr
import webbrowser as wb

reconocimiento = sr.Recognizer()

# Especificar el archivo de audio de entrada
with sr.Microphone() as source:
    print("Hola, en que puedo ayudarte?")
    audio = reconocimiento.listen(source)

# Imprimir el texto de audio
print("Acabas de decir: ")
frase = reconocimiento.recognize_google(audio, language="es-EC")
print(frase)
url = "https://www.google.com/search?q="
wb.open(url+frase)