# Funciona solo con la version 0.28 de chatGPT
# Para instalar es version pip install openai==0.28
import openai

openai.api_key = "INSERTE SU API"
system_rol = """
                Analizador de sentimientos:
                Yo te paso los sentimientosy tu analizas el sentimiento de los mensajes
                y me das una respuesta con al menos 1 caracter y como maximo 4 caracteres
                SOLO RESPUESSTAS NUMERICAS. donde -1 es negatividad maxima, 0 es neutral y 1 positividad maxima
                (Solo puedes responder con inits y floats)
                """

mensajes = [{"role": "system", "content": system_rol}]

class AnalizadorDeSentimientos:
    def analizar_sentimiento(self, polaridad):
        if -0.6 < polaridad <= -0.3:
            return "\x1b[1;31m" + "Negativo"+ "\x1b[0;37m"
        elif -0.3 < polaridad < -0.1:
            return "\x1b[1;31m" + "Algo Negativo" + "\x1b[0;37m"
        elif -0.1 <= polaridad <= 0.1:
            return "\x1b[1;33m" + "Neutral" + "\x1b[0;37m"
        elif 0.1 <= polaridad <= 0.4:
            return "\x1b[1;32m" + "Algo positivo" + "\x1b[0;37m"
        elif 0.4 <= polaridad <= 0.9:
            return "\x1b[1;32m" + "Positivo" + "\x1b[0;37m"
        elif polaridad > 0.9:
            return "\x1b[1;32m" + "Muy positivo" + "\x1b[0;37m"
        else:
            return "\x1b[1;31m" + "Muy negativo" + "\x1b[0;37m"


analizador = AnalizadorDeSentimientos()

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