import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

#Escuchar microfono y devolver audio como texto
def transformar_audio_en_texto():
    
    #Almacenamos recognizer en variable
    r = sr.Recognizer()
    
    #Configurar el microfono
    with sr.Microphone() as origen:
        
        r.pause_threshold = 0.8 #Tiempo de espera
        print("Ya puedes hablar") 
        
        audio = r.listen(origen) #Escuchamos el audio
        
        try: 
            #buscar en google
            pedido = r.recognize_google(audio, language="es-ar")
            print("Dijiste: " + pedido) #Probar lo que escucho
            
            return pedido
        
        except sr.UnknownValueError: #Error si no comprende el audio (valor desconocido)
            print("Ups, no entendí")
            return "Sigo esperando" 
        
        except sr.RequestError: #Error si no puede resolver el pedido
            print("Ups, no hay servicio")
            return "Sigo esperando"
        
        except:
            print("Ups, algo salió mal")
            return "Sigo esperando"
        
#Funcion para que el asistente pueda responder
def hablar(mensaje):
    engine = pyttsx3.init() #Iniciar el motor de pyttsx3
    
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    
    engine.say(mensaje) #Decir el mensaje
    engine.runAndWait() #Esperar y ejecutar

    
#Funcion para informar dia de la semana
def pedir_dia():
    dia = datetime.date.today() #Variable para el dia de hoy
    dia_semana = dia.weekday() #Variable para el dia de semana
    numero_mes = dia.month
    
    #Diccionario para los dias de la semana
    dias = {0: 'Lunes', 1: 'Martes', 2: 'Miércoles', 3: 'Jueves', 4: 'Viernes', 5: 'Sábado', 6: 'Domingo'}
    meses = {1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto', 9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'}

    
    hablar(f'Hoy es {dias[dia_semana]}, {dia.day} de {meses[numero_mes]}')
    
#Funcion para informar la hora
def pedir_hora():
    hora = datetime.datetime.now() #Variable para la hora actual
    print(hora)
    hablar(f'En este momento son las {hora.hour} horas con {hora.minute} minutos')
    

#Funcion de saludo inicial
def saludo_inicial():
    hablar("Hola Piju, soy tu asistente personal. ¿En qué puedo ayudarte?")
    

#Funcion principal del asistente
def pedidos(): 
    saludo_inicial()
    comenzar = True
    
    #loop central
    while comenzar:
        
        #activar microfono y guardar pedido
        pedido = transformar_audio_en_texto().lower()
        
        # A continuacion, los distintos pedidos que puede completar el asistente
        if 'abrir youtube' in pedido: 
            hablar("Oka, Abriendo YouTube")
            webbrowser.open("https://www.youtube.com")
            continue
        elif 'abrir internet' in pedido or 'abrir google' in pedido:
            hablar('Dale, ya te abro internet')
            webbrowser.open("https://www.google.com")
            continue
        elif 'qué día es hoy' in pedido or 'qué día es' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido or 'decir la hora' in pedido:
            pedir_hora()
            continue