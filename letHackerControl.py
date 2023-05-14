import discord
import keyboard
import asyncio


client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")
    channel = discord.utils.get(client.get_all_channels(), name='CHANNEL NAME')
    await channel.send("Bot is now listening for messages...")
    @client.event
    async def on_message(message):
        if message.channel.name == "CHANNEL NAME" and message.author != client.user:
            for letter in message.content:
                keyboard.press(letter)
                keyboard.release(letter)
                await asyncio.sleep(0.1)

client.run("UR TOKEN")
