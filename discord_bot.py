from page import *
from scraper import *
import discord
from discord.ext import commands
from discordmovie import details

with open('token.txt', 'r') as f:
    token = f.read()

class MyClient(discord.Client):

    d = discord.Guild.member_count
    # for i in d.__str__:
    #     print(i)
    async def on_ready(self):
        print(f'Logged on as {self.user}')

    async def on_message(self, message):

        channel = 'movie-bot-channel'
        bot = 'Movie Bot#8413'
        
        if message.author != self.user:

            if str(message.channel) == channel:
                
                if message.content == '!':
                    embed = discord.Embed(title='Bot Commands')

                    embed.add_field(name='!movie {movie name}',value='Movie Details')
                    embed.add_field(name='!users',value ='Users count')

                    await message.channel.send(embed=embed)

                elif message.content.startswith('!movie'):

                    movie_name = message.content.replace('!movie ','')
                    movie_details = details(movie_name)

                    embed = discord.Embed(title='Movie Info')
                    for k, v in movie_details.items():
                        embed.add_field(name=k,value=v)

                    await message.channel.send(content=None,embed=embed)

                elif message.content == '!users':
                    await message.channel.send(f'Online users are : {discord.Guild.member_count}')

                else:
                    await message.channel.send('Unknown command type ! for help')
                
            else:

                await message.channel.send(f'Please type your commands in {channel} tab')




intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.all
client = MyClient(intents=intents)
client.run(token)
