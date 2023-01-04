import openai
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

openai.api_key = "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"

def start(update, context):
    update.message.reply_text("Bonjour ! Je suis un bot qui utilise l'API de OpenAI pour compléter des phrases et répondre à vos questions. Pour utiliser mon service, envoyez-moi une phrase ou une question et je ferai de mon mieux pour y répondre.")

def respond(update, context):
    # Récupération du message envoyé par l'utilisateur
    message = update.message.text
    # Utilisation de l'API de OpenAI pour compléter la phrase
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message,
        max_tokens=3000,
        temperature=0,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # Récupération de la réponse de l'API
    reply = response["choices"][0]["text"]
    # Envoi de la réponse à l'utilisateur
    update.message.reply_text(reply)

# Création de l'objet Updater
updater = Updater("35863806224:AAH1Goj9EVNJPhLKxS5T5adSbgqOe5uZXxw", use_context=True)

# Récupération de l'objet Dispatcher
dispatcher = updater.dispatcher

# Ajout des handlers pour gérer les commandes
dispatcher.add_handler(CommandHandler("start", start))

# Ajout d'un handler pour traiter les messages envoyés par les utilisateurs
dispatcher.add_handler(MessageHandler(Filters.text, respond))

# Démarrage du bot
updater.start_polling()






