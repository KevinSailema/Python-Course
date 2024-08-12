# Funciona solo con la version 0.28 de chatGPT
# Para instalar es version pip install openai==0.28
import openai

# Codigo optimizado quitando dependencias

openai.api_key = "INSERTE SU API"
system_rol = """
                Analizador de sentimientos:
                Yo te paso los sentimientosy tu analizas el sentimiento de los mensajes
                y me das una respuesta con al menos 1 caracter y como maximo 4 caracteres
                SOLO RESPUESSTAS NUMERICAS. donde -1 es negatividad maxima, 0 es neutral y 1 positividad maxima
                (Solo puedes responder con inits y floats)
                """

mensajes = [{"role": "system", "content": system_rol}]

class Sentimiento:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
    
    def __str__(self):
        return "\x1b[1;{}m{}\x1b[0;0,37m".format(self.color, self.nombre)

class AnalizadorDeSentimientos:
    def __init__(self, rangos):
        self.rangos = rangos      

    def analizar_sentimiento(self, polaridad):
        for rango, sentimiento in self.rangos:
            if rango [0] < polaridad <=  rango [1]:
                return sentimiento
        return Sentimiento("Muy negativo", "31")

rangos = [
    ((-0.6, -0.3), Sentimiento("negativo", "31")),
    ((-0.3 ,-0.1), Sentimiento("algo negativo", "31")),
    ((-0.1 , 0.1), Sentimiento("neutral", "33")),
    ((0.1 , 0.4), Sentimiento("algo positivo", "32")),
    ((0.4 , 0.9), Sentimiento("positivo", "32")),
    ((0.9 , 1), Sentimiento("muy positivo", "32"))
]

analizador = AnalizadorDeSentimientos(rangos)

while True:
    user_prompt = input("\x1b[1;33m" + "\n Dime como te sientes: " + "\x1b[0;37m")
    mensajes.append({"role": "user", "content": user_prompt})

# pylint: disable=no-member
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=mensajes,
        max_tokens=8
    )

    respuesta = completion.choices[0].message["content"]
    mensajes.append({"role": "assistant", "content": respuesta })

    sentimiento = analizador.analizar_sentimiento(float(respuesta))
    print(sentimiento)