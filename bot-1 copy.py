from dotenv import dotenv_values
from owlmind.pipeline import ModelProvider
from owlmind.simple import SimpleEngine
from owlmind.discord import DiscordBot

DISCORD_TOKEN = 'DISCORD TOKEN'
SERVER_URL='Server url'
SERVER_MODEL='Model'
SERVER_TYPE='Type'
SERVER_API_KEY="APIkey"

if __name__ == '__main__':

    # load token from .env
    config = dotenv_values('.env')
    # TOKEN = config[DISCORD_TOKEN]
    TOKEN = DISCORD_TOKEN
    URL = SERVER_URL
    MODEL = SERVER_MODEL
    TYPE = SERVER_TYPE
    API_KEY = SERVER_API_KEY

    # Configure a ModelProvider if there is an URL
    provider = ModelProvider(type=TYPE,  base_url=URL, api_key=API_KEY, model=MODEL) if URL else None

    # Load Simples Bot Brain loading rules from a CSV
    engine = SimpleEngine(id='bot-1')
    engine.model_provider = provider
    engine.load('rules/bot-rules-5.csv')

    # Kick start the Bot Runner process
    bot = DiscordBot(token=TOKEN, engine=engine, debug=True)
    bot.run()