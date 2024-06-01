API_TOKEN = "7413418087:AAFa6s3SHansZSn4ZomK6v1pTWFxYZejGKM"
CHAT_ID = "6915234050"
URL = "https://777xbets.com/vgames/exclusive/fortunetiger"

import json
import requests
import telebot

bot = telebot.TeleBot(API_TOKEN)


def 777xbets():
    resposta = requests.get(URL)
    return resposta.text


def telegram(texto):
    bot.send_message(CHAT_ID, texto)


def pegar_resultado(resposta):
    lista_resultados = []
    json_valores = json.loads(resposta)
    for index, valor in enumerate(json_valores):
        if index < 4:
            if float(valor["fortune_tiger"]) >= 2.0:
                lista_resultados.append(valor["fortune_tiger"])
                print("bom", valor["fortune_tiger"])
            else:
                print("ruim", valor["fortune_tiger"])
    return lista_resultados


if __name__ == "__main__":
    resposta = 777xbets()
    lista_resultados = pegar_resultado(resposta)
    if len(lista_resultados) > 1:
        telegram("Entrada no jogo tiger")
