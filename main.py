import discord
import openai

TOKEN = ''
KEY = ''
CHANNEL = 9999999999999

# initialize for discord
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# initialize for openAI
openai.api_key = KEY

# initialize for logic
message_list = ['please tell me. you can input some talk with me.', 'empty']
_counter = 0

# event @ invoke
@client.event
async def on_ready():
    print('ログインしますた')

# event @ recv message
@client.event
async def on_message(message):
    if message.channel.id == CHANNEL:
        # ignore message by bot
        if message.author.bot:
            return
        global _counter
        if _counter > 0 :
            _counter = 0
        else :
            _counter = _counter + 1
        print(message.content)
        print("_counter : " + str(_counter))
        print(message_list)
        print('------------------')
        message_list[_counter] = message.content
        print(message_list)
        print('access index : ' + str((_counter - 1) * -1))

        # if type /neko then throw question to chatGPT.
        if message.content == '/neko' :
            _prompt = message_list[ (_counter - 1) * -1 ] 
            print('prompt : ' + _prompt)

            # connected openAI use gpt 3.5
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role":"user", "content" : _prompt},
                ]
            )
            await message.channel.send(response.choices[0]["message"]["content"])

# bot invoke and connect discord server
client.run(TOKEN)
