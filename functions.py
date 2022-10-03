import os, discord, functions, openai, random, settings

from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_response(message, character):

    #Configuration for the openAI model.
    response = openai.Completion.create(
          model="text-davinci-002",                                   #model used for text generation
          prompt=character + "\nPerson: " + message + ".",   #data that is sent to openAI API.
          temperature=settings.temp_val,
          max_tokens=settings.token_val,                              #max length of message that can be generated.
          top_p=settings.top_p_val,                  
          best_of=settings.best_of_val,                               # # of responses that are generated, picks best from n
          frequency_penalty=settings.freq_penalty_val,                #higher the number, the more random the responses will be. lower the number, the more they will conform to 
          presence_penalty=settings.pres_penalty_val,
          stop=["Person:"]
        )
    print(character + "\n\nPerson: " + message + "\n\nSummit:")

    print (response["choices"][0]["text"])
    return response["choices"][0]["text"]

def generate_typetime(msg):
    return (len(msg)/settings.t_speed_multiplier)

def mit_image():
    return("Speaking of work, I'm so glad I'm a sewer worker, selfie I took right now :sunglasses: \nhttps://cdn.discordapp.com/attachments/667593657477758998/997321680139591800/IMG_0201.jpg")